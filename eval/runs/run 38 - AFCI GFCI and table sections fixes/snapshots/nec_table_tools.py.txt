"""
NEC Table Lookup Tools
Provides deterministic access to NEC 2023 tables for electrical calculations and specifications
"""
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
import re


# ============================================================================
# GLOBAL UTILITY FUNCTIONS FOR NEC TABLE DATA HANDLING
# ============================================================================

def safe_get_numeric_value(value: Any, field_name: str = "value") -> Optional[float]:
    """
    Safely convert table value to float, handling None and string "None" globally.

    This utility handles the 29+ NEC tables that contain None values for
    not-applicable or out-of-range conditions.

    Args:
        value: Value from table (could be int, float, str, None)
        field_name: Name of field for error messages

    Returns:
        Float value if valid number, None if not applicable

    Examples:
        >>> safe_get_numeric_value(25.5)
        25.5
        >>> safe_get_numeric_value("25.5")
        25.5
        >>> safe_get_numeric_value(None)
        None
        >>> safe_get_numeric_value("None")
        None
    """
    if value is None:
        return None

    # Handle string "None" (some tables may have this)
    if isinstance(value, str) and value.strip().lower() == "none":
        return None

    # Convert to float
    try:
        return float(value)
    except (ValueError, TypeError):
        # If we can't convert, treat as None
        return None


def parse_range_value(range_str: str, test_value: Union[int, float]) -> tuple:
    """
    Parse ANY NEC table range format and test if value matches.

    Handles all non-standard range formats found in 29+ tables:
    - Standard ranges: "11-15", "11–15" (hyphen or en-dash)
    - Lower bounds: "10 or less", "under 10", "not over 10"
    - Upper bounds: "41 and above", "over 100", "61 and over"
    - Through ranges: "Over 3/0 through 350", "Over 600 through 1100"
    - Open-ended: "Over 1100"

    Args:
        range_str: Range string from table
        test_value: Numeric value to test

    Returns:
        Tuple of (matched: bool, range_description: str)

    Examples:
        >>> parse_range_value("11–15", 12)
        (True, "11–15")
        >>> parse_range_value("10 or less", 8)
        (True, "10 or less")
        >>> parse_range_value("41 and above", 50)
        (True, "41 and above")
        >>> parse_range_value("Over 3/0 through 350", 250)
        (True, "Over 3/0 through 350")
    """
    range_str = range_str.strip()

    # Pattern 1: "X or less", "X or under", "not over X"
    lower_bound_patterns = [
        r'(\d+(?:\.\d+)?)\s+or\s+less',
        r'(\d+(?:\.\d+)?)\s+or\s+under',
        r'not\s+over\s+(\d+(?:\.\d+)?)',
        r'under\s+(\d+(?:\.\d+)?)'
    ]

    for pattern in lower_bound_patterns:
        match = re.search(pattern, range_str, re.IGNORECASE)
        if match:
            max_val = float(match.group(1))
            return (test_value <= max_val, range_str)

    # Pattern 2a: "X and above", "X and over" (inclusive)
    inclusive_upper_patterns = [
        r'(\d+(?:\.\d+)?)\s+and\s+above',
        r'(\d+(?:\.\d+)?)\s+and\s+over'
    ]

    for pattern in inclusive_upper_patterns:
        match = re.search(pattern, range_str, re.IGNORECASE)
        if match:
            min_val = float(match.group(1))
            return (test_value >= min_val, range_str)

    # Pattern 2b: "over X" (exclusive, not "over X through Y")
    over_match = re.search(r'over\s+(\d+(?:\.\d+)?)\s*$', range_str, re.IGNORECASE)
    if over_match:
        min_val = float(over_match.group(1))
        return (test_value > min_val, range_str)

    # Pattern 3: "Over X through Y"
    through_match = re.search(r'over\s+(\d+(?:\.\d+)?)\s+through\s+(\d+(?:\.\d+)?)', range_str, re.IGNORECASE)
    if through_match:
        min_val = float(through_match.group(1))
        max_val = float(through_match.group(2))
        return (min_val < test_value <= max_val, range_str)

    # Pattern 4: Standard range "X-Y" or "X–Y" (hyphen or en-dash)
    # Handle both en-dash (–) and hyphen (-)
    if '–' in range_str or '-' in range_str:
        separator = '–' if '–' in range_str else '-'
        parts = range_str.split(separator)
        if len(parts) == 2:
            try:
                low = float(parts[0].strip())
                high = float(parts[1].strip())
                return (low <= test_value <= high, range_str)
            except ValueError:
                # Not numeric, fall through
                pass

    # No pattern matched
    return (False, range_str)


def normalize_separator(text: str) -> str:
    """
    Normalize all separator characters to standard hyphen.

    Handles character encoding variations:
    - En-dash (–, Unicode U+2013)
    - Em-dash (—, Unicode U+2014)
    - Hyphen (-, ASCII)

    Args:
        text: Text containing separators

    Returns:
        Text with all separators normalized to hyphen

    Examples:
        >>> normalize_separator("11–15")
        "11-15"
        >>> normalize_separator("11—15")
        "11-15"
    """
    # Replace en-dash and em-dash with hyphen
    text = text.replace('–', '-')  # En-dash U+2013
    text = text.replace('—', '-')  # Em-dash U+2014
    return text


class NECTableTools:
    """Class to handle NEC table lookups and calculations"""

    def __init__(self, tables_file_path: str = None):
        """Initialize with NEC tables data"""
        if tables_file_path is None:
            # Default path relative to this file
            current_dir = Path(__file__).parent
            tables_file_path = current_dir.parent / "data" / "NEC_2023" / "nec_tables_unified.json"

        self.tables_file = Path(tables_file_path)
        self.tables_data = self._load_tables()

    def _load_tables(self) -> Dict[str, Any]:
        """Load NEC tables from JSON file"""
        try:
            with open(self.tables_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"Loaded {data['metadata']['total_tables']} NEC tables")
            return data
        except Exception as e:
            print(f"Error loading NEC tables: {e}")
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

            # Match "See X.X(Y)" patterns (common in NEC)
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

        Examples:
            >>> _normalize_table_id("310.16")
            "Table 310.16"
            >>> _normalize_table_id("Table 310.16")
            "Table 310.16"
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
            return {
                "table_id": table["table_id"],
                "caption": table["caption"],
                "description": table["description"],
                "section": table["section"],
                "keywords": table["keywords"]
            }
        return None

    def lookup_conductor_ampacity(self, conductor_size: str, temperature_rating: str = "75°C",
                                 conductor_type: str = "copper") -> Dict[str, Any]:
        """
        Look up conductor ampacity from NEC Table 310.16

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

                    return {
                        "ampacity": int(ampacity) if ampacity == int(ampacity) else ampacity,
                        "conductor_size": conductor_size,
                        "temperature_rating": temperature_rating,
                        "conductor_type": conductor_type,
                        "table_reference": "NEC 2023 Table 310.16",
                        "description": table_310_16["description"],
                        "applicable_notes": notes_info["applicable_notes"],
                        "cross_references": notes_info["cross_references"]
                    }

        return {"error": f"Conductor size {conductor_size} ({size_normalized}) not found in Table 310.16 or no ampacity for {conductor_type} at {temperature_rating}"}

    def lookup_working_space(self, voltage_to_ground: int, condition: int) -> Dict[str, Any]:
        """
        Look up working space requirements from Table 110.26(A)(1)

        Args:
            voltage_to_ground: Voltage in volts (e.g., 120, 277, 480)
            condition: Condition number 1, 2, or 3

        Returns:
            Dict with working space depth, table reference, and applicable footnotes/cross-references
        """
        table_110_26 = self.tables_data["tables"].get("Table 110.26(A)(1)")
        if not table_110_26:
            return {"error": "Table 110.26(A)(1) not found"}

        # Find appropriate voltage range
        for row in table_110_26["rows"]:
            voltage_range = row.get("voltage_range", "")

            # Use global utility to parse ANY range format
            # Handles standard ranges with hyphen/en-dash and special formats
            matches, _ = parse_range_value(voltage_range, voltage_to_ground)

            if matches:
                condition_key = f"condition_{condition}"
                clearance = row.get(condition_key)

                # Handle None values (not-applicable conditions)
                if clearance is None or (isinstance(clearance, str) and clearance.strip().lower() == "none"):
                    return {"error": f"Working space clearance is not available for voltage range {voltage_range}, condition {condition}"}

                # Get applicable notes and cross-references for this row
                notes_info = self._get_applicable_notes(table_110_26, row)

                # Also include condition descriptions from table notes if available
                condition_notes = []
                for note in table_110_26.get("notes", []):
                    # Check for condition descriptions (e.g., "Condition 1", "Condition 2")
                    condition_label = note.get("condition", "")
                    if condition_label == f"Condition {condition}":
                        condition_notes.append(note.get("text", ""))

                return {
                    "working_space_depth": clearance,
                    "voltage_to_ground": voltage_to_ground,
                    "condition": condition,
                    "condition_description": condition_notes[0] if condition_notes else "",
                    "voltage_range": voltage_range,
                    "table_reference": "NEC 2023 Table 110.26(A)(1)",
                    "description": table_110_26["description"],
                    "applicable_notes": notes_info["applicable_notes"] + condition_notes,
                    "cross_references": notes_info["cross_references"]
                }

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
                matches.append({
                    "table_id": table_id,
                    "caption": table_data.get("caption", ""),
                    "section": table_data.get("section", ""),
                    "keywords": table_data.get("keywords", [])[:5]  # First 5 keywords
                })

                if len(matches) >= limit:
                    break

        return matches

    def get_table_data(self, table_id: str, row_filter: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Get complete table data with optional row filtering

        Args:
            table_id: NEC table identifier
            row_filter: Optional dict to filter rows (e.g., {"voltage_range": "151-600"})

        Returns:
            Complete table data or filtered subset
        """
        # Normalize table ID to standard format
        table_id = self._normalize_table_id(table_id)

        # Tier 1: Try exact match first (fastest)
        table = self.tables_data["tables"].get(table_id)

        # Tier 2: If no exact match, try fuzzy/prefix matching
        # Example: "Table 310.12" matches "Table 310.12(A)"
        if not table:
            matching_tables = [
                tid for tid in self.tables_data["tables"].keys()
                if tid.startswith(table_id)
            ]

            if matching_tables:
                # Found prefix matches - use first one alphabetically
                # But include info about all matches in description
                matched_id = sorted(matching_tables)[0]
                table = self.tables_data["tables"][matched_id]

                # Add note about other matches if multiple found
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
            # Handles standard ranges (11-15, 11–15) and special formats (10 or less, 41 and above)
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

                # Get the full table for notes
                full_table = self.tables_data["tables"].get(table_id, {})
                notes_info = self._get_applicable_notes(full_table, row)

                return {
                    "success": True,
                    "table_id": table_id,
                    "correction_factor": correction_factor,
                    "ambient_temp": ambient_temp,
                    "temp_range": temp_range,
                    "conductor_rating": conductor_temp_rating,
                    "base_temp": base_temp,
                    "applicable_notes": notes_info["applicable_notes"],
                    "cross_references": notes_info["cross_references"]
                }

        return {"error": f"No temperature correction found for {ambient_temp}°C"}

    def lookup_bundling_adjustment(self, num_conductors: int) -> Dict[str, Any]:
        """
        Look up bundling adjustment factor from NEC 2023 Table 310.15(C)(1).

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
                "code_reference": "NEC 2023"
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
                    "code_reference": "NEC 2023"
                }

                return result

        return {"error": f"No bundling adjustment found for {num_conductors} conductors"}

    def lookup_egc_size(self, overcurrent_device_amperes: int) -> Dict[str, Any]:
        """
        Look up equipment grounding conductor size from NEC 2023 Table 250.122

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
                    "table_reference": "NEC 2023 Table 250.122",
                    "description": table_250_122.get("description", "")
                }
                return result

        return {"error": f"Overcurrent device rating {overcurrent_device_amperes}A exceeds Table 250.122 maximum"}

    def lookup_gec_size(self, service_conductor_size: str, conductor_type: str = "copper") -> Dict[str, Any]:
        """
        Look up grounding electrode conductor size from NEC 2023 Table 250.66

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

        # Convert to numeric for range comparisons (kcmil sizes only)
        size_numeric = None
        try:
            size_numeric = float(size_normalized.replace("/", ""))
            if "/" in size_normalized:
                size_numeric = None
        except (ValueError, AttributeError):
            size_numeric = None

        # Determine which column to search based on conductor type
        search_column = "largest_conductor_copper" if conductor_type.lower() == "copper" else "largest_conductor_aluminum"

        for row in table_250_66["rows"]:
            row_value = row.get(search_column, "")

            # Strategy 1: Check for exact string match
            if size_normalized in row_value or row_value == size_normalized:
                result = {
                    "service_conductor_size": service_conductor_size,
                    "conductor_type": conductor_type,
                    "service_conductor_range": row_value,
                    "gec_copper": row.get("grounding_conductor_copper"),
                    "gec_aluminum": row.get("grounding_conductor_aluminum"),
                    "table_reference": "NEC 2023 Table 250.66",
                    "description": table_250_66.get("description", "")
                }
                return result

            # Strategy 2: For numeric values (kcmil sizes), use range parsing
            if size_numeric is not None:
                matches, _ = parse_range_value(row_value, size_numeric)
                if matches:
                    result = {
                        "service_conductor_size": service_conductor_size,
                        "conductor_type": conductor_type,
                        "service_conductor_range": row_value,
                        "gec_copper": row.get("grounding_conductor_copper"),
                        "gec_aluminum": row.get("grounding_conductor_aluminum"),
                        "table_reference": "NEC 2023 Table 250.66",
                        "description": table_250_66.get("description", "")
                    }
                    return result

        return {"error": f"Service conductor size {service_conductor_size} not found in Table 250.66"}

    def calculate_derated_ampacity(
        self,
        conductor_size: str,
        insulation_type: str,
        ambient_temperature: float = 30.0,
        num_conductors: int = 3,
        conductor_type: str = "copper"
    ) -> Dict[str, Any]:
        """
        Complete ampacity decision tree - calculates derated ampacity with all factors applied.

        This chains:
        1. Insulation type → temperature rating lookup
        2. Base ampacity from correct Table 310.16 column
        3. Temperature correction factor (if ambient ≠ 30°C)
        4. Bundling adjustment factor (if > 3 conductors)
        5. Final calculation: Base × Temp Factor × Bundling Factor

        Args:
            conductor_size: Wire size (e.g., "12 AWG", "2/0 AWG", "250 kcmil")
            insulation_type: Conductor insulation (THHN, TW, THWN, XHHW, etc.)
            ambient_temperature: Ambient temperature in °C (default: 30.0)
            num_conductors: Number of current-carrying conductors (default: 3)
            conductor_type: "copper" or "aluminum"

        Returns:
            Dict with all intermediate values and final derated ampacity
        """
        # Step 1: Map insulation type to temperature rating
        INSULATION_TEMP_RATINGS = {
            # 90°C insulations
            "THHN": "90°C", "THWN-2": "90°C", "XHHW-2": "90°C",
            "RHH": "90°C", "RHW-2": "90°C", "USE-2": "90°C",
            "SA": "90°C", "SIS": "90°C", "FEP": "90°C", "FEPB": "90°C",
            "MI": "90°C", "XHH": "90°C", "ZW-2": "90°C",
            # 75°C insulations
            "THW": "75°C", "THWN": "75°C", "XHHW": "75°C",
            "RHW": "75°C", "USE": "75°C", "ZW": "75°C",
            "TBS": "75°C", "SFF-1": "75°C", "SFF-2": "75°C",
            # 60°C insulations
            "TW": "60°C", "UF": "60°C", "TF": "60°C", "TFF": "60°C",
            "MTW": "60°C", "TFFN": "60°C",
        }

        insulation_upper = insulation_type.upper().strip()
        temperature_rating = INSULATION_TEMP_RATINGS.get(insulation_upper)

        if not temperature_rating:
            return {
                "error": f"Unknown insulation type: {insulation_type}. "
                         f"Known types: {', '.join(sorted(INSULATION_TEMP_RATINGS.keys()))}"
            }

        # Step 2: Get base ampacity from Table 310.16
        base_result = self.lookup_conductor_ampacity(
            conductor_size, temperature_rating, conductor_type
        )

        if "error" in base_result:
            return base_result

        base_ampacity = base_result["ampacity"]

        # Step 3: Get temperature correction factor (only if ambient ≠ 30°C)
        temp_factor = 1.0
        temp_result = None
        if ambient_temperature != 30.0:
            temp_result = self.lookup_temperature_correction(
                ambient_temperature, temperature_rating, "30°C"
            )
            if "error" in temp_result:
                return temp_result
            temp_factor = temp_result["correction_factor"]

        # Step 4: Get bundling adjustment factor (only if > 3 conductors)
        bundling_factor = 1.0
        bundling_result = None
        if num_conductors > 3:
            bundling_result = self.lookup_bundling_adjustment(num_conductors)
            if "error" in bundling_result:
                return bundling_result
            bundling_factor = bundling_result["adjustment_factor"]

        # Step 5: Calculate final derated ampacity
        derated_ampacity = base_ampacity * temp_factor * bundling_factor
        derated_ampacity_rounded = round(derated_ampacity, 2)

        # Build comprehensive result
        result = {
            "success": True,
            "conductor_size": conductor_size,
            "conductor_type": conductor_type,
            "insulation_type": insulation_upper,
            "insulation_temperature_rating": temperature_rating,

            # Step-by-step values
            "step_1_base_ampacity": base_ampacity,
            "step_1_table": "Table 310.16",
            "step_1_column": f"{conductor_type}_{temperature_rating}",

            "step_2_ambient_temperature": ambient_temperature,
            "step_2_temp_correction_factor": temp_factor,
            "step_2_applied": ambient_temperature != 30.0,

            "step_3_num_conductors": num_conductors,
            "step_3_bundling_factor": bundling_factor,
            "step_3_applied": num_conductors > 3,

            # Final result
            "final_derated_ampacity": derated_ampacity_rounded,
            "calculation": f"{base_ampacity}A × {temp_factor} × {bundling_factor} = {derated_ampacity_rounded}A",

            # References
            "code_reference": "NEC 2023",
            "tables_used": ["Table 310.16"],
            "cross_references": base_result.get("cross_references", []),
            "applicable_notes": base_result.get("applicable_notes", [])
        }

        # Add table references for adjustments if applied
        if temp_result:
            result["tables_used"].append(temp_result.get("table_id", "Table 310.15(B)(1)"))
        if bundling_result:
            result["tables_used"].append(bundling_result.get("table_id", "Table 310.15(C)(1)"))

        # Add limiting rule reminder for small conductors
        if conductor_size.upper().replace(" AWG", "").strip() in ["14", "12", "10"]:
            result["limiting_rule_warning"] = (
                f"⚠️ 240.4(D) limits overcurrent protection for {conductor_size}. "
                "Check that OCP device does not exceed limits."
            )

        return result

    def lookup_conduit_fill(self, conduit_type: str, conduit_size: str,
                           conductor_type: str, conductor_size: str,
                           num_conductors: int = 3) -> Dict[str, Any]:
        """
        Look up conduit fill data from NEC 2023 Chapter 9 tables.

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
            "table_reference": "NEC 2023 Chapter 9 Tables 4 & 5",
            "source": "NEC 2023 Chapter 9"
        }

    def lookup_conductor_resistance(self, conductor_size: str, conductor_type: str = "copper") -> Dict[str, Any]:
        """
        Look up conductor DC resistance from NEC 2023 Chapter 9 Table 8.

        Used for voltage drop calculations per 210.19(A)(1) Informational Note No. 4.
        Returns resistance in ohms per 1000 feet at 75°C (167°F).

        Args:
            conductor_size: Wire size (e.g., "12", "12 AWG", "4/0", "4/0 AWG", "250", "250 kcmil")
            conductor_type: "copper" or "aluminum" (default: "copper")

        Returns:
            Dict with resistance value, units, and reference information
        """
        # Get Table 8 data
        table8 = self.get_table_data("Chapter 9 Table 8")
        if "error" in table8:
            return {"error": f"Chapter 9 Table 8 not found: {table8['error']}"}

        # Normalize conductor size - remove "AWG" and "kcmil" suffixes, standardize format
        size_normalized = conductor_size.upper().replace(" AWG", "").replace("AWG", "").replace(" KCMIL", "").replace("KCMIL", "").strip()

        # Normalize conductor type
        cond_type = conductor_type.lower().strip()
        if cond_type not in ["copper", "aluminum"]:
            return {"error": f"Invalid conductor type: {conductor_type}. Must be 'copper' or 'aluminum'."}

        # Determine resistance key based on conductor type
        resistance_key = "copper_resistance" if cond_type == "copper" else "aluminum_resistance"

        # Search for matching row - prefer stranded for sizes 8 AWG and larger
        rows = table8.get("rows", [])
        matching_rows = [r for r in rows if r.get("size", "").upper() == size_normalized]

        if not matching_rows:
            # Try alternate formats for /0 sizes
            if "/" in size_normalized:
                # Already has /0 format
                pass
            elif size_normalized in ["10", "20", "30", "40"]:
                # Try adding /0 format (e.g., "10" -> "1/0")
                alt_size = size_normalized[0] + "/0" if len(size_normalized) == 2 else size_normalized
                matching_rows = [r for r in rows if r.get("size", "").upper() == alt_size]

            if not matching_rows:
                available_sizes = sorted(set(r.get("size", "") for r in rows))
                return {
                    "error": f"Conductor size '{conductor_size}' not found in Chapter 9 Table 8.",
                    "available_sizes": available_sizes
                }

        # For sizes with both solid and stranded, prefer stranded (more common for installation)
        if len(matching_rows) > 1:
            stranded_rows = [r for r in matching_rows if r.get("stranding", "").lower() == "stranded"]
            if stranded_rows:
                row = stranded_rows[0]
            else:
                row = matching_rows[0]
        else:
            row = matching_rows[0]

        resistance = row.get(resistance_key)
        if resistance is None:
            return {"error": f"No {cond_type} resistance value for size {conductor_size}"}

        # Format the size for display
        size_display = row.get("size", size_normalized)
        if size_display in ["18", "16", "14", "12", "10", "8", "6", "4", "3", "2", "1"]:
            size_display = f"{size_display} AWG"
        elif "/" in size_display:
            size_display = f"{size_display} AWG"
        else:
            size_display = f"{size_display} kcmil"

        return {
            "resistance": resistance,
            "units": "ohms per 1000 feet",
            "temperature": "75°C (167°F)",
            "conductor_size": size_display,
            "conductor_type": cond_type.capitalize(),
            "stranding": row.get("stranding", "Unknown"),
            "table_id": "Chapter 9 Table 8",
            "code_reference": "NEC 2023 Chapter 9 Table 8",
            "notes": [
                "Use for voltage drop calculations per 210.19(A)(1) Informational Note No. 4.",
                "Formula: VD = (2 × L × R × I) / 1000, where L = one-way length in feet, R = resistance per 1000 ft, I = current.",
                "Branch circuits: 3% max recommended. Branch + feeder combined: 5% max recommended."
            ]
        }


# Function definitions for Gemini function calling
def lookup_conductor_ampacity(conductor_size: str, temperature_rating: str = "75°C",
                             conductor_type: str = "copper") -> str:
    """
    Look up conductor ampacity from NEC Table 310.16

    Args:
        conductor_size: Wire size like "12 AWG", "2/0 AWG", "250 kcmil"
        temperature_rating: Temperature rating - "60°C", "75°C", or "90°C"
        conductor_type: Conductor material - "copper" or "aluminum"

    Returns:
        String with ampacity information, NEC reference, and cross-references
    """
    tools = NECTableTools()
    result = tools.lookup_conductor_ampacity(conductor_size, temperature_rating, conductor_type)

    if "error" in result:
        return f"Error: {result['error']}"

    output = f"Conductor ampacity for {result['conductor_size']} {result['conductor_type']} at {result['temperature_rating']}: {result['ampacity']} amperes per {result['table_reference']}. {result['description']}"

    # Include applicable notes if present
    if result.get("applicable_notes"):
        output += f"\n\nApplicable Notes: {' '.join(result['applicable_notes'])}"

    # Include cross-references if present
    if result.get("cross_references"):
        output += f"\n\nCross-References (MUST be consulted): {', '.join(result['cross_references'])}"

    return output


def lookup_working_space_clearance(voltage_to_ground: int, condition: int) -> str:
    """
    Look up required working space clearances from NEC Table 110.26(A)(1)

    Args:
        voltage_to_ground: Nominal voltage to ground in volts (e.g. 120, 277, 480)
        condition: Working space condition number (1, 2, or 3)

    Returns:
        String with working space requirements, NEC reference, and cross-references
    """
    tools = NECTableTools()
    result = tools.lookup_working_space(voltage_to_ground, condition)

    if "error" in result:
        return f"Error: {result['error']}"

    output = f"Working space requirement for {result['voltage_to_ground']}V (condition {result['condition']}): {result['working_space_depth']} per {result['table_reference']}. Voltage range: {result['voltage_range']}V."

    # Include condition description if available
    if result.get("condition_description"):
        output += f"\n\nCondition {result['condition']} Definition: {result['condition_description']}"

    # Include applicable notes if present
    if result.get("applicable_notes"):
        output += f"\n\nApplicable Notes: {' '.join(result['applicable_notes'])}"

    # Include cross-references if present
    if result.get("cross_references"):
        output += f"\n\nCross-References (MUST be consulted): {', '.join(result['cross_references'])}"

    return output


def search_nec_tables(keyword: str, limit: int = 5) -> str:
    """
    Search NEC tables by keyword to find relevant tables

    Args:
        keyword: Search term (e.g. "ampacity", "clearance", "AFCI")
        limit: Maximum number of results to return

    Returns:
        String with list of matching tables and their purposes
    """
    tools = NECTableTools()
    results = tools.search_tables_by_keyword(keyword, limit)

    if not results:
        return f"No NEC tables found matching keyword: {keyword}"

    output = [f"NEC tables related to '{keyword}':"]
    for table in results:
        output.append(f"- {table['table_id']} ({table['section']}): {table['caption']}")
        if table['keywords']:
            output.append(f"  Keywords: {', '.join(table['keywords'])}")

    return "\n".join(output)


def get_table_information(table_id: str) -> str:
    """
    Get detailed information about a specific NEC table

    Args:
        table_id: NEC table identifier (e.g. "Table 310.16", "Table 110.26(A)(1)")

    Returns:
        String with table description and purpose
    """
    tools = NECTableTools()
    result = tools.get_table_info(table_id)

    if not result:
        return f"Table {table_id} not found in NEC database"

    return f"{result['table_id']} - {result['caption']}\nSection: {result['section']}\nDescription: {result['description']}\nKeywords: {', '.join(result['keywords'][:10])}"


def nec_lookup_conductor_size_for_ampacity(
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
        nec_lookup_conductor_size_for_ampacity(60, "75°C", "copper", "general")
        → Returns "6 AWG" (which has 65A at 75°C per Table 310.16)

        nec_lookup_conductor_size_for_ampacity(150, "75°C", "aluminum", "service")
        → Returns "2/0 AWG" (per Table 310.12(A) for dwelling services)
    """
    tools = NECTableTools()

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
        result += f"- Table reference: NEC 2023 Table 310.12(A) (Single-Phase Dwelling Services and Feeders)\n"
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
        result += f"- Table reference: NEC 2023 {table_ref}\n"

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
            result += f"\nYou MUST also call nec_exception_search(base_rule='240.4(D)', context='overcurrent protection {matching_conductor} AWG')"

        return result


if __name__ == "__main__":
    # Test the tools
    tools = NECTableTools()

    print("Testing conductor ampacity lookup:")
    result = lookup_conductor_ampacity("12 AWG", "75°C", "copper")
    print(result)

    print("\nTesting working space lookup:")
    result = lookup_working_space_clearance(120, 1)
    print(result)

    print("\nTesting table search:")
    result = search_nec_tables("ampacity")
    print(result)

    print("\nTesting NEC reverse conductor size lookup (60A at 75°C):")
    result = nec_lookup_conductor_size_for_ampacity(60, "75°C", "copper")
    print(result)

    print("\nTesting NEC reverse conductor size lookup (200A at 75°C aluminum):")
    result = nec_lookup_conductor_size_for_ampacity(200, "75°C", "aluminum")
    print(result)
