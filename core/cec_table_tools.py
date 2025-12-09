"""
CEC Table Lookup Tools
Provides deterministic access to CEC 2022 (California Electrical Code) tables for electrical calculations and specifications

The CEC 2022 is based on NEC 2020 with California-specific amendments.
Tables marked with California amendments have been updated from the base NEC tables.
"""
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Union

# Import shared utilities from NEC table tools
from core.nec_table_tools import (
    safe_get_numeric_value,
    parse_range_value,
    normalize_separator
)
import re


class CECTableTools:
    """Class to handle CEC 2022 table lookups and calculations"""

    def __init__(self, tables_file_path: str = None):
        """Initialize with CEC tables data"""
        if tables_file_path is None:
            # Default path relative to this file
            current_dir = Path(__file__).parent
            tables_file_path = current_dir.parent / "data" / "CEC_2022" / "cec_tables_unified.json"

        self.tables_file = Path(tables_file_path)
        self.tables_data = self._load_tables()

    def _load_tables(self) -> Dict[str, Any]:
        """Load CEC tables from JSON file"""
        try:
            with open(self.tables_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"Loaded {data['metadata']['total_tables']} CEC tables")
            return data
        except Exception as e:
            print(f"Error loading CEC tables: {e}")
            return {"metadata": {"total_tables": 0}, "tables": {}}

    def _extract_cross_refs(self, notes: List[str]) -> List[str]:
        """
        Extract section and table references from footnote text.

        Parses footnote text for cross-references like:
        - "Section 240.4(D)"
        - "Table 310.15(B)"
        - "See 210.23(A)"

        Args:
            notes: List of footnote/note text strings

        Returns:
            List of extracted section/table references (e.g., ["240.4(D)", "310.15(B)"])
        """
        refs = []
        for note in notes:
            # Match "Section X.X(Y)" patterns
            section_matches = re.findall(r'Section\s+(\d+\.\d+(?:\([A-Za-z0-9]+\))*)', note)
            refs.extend(section_matches)

            # Match "Table X.X(Y)" patterns
            table_matches = re.findall(r'Table\s+(\d+\.\d+(?:\([A-Za-z0-9]+\))*)', note)
            refs.extend(table_matches)

            # Match "See X.X(Y)" patterns (common in NEC/CEC)
            see_matches = re.findall(r'See\s+(\d+\.\d+(?:\([A-Za-z0-9]+\))*)', note)
            refs.extend(see_matches)

        # Remove duplicates while preserving order
        seen = set()
        unique_refs = []
        for ref in refs:
            if ref not in seen:
                seen.add(ref)
                unique_refs.append(ref)

        return unique_refs

    def _get_applicable_notes(self, table: Dict[str, Any], row: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract applicable footnotes and cross-references for a table row.

        Looks for:
        1. Row-level note markers (e.g., "note": "*") and matches them to footnotes
        2. General table notes that may apply

        Args:
            table: Full table data dict
            row: The specific row being looked up

        Returns:
            Dict with:
                - applicable_notes: List of note text strings
                - cross_references: List of extracted section references
        """
        applicable_notes = []

        # Check for row-level note markers (e.g., "note": "*")
        row_note_marker = row.get("note")
        if row_note_marker:
            # Check footnotes array (uses "marker" field)
            for footnote in table.get("footnotes", []):
                if footnote.get("marker") == row_note_marker:
                    applicable_notes.append(footnote.get("text", ""))

            # Check notes array (can use either "marker" or "number" field)
            for note in table.get("notes", []):
                # Some notes use "marker" (like the 240.4(D) note), others use "number"
                if note.get("marker") == row_note_marker or note.get("number") == row_note_marker:
                    applicable_notes.append(note.get("text", ""))

        # Extract cross-references from all applicable notes
        cross_refs = self._extract_cross_refs(applicable_notes)

        return {
            "applicable_notes": applicable_notes,
            "cross_references": cross_refs
        }

    def _normalize_table_id(self, table_id: str) -> str:
        """
        Normalize table ID to standard format with 'Table ' prefix.

        Args:
            table_id: Raw table ID (e.g., "310.16" or "Table 310.16")

        Returns:
            Normalized table ID (e.g., "Table 310.16")
        """
        table_id = table_id.strip()
        # Don't add "Table " if it's already there or if it's a Chapter 9 table
        if table_id.startswith("Chapter 9") or table_id.startswith("Table "):
            return table_id
        return f"Table {table_id}"

    def get_table_info(self, table_id: str) -> Optional[Dict[str, Any]]:
        """Get general information about a table"""
        table_id = self._normalize_table_id(table_id)
        if table_id in self.tables_data["tables"]:
            table = self.tables_data["tables"][table_id]
            result = {
                "table_id": table["table_id"],
                "caption": table["caption"],
                "description": table["description"],
                "section": table["section"],
                "keywords": table["keywords"]
            }
            # Include California amendment info if present
            if table.get("california_amendment"):
                result["california_amendment"] = True
                result["amendment_type"] = table.get("amendment_type", "delta")
            return result
        return None

    def lookup_conductor_ampacity(self, conductor_size: str, temperature_rating: str = "75°C",
                                 conductor_type: str = "copper") -> Dict[str, Any]:
        """
        Look up conductor ampacity from CEC 2022 Table 310.16

        Args:
            conductor_size: Wire size (e.g., "12 AWG", "2/0 AWG", "250 kcmil")
            temperature_rating: "60°C", "75°C", or "90°C"
            conductor_type: "copper" or "aluminum"

        Returns:
            Dict with ampacity value, table reference, and applicable footnotes/cross-references
        """
        table_310_16 = self.tables_data["tables"].get("Table 310.16")
        if not table_310_16:
            return {"error": "Table 310.16 not found"}

        # Normalize inputs - just get the size number/designation
        size_normalized = conductor_size.upper().strip()
        if " AWG" in size_normalized:
            size_normalized = size_normalized.replace(" AWG", "")
        if " KCMIL" in size_normalized:
            size_normalized = size_normalized.replace(" KCMIL", "")

        # Create column key based on actual structure
        temp_suffix = temperature_rating.replace("°C", "c").lower()
        material_prefix = "copper" if conductor_type.lower() == "copper" else "aluminum"
        ampacity_key = f"{material_prefix}_{temp_suffix}"

        # Find matching row
        for row in table_310_16["rows"]:
            row_size = row.get("size", "").strip()
            if row_size == size_normalized:
                ampacity_raw = row.get(ampacity_key)

                # Use global utility to safely convert to numeric value
                ampacity = safe_get_numeric_value(ampacity_raw, ampacity_key)

                if ampacity is not None:
                    # Get applicable notes and cross-references for this row
                    notes_info = self._get_applicable_notes(table_310_16, row)

                    result = {
                        "ampacity": int(ampacity) if ampacity == int(ampacity) else ampacity,
                        "conductor_size": conductor_size,
                        "temperature_rating": temperature_rating,
                        "conductor_type": conductor_type,
                        "table_reference": "CEC 2022 Table 310.16",
                        "description": table_310_16["description"],
                        "applicable_notes": notes_info["applicable_notes"],
                        "cross_references": notes_info["cross_references"]
                    }
                    # Note if this is a California amendment
                    if table_310_16.get("california_amendment"):
                        result["california_amendment"] = True
                    return result

        return {"error": f"Conductor size {conductor_size} ({size_normalized}) not found in Table 310.16 or no ampacity for {conductor_type} at {temperature_rating}"}

    def lookup_working_space(self, voltage_to_ground: int, condition: int) -> Dict[str, Any]:
        """
        Look up working space requirements from CEC 2022 Table 110.26(A)(1)

        Args:
            voltage_to_ground: Voltage in volts (e.g., 120, 277, 480)
            condition: Condition number 1, 2, or 3

        Returns:
            Dict with working space depth, table reference, and applicable notes/cross-references
        """
        table_110_26 = self.tables_data["tables"].get("Table 110.26(A)(1)")
        if not table_110_26:
            return {"error": "Table 110.26(A)(1) not found"}

        # Find appropriate voltage range
        for row in table_110_26["rows"]:
            voltage_range = row.get("voltage_range", "")

            # Use global utility to parse ANY range format
            matches, _ = parse_range_value(voltage_range, voltage_to_ground)

            if matches:
                condition_key = f"condition_{condition}"
                clearance = row.get(condition_key)

                # Handle None values (not-applicable conditions)
                if clearance is None or (isinstance(clearance, str) and clearance.strip().lower() == "none"):
                    return {"error": f"Working space clearance is not available for voltage range {voltage_range}, condition {condition}"}

                # Get applicable notes and cross-references for this row
                notes_info = self._get_applicable_notes(table_110_26, row)

                # Also get condition descriptions from table notes if available
                condition_descriptions = []
                for note in table_110_26.get("notes", []):
                    note_text = note.get("text", "")
                    if f"Condition {condition}" in note_text or f"condition {condition}" in note_text.lower():
                        condition_descriptions.append(note_text)

                result = {
                    "working_space_depth": clearance,
                    "voltage_to_ground": voltage_to_ground,
                    "condition": condition,
                    "voltage_range": voltage_range,
                    "table_reference": "CEC 2022 Table 110.26(A)(1)",
                    "description": table_110_26["description"],
                    "applicable_notes": notes_info["applicable_notes"],
                    "cross_references": notes_info["cross_references"],
                    "condition_descriptions": condition_descriptions
                }
                if table_110_26.get("california_amendment"):
                    result["california_amendment"] = True
                return result

        return {"error": f"Voltage {voltage_to_ground}V not found in working space table"}

    def search_tables_by_keyword(self, keyword: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Search for tables by keyword

        Args:
            keyword: Search term
            limit: Maximum number of results

        Returns:
            List of matching tables with basic info
        """
        keyword_lower = keyword.lower()
        matches = []

        for table_id, table_data in self.tables_data["tables"].items():
            # Search in keywords, caption, and description
            search_fields = [
                " ".join(table_data.get("keywords", [])),
                table_data.get("caption", ""),
                table_data.get("description", "")
            ]

            if any(keyword_lower in field.lower() for field in search_fields):
                result = {
                    "table_id": table_id,
                    "caption": table_data.get("caption", ""),
                    "section": table_data.get("section", ""),
                    "keywords": table_data.get("keywords", [])[:5]
                }
                if table_data.get("california_amendment"):
                    result["california_amendment"] = True
                matches.append(result)

                if len(matches) >= limit:
                    break

        return matches

    def get_table_data(self, table_id: str, row_filter: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Get complete table data with optional row filtering

        Args:
            table_id: CEC table identifier
            row_filter: Optional dict to filter rows (e.g., {"voltage_range": "151-600"})

        Returns:
            Complete table data or filtered subset, including notes and footnotes
        """
        # Normalize table ID to standard format
        table_id = self._normalize_table_id(table_id)

        # Tier 1: Try exact match first (fastest)
        table = self.tables_data["tables"].get(table_id)

        # Tier 2: If no exact match, try fuzzy/prefix matching
        if not table:
            matching_tables = [
                tid for tid in self.tables_data["tables"].keys()
                if tid.startswith(table_id)
            ]

            if matching_tables:
                matched_id = sorted(matching_tables)[0]
                table = self.tables_data["tables"][matched_id]

                fuzzy_match_note = ""
                if len(matching_tables) > 1:
                    other_tables = [t for t in sorted(matching_tables) if t != matched_id]
                    fuzzy_match_note = f"\n\nNote: Multiple tables match '{table_id}': {', '.join(matching_tables)}. Showing {matched_id}. To access others, use specific table ID."
            else:
                return {"error": f"Table {table_id} not found"}
        else:
            fuzzy_match_note = ""

        result = {
            "table_id": table["table_id"],
            "caption": table["caption"],
            "description": table["description"] + fuzzy_match_note,
            "section": table["section"],
            "headers": table.get("headers", []),
            "rows": table.get("rows", []),
            # Include notes and footnotes - these often contain critical cross-references
            "notes": table.get("notes", []),
            "footnotes": table.get("footnotes", [])
        }

        # Extract all cross-references from notes and footnotes
        all_note_texts = []
        for note in result["notes"]:
            if isinstance(note, dict):
                all_note_texts.append(note.get("text", ""))
            elif isinstance(note, str):
                all_note_texts.append(note)
        for footnote in result["footnotes"]:
            if isinstance(footnote, dict):
                all_note_texts.append(footnote.get("text", ""))
            elif isinstance(footnote, str):
                all_note_texts.append(footnote)

        result["cross_references"] = self._extract_cross_refs(all_note_texts)

        # Include California amendment info
        if table.get("california_amendment"):
            result["california_amendment"] = True
            result["amendment_type"] = table.get("amendment_type", "delta")

        # Apply row filtering if specified
        if row_filter and result["rows"]:
            filtered_rows = []
            for row in result["rows"]:
                match = True
                for key, value in row_filter.items():
                    if row.get(key) != value:
                        match = False
                        break
                if match:
                    filtered_rows.append(row)
            result["rows"] = filtered_rows

        return result

    def lookup_temperature_correction(
        self,
        ambient_temp: float,
        conductor_temp_rating: str,
        base_temp: str = "30°C"
    ) -> Dict[str, Any]:
        """
        Look up temperature correction factor with automatic sub-table selection.

        Args:
            ambient_temp: Ambient temperature in °C
            conductor_temp_rating: "60°C", "75°C", or "90°C"
            base_temp: "30°C" or "40°C" (default: "30°C")

        Returns:
            Dict with correction factor and table metadata
        """
        # Select correct sub-table based on base temperature
        table_id = "Table 310.15(B)(1)(1)" if base_temp == "30°C" else "Table 310.15(B)(1)(2)"

        # Get table data
        table_data = self.get_table_data(table_id)

        if "error" in table_data:
            return table_data

        # Find temperature range
        for row in table_data['rows']:
            temp_range = row.get('temp_c', '')

            # Use global utility to parse ANY range format
            matches, _ = parse_range_value(temp_range, ambient_temp)

            if matches:
                # Select correct column based on conductor rating
                column_map = {
                    "60°C": "rating_60c",
                    "75°C": "rating_75c",
                    "90°C": "rating_90c"
                }
                column = column_map.get(conductor_temp_rating)
                if not column:
                    return {"error": f"Invalid conductor temperature rating: {conductor_temp_rating}"}

                # Use global utility to safely get numeric value (handles None)
                correction_factor = safe_get_numeric_value(row.get(column), column)

                # Handle None values (not-applicable conditions)
                if correction_factor is None:
                    return {"error": f"Temperature correction factor is not available for {temp_range} at {conductor_temp_rating}"}

                result = {
                    "success": True,
                    "table_id": table_id,
                    "correction_factor": correction_factor,
                    "ambient_temp": ambient_temp,
                    "temp_range": temp_range,
                    "conductor_rating": conductor_temp_rating,
                    "base_temp": base_temp,
                    "code_reference": "CEC 2022"
                }
                return result

        return {"error": f"No temperature correction found for {ambient_temp}°C"}

    def lookup_bundling_adjustment(self, num_conductors: int) -> Dict[str, Any]:
        """
        Look up bundling adjustment factor from CEC 2022 Table 310.15(C)(1).

        Args:
            num_conductors: Number of current-carrying conductors in raceway/cable

        Returns:
            Dict with adjustment factor and table metadata
        """
        # 3 or fewer conductors = no adjustment needed
        if num_conductors <= 3:
            return {
                "success": True,
                "table_id": "Table 310.15(C)(1)",
                "num_conductors": num_conductors,
                "adjustment_factor": 1.00,
                "percent": "100",
                "conductor_range": "1-3",
                "note": "No adjustment required for 3 or fewer current-carrying conductors",
                "code_reference": "CEC 2022"
            }

        # Get table data
        table_data = self.get_table_data("Table 310.15(C)(1)")

        if "error" in table_data:
            return table_data

        # Find the matching conductor range
        for row in table_data['rows']:
            conductor_range = row.get('conductors', '')

            # Parse range like "4–6", "7–9", "10–20", "21–30", "31–40", "41 and above"
            matches, _ = parse_range_value(conductor_range, num_conductors)

            if matches:
                percent_str = row.get('percent', '')
                try:
                    adjustment_factor = float(percent_str) / 100.0
                except (ValueError, TypeError):
                    return {"error": f"Could not parse percent value: {percent_str}"}

                result = {
                    "success": True,
                    "table_id": "Table 310.15(C)(1)",
                    "num_conductors": num_conductors,
                    "adjustment_factor": adjustment_factor,
                    "percent": percent_str,
                    "conductor_range": conductor_range,
                    "code_reference": "CEC 2022"
                }

                # Check for California amendment
                if table_data.get("california_amendment"):
                    result["california_amendment"] = True

                return result

        return {"error": f"No bundling adjustment found for {num_conductors} conductors"}

    def lookup_egc_size(self, overcurrent_device_amperes: int) -> Dict[str, Any]:
        """
        Look up equipment grounding conductor size from CEC 2022 Table 250.122

        Args:
            overcurrent_device_amperes: Rating of overcurrent device in amperes

        Returns:
            Dict with copper and aluminum EGC sizes
        """
        table_250_122 = self.tables_data["tables"].get("Table 250.122")
        if not table_250_122:
            return {"error": "Table 250.122 not found"}

        # Find the row where overcurrent device rating does not exceed the table value
        for row in table_250_122["rows"]:
            row_amperes = int(row.get("amperes", 0))
            if overcurrent_device_amperes <= row_amperes:
                result = {
                    "overcurrent_device_amperes": overcurrent_device_amperes,
                    "table_amperes": row_amperes,
                    "copper_egc": row.get("copper"),
                    "aluminum_egc": row.get("aluminum"),
                    "table_reference": "CEC 2022 Table 250.122",
                    "description": table_250_122.get("description", "")
                }
                if table_250_122.get("california_amendment"):
                    result["california_amendment"] = True
                return result

        return {"error": f"Overcurrent device rating {overcurrent_device_amperes}A exceeds Table 250.122 maximum"}

    def lookup_gec_size(self, service_conductor_size: str, conductor_type: str = "copper") -> Dict[str, Any]:
        """
        Look up grounding electrode conductor size from CEC 2022 Table 250.66

        Args:
            service_conductor_size: Size of largest service conductor (e.g., "2/0", "250")
            conductor_type: "copper" or "aluminum"

        Returns:
            Dict with GEC sizes for copper and aluminum
        """
        table_250_66 = self.tables_data["tables"].get("Table 250.66")
        if not table_250_66:
            return {"error": "Table 250.66 not found"}

        # Normalize input
        size_normalized = service_conductor_size.upper().strip()
        size_normalized = size_normalized.replace(" AWG", "").replace(" KCMIL", "")

        # Determine which column to search based on conductor type
        search_column = "largest_conductor_copper" if conductor_type.lower() == "copper" else "largest_conductor_aluminum"

        for row in table_250_66["rows"]:
            row_value = row.get(search_column, "")

            # Check for exact match or range match
            if size_normalized in row_value or row_value == size_normalized:
                result = {
                    "service_conductor_size": service_conductor_size,
                    "conductor_type": conductor_type,
                    "service_conductor_range": row_value,
                    "gec_copper": row.get("grounding_conductor_copper"),
                    "gec_aluminum": row.get("grounding_conductor_aluminum"),
                    "table_reference": "CEC 2022 Table 250.66",
                    "description": table_250_66.get("description", "")
                }
                if table_250_66.get("california_amendment"):
                    result["california_amendment"] = True
                return result

        return {"error": f"Service conductor size {service_conductor_size} not found in Table 250.66"}

    def lookup_conduit_fill(self, conduit_type: str, conduit_size: str,
                           conductor_type: str, conductor_size: str,
                           num_conductors: int = 3) -> Dict[str, Any]:
        """
        Look up conduit fill data from CEC 2022 Chapter 9 tables.

        Uses Chapter 9 Table 4 (conduit dimensions) and Table 5 (conductor dimensions)
        to calculate maximum number of conductors that fit in a conduit.

        Args:
            conduit_type: Type of conduit (EMT, RMC, IMC, PVC-40, PVC-80)
            conduit_size: Trade size (1/2, 3/4, 1, 1-1/4, 1-1/2, 2, etc.)
            conductor_type: Conductor insulation type (THHN, THWN, TW, XHHW, RHH, etc.)
            conductor_size: AWG/kcmil size (14, 12, 10, 8, 6, 4, 3, 2, 1, 1/0, 2/0, etc.)
            num_conductors: Number of conductors to check if they fit (default: 3)

        Returns:
            Dict with conduit area, conductor area, max conductors, and fit verification
        """
        # Get Table 4 (conduit dimensions)
        table4 = self.get_table_data("Chapter 9 Table 4")
        if "error" in table4:
            return {"error": f"Chapter 9 Table 4 not found: {table4['error']}"}

        # Get Table 5 (conductor dimensions)
        table5 = self.get_table_data("Chapter 9 Table 5")
        if "error" in table5:
            return {"error": f"Chapter 9 Table 5 not found: {table5['error']}"}

        # Normalize conduit type
        conduit_type_upper = conduit_type.upper().strip()
        # Handle common variations
        if conduit_type_upper == "PVC":
            conduit_type_upper = "PVC-40"  # Default to Schedule 40

        # Normalize conduit size (handle "1.25" -> "1-1/4" etc.)
        conduit_size_normalized = conduit_size.strip()
        size_conversions = {
            "0.5": "1/2", "1/2": "1/2",
            "0.75": "3/4", "3/4": "3/4",
            "1": "1", "1.0": "1",
            "1.25": "1-1/4", "1-1/4": "1-1/4", "1 1/4": "1-1/4",
            "1.5": "1-1/2", "1-1/2": "1-1/2", "1 1/2": "1-1/2",
            "2": "2", "2.0": "2",
            "2.5": "2-1/2", "2-1/2": "2-1/2", "2 1/2": "2-1/2",
            "3": "3", "3.0": "3",
            "3.5": "3-1/2", "3-1/2": "3-1/2", "3 1/2": "3-1/2",
            "4": "4", "4.0": "4",
        }
        conduit_size_normalized = size_conversions.get(conduit_size_normalized, conduit_size_normalized)

        # Find matching conduit row
        conduit_area = None
        total_area = None
        for row in table4.get('rows', []):
            if (row.get('conduit_type', '').upper() == conduit_type_upper and
                row.get('trade_size', '') == conduit_size_normalized):
                conduit_area = row.get('40pct_area_sq_in')
                total_area = row.get('total_area_sq_in')
                break

        if conduit_area is None:
            return {"error": f"Conduit {conduit_type} size {conduit_size} not found in Chapter 9 Table 4"}

        # Normalize conductor type and size
        conductor_type_upper = conductor_type.upper().strip()
        conductor_size_normalized = conductor_size.upper().strip()
        conductor_size_normalized = conductor_size_normalized.replace(" AWG", "").replace("AWG", "")
        conductor_size_normalized = conductor_size_normalized.replace(" KCMIL", "").replace("KCMIL", "")

        # Find matching conductor row (try multiple matching strategies)
        conductor_area = None
        matched_conductor_type = None
        for row in table5.get('rows', []):
            row_type = row.get('conductor_type', '').upper()
            row_size = row.get('awg_size', '').upper()

            if row_size == conductor_size_normalized:
                # Check for conductor type match (handle variations like THHN vs THHN/THWN-2)
                if (conductor_type_upper in row_type or
                    row_type.startswith(conductor_type_upper) or
                    conductor_type_upper.split('/')[0] in row_type):
                    conductor_area = row.get('area_sq_in')
                    matched_conductor_type = row.get('conductor_type')
                    break

        if conductor_area is None:
            return {"error": f"Conductor {conductor_type} size {conductor_size} not found in Chapter 9 Table 5"}

        # Calculate max conductors
        max_conductors = int(conduit_area / conductor_area)
        exact_calc = conduit_area / conductor_area
        total_conductor_area = conductor_area * num_conductors
        fits = num_conductors <= max_conductors

        return {
            "conduit_type": conduit_type_upper,
            "conduit_size": conduit_size_normalized,
            "conduit_total_area": total_area,
            "conduit_area_40pct": conduit_area,
            "conductor_type": matched_conductor_type,
            "conductor_size": conductor_size_normalized,
            "conductor_area": conductor_area,
            "max_conductors": max_conductors,
            "exact_calculation": round(exact_calc, 2),
            "num_conductors_requested": num_conductors,
            "total_conductor_area": round(total_conductor_area, 4),
            "fits": fits,
            "fill_percentage": round((total_conductor_area / total_area) * 100, 1) if total_area else None,
            "table_reference": "CEC 2022 Chapter 9 Tables 4 & 5",
            "source": "CEC 2022 Chapter 9"
        }


# Function definitions for Gemini function calling
def cec_lookup_conductor_ampacity(conductor_size: str, temperature_rating: str = "75°C",
                                  conductor_type: str = "copper") -> str:
    """
    Look up conductor ampacity from CEC 2022 Table 310.16

    Args:
        conductor_size: Wire size like "12 AWG", "2/0 AWG", "250 kcmil"
        temperature_rating: Temperature rating - "60°C", "75°C", or "90°C"
        conductor_type: Conductor material - "copper" or "aluminum"

    Returns:
        String with ampacity information, CEC reference, and cross-references
    """
    tools = CECTableTools()
    result = tools.lookup_conductor_ampacity(conductor_size, temperature_rating, conductor_type)

    if "error" in result:
        return f"Error: {result['error']}"

    ca_note = " [California Amendment]" if result.get("california_amendment") else ""
    output = f"Conductor ampacity for {result['conductor_size']} {result['conductor_type']} at {result['temperature_rating']}: {result['ampacity']} amperes per {result['table_reference']}{ca_note}. {result['description']}"

    # Include applicable notes if present
    if result.get("applicable_notes"):
        output += f"\n\nApplicable Notes: {' '.join(result['applicable_notes'])}"

    # Include cross-references if present
    if result.get("cross_references"):
        output += f"\n\nCross-References (MUST be consulted): {', '.join(result['cross_references'])}"

    return output


def cec_lookup_working_space_clearance(voltage_to_ground: int, condition: int) -> str:
    """
    Look up required working space clearances from CEC 2022 Table 110.26(A)(1)

    Args:
        voltage_to_ground: Nominal voltage to ground in volts (e.g. 120, 277, 480)
        condition: Working space condition number (1, 2, or 3)

    Returns:
        String with working space requirements and CEC reference
    """
    tools = CECTableTools()
    result = tools.lookup_working_space(voltage_to_ground, condition)

    if "error" in result:
        return f"Error: {result['error']}"

    ca_note = " [California Amendment]" if result.get("california_amendment") else ""
    return f"Working space requirement for {result['voltage_to_ground']}V (condition {result['condition']}): {result['working_space_depth']} per {result['table_reference']}{ca_note}. Voltage range: {result['voltage_range']}V."


def cec_search_tables(keyword: str, limit: int = 5) -> str:
    """
    Search CEC 2022 tables by keyword to find relevant tables

    Args:
        keyword: Search term (e.g. "ampacity", "clearance", "AFCI")
        limit: Maximum number of results to return

    Returns:
        String with list of matching tables and their purposes
    """
    tools = CECTableTools()
    results = tools.search_tables_by_keyword(keyword, limit)

    if not results:
        return f"No CEC tables found matching keyword: {keyword}"

    output = [f"CEC 2022 tables related to '{keyword}':"]
    for table in results:
        ca_marker = " [CA Amendment]" if table.get("california_amendment") else ""
        output.append(f"- {table['table_id']} ({table['section']}): {table['caption']}{ca_marker}")
        if table['keywords']:
            output.append(f"  Keywords: {', '.join(table['keywords'])}")

    return "\n".join(output)


def cec_get_table_information(table_id: str) -> str:
    """
    Get detailed information about a specific CEC 2022 table

    Args:
        table_id: CEC table identifier (e.g. "Table 310.16", "Table 110.26(A)(1)")

    Returns:
        String with table description and purpose
    """
    tools = CECTableTools()
    result = tools.get_table_info(table_id)

    if not result:
        return f"Table {table_id} not found in CEC database"

    ca_note = " [California Amendment]" if result.get("california_amendment") else ""
    return f"{result['table_id']} - {result['caption']}{ca_note}\nSection: {result['section']}\nDescription: {result['description']}\nKeywords: {', '.join(result['keywords'][:10])}"


def cec_lookup_egc_size(overcurrent_device_amperes: int) -> str:
    """
    Look up equipment grounding conductor size from CEC 2022 Table 250.122

    Args:
        overcurrent_device_amperes: Rating of overcurrent device in amperes

    Returns:
        String with EGC sizes and CEC reference
    """
    tools = CECTableTools()
    result = tools.lookup_egc_size(overcurrent_device_amperes)

    if "error" in result:
        return f"Error: {result['error']}"

    ca_note = " [California Amendment]" if result.get("california_amendment") else ""
    return f"Equipment grounding conductor for {result['overcurrent_device_amperes']}A overcurrent device: Copper: {result['copper_egc']} AWG, Aluminum: {result['aluminum_egc']} AWG per {result['table_reference']}{ca_note}."


def cec_lookup_gec_size(service_conductor_size: str, conductor_type: str = "copper") -> str:
    """
    Look up grounding electrode conductor size from CEC 2022 Table 250.66

    Args:
        service_conductor_size: Size of largest service conductor (e.g., "2/0", "250")
        conductor_type: "copper" or "aluminum"

    Returns:
        String with GEC sizes and CEC reference
    """
    tools = CECTableTools()
    result = tools.lookup_gec_size(service_conductor_size, conductor_type)

    if "error" in result:
        return f"Error: {result['error']}"

    ca_note = " [California Amendment]" if result.get("california_amendment") else ""
    return f"Grounding electrode conductor for {result['service_conductor_size']} {result['conductor_type']} service conductor: Copper GEC: {result['gec_copper']} AWG, Aluminum GEC: {result['gec_aluminum']} AWG per {result['table_reference']}{ca_note}."


def cec_lookup_conductor_size_for_ampacity(
    required_ampacity: int,
    temperature_rating: str = "75°C",
    conductor_type: str = "copper",
    conductor_application: str = "general"
) -> str:
    """
    Find the MINIMUM conductor size that can handle a required ampacity.
    This is a REVERSE LOOKUP - given ampacity, find the smallest conductor.

    Use this tool when the question asks "What size conductor for X amps?"
    NOT for "What is the ampacity of X AWG conductor?"

    Args:
        required_ampacity: The minimum ampacity needed (e.g., 60 for a 60A circuit)
        temperature_rating: Temperature rating - "60°C", "75°C", or "90°C" (ignored for service applications)
        conductor_type: Conductor material - "copper" or "aluminum"
        conductor_application: Application type determines which table to use:
            - "general" (default): Table 310.16 for branch circuits, feeders, general wiring
            - "service": Table 310.12(A) for single-phase dwelling services and feeders
              Use "service" when question mentions: "service", "200A service", "service entrance",
              "dwelling service", "service conductors", "main service"

    Returns:
        String with the minimum conductor size and verification context

    Example:
        cec_lookup_conductor_size_for_ampacity(60, "75°C", "copper", "general")
        → Returns "6 AWG" (which has 65A at 75°C per Table 310.16)

        cec_lookup_conductor_size_for_ampacity(150, "75°C", "aluminum", "service")
        → Returns "2/0 AWG" (per Table 310.12(A) for dwelling services)
    """
    tools = CECTableTools()

    # Select appropriate table based on application
    if conductor_application.lower() == "service":
        # Use Table 310.12(A) for dwelling services
        table = tools.tables_data["tables"].get("Table 310.12(A)")
        table_ref = "Table 310.12(A)"
        if not table:
            return "Error: Table 310.12(A) not found"

        # Table 310.12(A) has exact amperage ratings, not ampacity ranges
        # Structure: amperes, copper, aluminum
        material_key = "copper" if conductor_type.lower() == "copper" else "aluminum"

        # Find the exact or next higher amperage rating
        matching_conductor = None
        matching_amperes = None

        for row in table["rows"]:
            amperes_raw = row.get("amperes", "")
            try:
                amperes = int(amperes_raw)
            except (ValueError, TypeError):
                continue

            if amperes >= required_ampacity:
                matching_conductor = row.get(material_key, "").strip()
                matching_amperes = amperes
                break

        if matching_conductor is None:
            return f"Error: No {conductor_type} conductor in Table 310.12(A) meets {required_ampacity}A service rating"

        # Format the size with AWG/kcmil suffix
        if matching_conductor in ["250", "300", "350", "400", "500", "600", "700", "750"]:
            size_formatted = f"{matching_conductor} kcmil"
        else:
            size_formatted = f"{matching_conductor} AWG"

        # Build result
        result = f"DWELLING SERVICE/FEEDER conductor size for {required_ampacity}A: **{size_formatted} {conductor_type}**\n"
        result += f"- Service/Feeder Rating: {matching_amperes}A\n"
        result += f"- Table reference: CEC 2022 Table 310.12(A) (Single-Phase Dwelling Services and Feeders)\n"
        result += f"\nNote: Table 310.12(A) applies when:\n"
        result += f"  (1) No temperature correction or adjustment factors required\n"
        result += f"  (2) Conductors supply entire load of dwelling unit\n"
        result += f"  (3) 120/240V or 120/208Y single-phase system"

        return result

    else:
        # Use Table 310.16 for general conductors (default)
        table_310_16 = tools.tables_data["tables"].get("Table 310.16")
        table_ref = "Table 310.16"
        if not table_310_16:
            return "Error: Table 310.16 not found"

        # Build column key
        temp_suffix = temperature_rating.replace("°C", "c").lower()
        material_prefix = "copper" if conductor_type.lower() == "copper" else "aluminum"
        ampacity_key = f"{material_prefix}_{temp_suffix}"

        # Standard conductor sizes in order from smallest to largest
        # AWG sizes go down (larger number = smaller wire), then kcmil goes up
        size_order = ["18", "16", "14", "12", "10", "8", "6", "4", "3", "2", "1",
                      "1/0", "2/0", "3/0", "4/0",
                      "250", "300", "350", "400", "500", "600", "700", "750",
                      "800", "900", "1000", "1250", "1500", "1750", "2000"]

        # Build a map of size -> ampacity for the specified column
        size_ampacity_map = {}
        for row in table_310_16["rows"]:
            size = row.get("size", "").strip()
            ampacity_raw = row.get(ampacity_key)
            ampacity = safe_get_numeric_value(ampacity_raw, ampacity_key)
            if size and ampacity is not None:
                size_ampacity_map[size] = int(ampacity) if ampacity == int(ampacity) else ampacity

        # Find the SMALLEST conductor that meets or exceeds the required ampacity
        matching_conductor = None
        matching_ampacity = None
        smaller_conductor = None
        smaller_ampacity = None

        for size in size_order:
            if size in size_ampacity_map:
                ampacity = size_ampacity_map[size]
                if ampacity >= required_ampacity:
                    matching_conductor = size
                    matching_ampacity = ampacity
                    break
                else:
                    # Track the last smaller conductor for context
                    smaller_conductor = size
                    smaller_ampacity = ampacity

        if matching_conductor is None:
            return f"Error: No {conductor_type} conductor in Table 310.16 meets {required_ampacity}A at {temperature_rating}"

        # Format the size with AWG/kcmil suffix
        if matching_conductor in ["250", "300", "350", "400", "500", "600", "700", "750", "800", "900", "1000", "1250", "1500", "1750", "2000"]:
            size_formatted = f"{matching_conductor} kcmil"
        else:
            size_formatted = f"{matching_conductor} AWG"

        # Build result with context
        result = f"MINIMUM conductor size for {required_ampacity}A at {temperature_rating}: **{size_formatted} {conductor_type}**\n"
        result += f"- Ampacity: {matching_ampacity}A (meets {required_ampacity}A requirement)\n"
        result += f"- Table reference: CEC 2022 {table_ref}\n"

        # Add context about why this size was selected
        if smaller_conductor:
            if smaller_conductor in ["250", "300", "350", "400", "500", "600", "700", "750", "800", "900", "1000", "1250", "1500", "1750", "2000"]:
                smaller_formatted = f"{smaller_conductor} kcmil"
            else:
                smaller_formatted = f"{smaller_conductor} AWG"
            result += f"\nNote: {smaller_formatted} ({smaller_ampacity}A) is too small - does NOT meet {required_ampacity}A requirement."

        # Add cross-references if 14, 12, or 10 AWG (240.4(D) limitation)
        if matching_conductor in ["14", "12", "10"]:
            result += f"\n\n⚠️ IMPORTANT: Section 240.4(D) limits overcurrent protection for {matching_conductor} AWG conductors."
            result += f"\nYou MUST also call cec_exception_search(base_rule='240.4(D)', context='overcurrent protection {matching_conductor} AWG')"

        return result


if __name__ == "__main__":
    # Test the tools
    tools = CECTableTools()

    print("Testing CEC conductor ampacity lookup:")
    result = cec_lookup_conductor_ampacity("12 AWG", "75°C", "copper")
    print(result)

    print("\nTesting CEC working space lookup:")
    result = cec_lookup_working_space_clearance(120, 1)
    print(result)

    print("\nTesting CEC table search:")
    result = cec_search_tables("grounding")
    print(result)

    print("\nTesting CEC EGC lookup:")
    result = cec_lookup_egc_size(100)
    print(result)

    print("\nTesting CEC GEC lookup:")
    result = cec_lookup_gec_size("2/0", "copper")
    print(result)

    print("\nTesting CEC reverse conductor size lookup (60A at 75°C):")
    result = cec_lookup_conductor_size_for_ampacity(60, "75°C", "copper")
    print(result)

    print("\nTesting CEC reverse conductor size lookup (200A at 75°C aluminum):")
    result = cec_lookup_conductor_size_for_ampacity(200, "75°C", "aluminum")
    print(result)
