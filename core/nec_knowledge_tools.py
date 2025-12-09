"""
NEC Knowledge Tools - 3-Tool Architecture
Provides deterministic NEC lookups for the unified agent

Tools:
1. nec_search - General rule and section search
2. nec_exception_search - Targeted exception finding
3. nec_table_lookup - Unified table value lookups
"""
import json
from typing import Dict, List, Any, Optional
from pathlib import Path

# Import our components
from core.opensearch_hybrid_client import get_hybrid_client
from core.nec_table_tools import NECTableTools


class NECKnowledgeTools:
    """
    Knowledge tool system for NEC agent v2
    Combines hybrid search with deterministic table lookups
    """

    def __init__(self):
        """Initialize unified tools with search and table components"""
        self.search_client = get_hybrid_client()
        self.table_tools = NECTableTools()

        # Check availability
        self.search_available = self.search_client.is_available
        print(f"Search available: {self.search_available}")
        print(f"Tables loaded: {self.table_tools.tables_data['metadata']['total_tables']}")

    def nec_search(self,
                   query: str,
                   article_filter: Optional[str] = None,
                   limit: int = 5) -> str:
        """
        Search NEC 2023 for rules, sections, and requirements

        This tool performs hybrid search (BM25 + vector) to find relevant
        NEC content based on your query. Use this for finding:
        - General NEC requirements
        - Section text and interpretations
        - Rule applicability
        - Code requirements for specific scenarios

        Args:
            query: Search query describing what you're looking for
            article_filter: Optional article number to filter results (e.g., "310", "240")
            limit: Maximum number of results to return (default: 5)

        Returns:
            Formatted string with NEC sections and their content
        """
        # Build filters
        filters = {}
        if article_filter:
            filters["article"] = article_filter

        # Execute hybrid search
        results = self.search_client.hybrid_search(
            query=query,
            filters=filters if filters else None,
            limit=limit
        )

        # Handle errors
        if not results:
            return f"No NEC content found for query: {query}"

        if len(results) == 1 and "error" in results[0]:
            return f"Search error: {results[0]['error']}"

        # Format results
        output = [f"NEC 2023 search results for: '{query}'"]
        if article_filter:
            output.append(f"(Filtered to Article {article_filter})")

        output.append("")

        for i, result in enumerate(results, 1):
            section = result.get('section', 'Unknown')
            article = result.get('article', '')
            chapter = result.get('chapter', '')
            content = result.get('content', '')
            score = result.get('score', 0)

            # Create citation
            if section and section != 'Unknown':
                citation = f"NEC 2023 Section {section}"
            elif article:
                citation = f"NEC 2023 Article {article}"
            else:
                citation = "NEC 2023"

            output.append(f"Result {i} [{citation}] (relevance: {score:.2f})")
            output.append(f"{content}")
            output.append("")

        return "\n".join(output)

    def nec_exception_search(self,
                            base_rule: str,
                            context: Optional[str] = None,
                            limit: int = 5) -> str:
        """
        Search for NEC exceptions related to a base rule

        This tool specifically searches for exceptions, overrides, and
        alternative methods that may modify or supersede a base NEC rule.
        Use this whenever you:
        - Find a base rule and need to check for exceptions
        - Need to verify if alternative methods are permitted
        - Want to find "shall not apply" or "not required" conditions

        Args:
            base_rule: The base NEC rule/section (e.g., "310.16", "240.4", "250.32")
            context: Optional context to narrow search (e.g., "small conductors", "AFCI")
            limit: Maximum number of results (default: 5)

        Returns:
            Formatted string with exception information
        """
        # Execute exception search
        results = self.search_client.exception_search(
            base_rule=base_rule,
            context=context,
            limit=limit
        )

        # Handle errors
        if results is None:
            return f"Search error: Unable to search for exceptions to {base_rule} (connection issue or search failure)"

        if not results:
            return f"No exceptions found for base rule: {base_rule}"

        if len(results) == 1 and "error" in results[0]:
            return f"Exception search error: {results[0]['error']}"

        # Format results
        output = [f"NEC 2023 exceptions for base rule: {base_rule}"]
        if context:
            output.append(f"Context: {context}")
        output.append("")

        exception_found = False
        for i, result in enumerate(results, 1):
            content = result.get('content', '')
            section = result.get('section', 'Unknown')
            score = result.get('score', 0)

            # Check if this actually contains exception language
            exception_keywords = ['exception', 'Exception', 'shall not apply', 'not required',
                                'alternative', 'in lieu of', 'permitted']

            has_exception = any(keyword in content for keyword in exception_keywords)

            if has_exception:
                exception_found = True
                output.append(f"Exception {i} [NEC 2023 Section {section}] (relevance: {score:.2f})")
                output.append(f"{content}")
                output.append("")

        if not exception_found:
            output.append(f"No explicit exceptions found for {base_rule}.")
            output.append("The base rule likely applies without modification.")

        return "\n".join(output)

    def nec_table_lookup(self,
                        table_id: str,
                        lookup_params: Dict[str, Any]) -> str:
        """
        Look up values from NEC tables

        This tool provides deterministic lookups from NEC 2023 tables.
        Use this for any numeric values, factors, or requirements from tables.

        Supported lookups:
        - Conductor ampacity (Table 310.16)
        - Working space clearances (Table 110.26(A)(1))
        - Temperature correction factors (Table 310.15(B)(1))
        - Conduit fill (Chapter 9 tables)
        - And 143 more NEC tables

        Args:
            table_id: NEC table identifier (e.g., "Table 310.16", "Table 110.26(A)(1)")
            lookup_params: Parameters for the lookup as a dict. Examples:
                For ampacity: {"conductor_size": "12 AWG", "temperature_rating": "75°C",
                               "conductor_type": "copper"}
                For working space: {"voltage_to_ground": 120, "condition": 1}
                For general table: {"row_filter": {"voltage_range": "151-600"}}

        Returns:
            Formatted string with table value and NEC reference
        """
        # Normalize table_id
        table_id = table_id.strip()
        if not table_id.startswith("Table "):
            table_id = f"Table {table_id}"

        # Handle Table 315.60 generic request
        if table_id == "Table 315.60":
            return ("Error: Table 315.60 has 21 variants. Use search_nec_tables with keywords like 'copper triplexed air' "
                   "or 'aluminum three-conductor conduit' to find the correct variant (Table 315.60(C)(1) through (C)(20) "
                   "for ampacity, or (D)(4) for temperature correction).")

        # Handle specific table lookups with specialized methods
        if table_id == "Table 310.16":
            # Conductor ampacity lookup
            conductor_size = lookup_params.get("conductor_size")
            temperature_rating = lookup_params.get("temperature_rating", "75°C")
            conductor_type = lookup_params.get("conductor_type", "copper")

            if not conductor_size:
                return "Error: conductor_size is required for Table 310.16 lookup"

            result = self.table_tools.lookup_conductor_ampacity(
                conductor_size=conductor_size,
                temperature_rating=temperature_rating,
                conductor_type=conductor_type
            )

            if "error" in result:
                return f"Table 310.16 lookup error: {result['error']}"

            return (f"Conductor Ampacity Lookup [NEC 2023 Table 310.16]\n"
                   f"Size: {result['conductor_size']}\n"
                   f"Material: {result['conductor_type'].title()}\n"
                   f"Temperature Rating: {result['temperature_rating']}\n"
                   f"Ampacity: {result['ampacity']} amperes\n\n"
                   f"Reference: {result['table_reference']}\n"
                   f"Description: {result['description']}")

        elif table_id == "Table 110.26(A)(1)":
            # Working space lookup
            voltage_to_ground = lookup_params.get("voltage_to_ground")
            condition = lookup_params.get("condition")

            if voltage_to_ground is None or condition is None:
                return "Error: voltage_to_ground and condition are required for Table 110.26(A)(1)"

            result = self.table_tools.lookup_working_space(
                voltage_to_ground=int(voltage_to_ground),
                condition=int(condition)
            )

            if "error" in result:
                return f"Table 110.26(A)(1) lookup error: {result['error']}"

            return (f"Working Space Clearance [NEC 2023 Table 110.26(A)(1)]\n"
                   f"Voltage to Ground: {result['voltage_to_ground']}V\n"
                   f"Condition: {result['condition']}\n"
                   f"Required Clearance: {result['working_space_depth']}\n"
                   f"Voltage Range: {result['voltage_range']}V\n\n"
                   f"Reference: {result['table_reference']}\n"
                   f"Description: {result['description']}")

        elif "310.15(B)(1)" in table_id:
            # Temperature correction - handle both shorthand and full table names
            # Catch row_filter misuse and provide helpful guidance
            if "row_filter" in lookup_params:
                return ("Error: Table 310.15(B)(1) temperature correction lookups require specific parameters, not row_filter.\n\n"
                       "Required parameters:\n"
                       "  - ambient_temp: Ambient temperature in °C (e.g., 43)\n"
                       "  - conductor_temp_rating: Conductor rating - '60°C', '75°C', or '90°C'\n"
                       "  - base_temp (optional): '30°C' for Tables 310.16/310.17, '40°C' for Tables 310.18-310.21 (default: '30°C')\n\n"
                       f"Example: nec_table_lookup('{table_id}', ambient_temp=43, conductor_temp_rating='60°C')")

            ambient_temp = lookup_params.get("ambient_temp") or lookup_params.get("temperature")
            conductor_rating = lookup_params.get("conductor_temp_rating") or lookup_params.get("temperature_rating")

            # Auto-detect base_temp from table_id, or use parameter, or default to 30°C
            if table_id == "Table 310.15(B)(1)(1)":
                base_temp = "30°C"
            elif table_id == "Table 310.15(B)(1)(2)":
                base_temp = "40°C"
            else:
                base_temp = lookup_params.get("base_temp", "30°C")

            if ambient_temp is None or conductor_rating is None:
                return ("Error: Table 310.15(B)(1) requires ambient_temp and conductor_temp_rating parameters.\n\n"
                       f"Example: nec_table_lookup('{table_id}', ambient_temp=43, conductor_temp_rating='60°C')")

            result = self.table_tools.lookup_temperature_correction(
                ambient_temp=float(ambient_temp),
                conductor_temp_rating=conductor_rating,
                base_temp=base_temp
            )

            if "error" in result:
                return f"Temperature correction lookup error: {result['error']}"

            return (f"Temperature Correction Factor [NEC 2023 {result['table_id']}]\n"
                   f"Ambient Temperature: {result['ambient_temp']}°C (range: {result['temp_range']}°C)\n"
                   f"Conductor Rating: {result['conductor_rating']}\n"
                   f"Base Temperature: {result['base_temp']}\n"
                   f"Correction Factor: {result['correction_factor']}\n\n"
                   f"Reference: {result['table_id']}\n"
                   f"Description: Temperature correction factor for ampacity adjustment based on ambient temperature")

        else:
            # General table lookup
            row_filter = lookup_params.get("row_filter")
            result = self.table_tools.get_table_data(table_id, row_filter)

            if "error" in result:
                return f"Table lookup error: {result['error']}"

            # Format general table result
            output = [f"Table Lookup [NEC 2023 {result['table_id']}]"]
            output.append(f"Caption: {result['caption']}")
            output.append(f"Section: {result['section']}")
            output.append(f"Description: {result['description']}")
            output.append("")

            if result.get("rows"):
                output.append(f"Rows returned: {len(result['rows'])}")
                if len(result['rows']) <= 10:
                    output.append(json.dumps(result['rows'], indent=2))
                else:
                    output.append(f"(Showing first 10 of {len(result['rows'])} rows)")
                    output.append(json.dumps(result['rows'][:10], indent=2))

            return "\n".join(output)


# Singleton instance
_tools_instance = None

def get_knowledge_tools() -> NECKnowledgeTools:
    """Get or create singleton NEC knowledge tools instance"""
    global _tools_instance
    if _tools_instance is None:
        _tools_instance = NECKnowledgeTools()
    return _tools_instance


# Standalone function wrappers for Gemini function calling
def nec_search(query: str, article_filter: Optional[str] = None, limit: int = 5) -> str:
    """
    Search NEC 2023 for rules, sections, and requirements

    Args:
        query: What you're searching for
        article_filter: Optional article number to filter (e.g., "310")
        limit: Max results (default: 5)

    Returns:
        NEC search results with citations
    """
    tools = get_knowledge_tools()
    return tools.nec_search(query, article_filter, limit)


def nec_exception_search(base_rule: str, context: Optional[str] = None, limit: int = 5) -> str:
    """
    Search for exceptions to a base NEC rule

    Args:
        base_rule: Base NEC section (e.g., "240.4", "310.16")
        context: Optional context (e.g., "small conductors")
        limit: Max results (default: 5)

    Returns:
        Exception information with citations
    """
    tools = get_knowledge_tools()
    return tools.nec_exception_search(base_rule, context, limit)


def nec_table_lookup(table_id: str, **lookup_params) -> str:
    """
    Look up values from NEC tables

    Args:
        table_id: Table identifier (e.g., "Table 310.16")
        **lookup_params: Lookup parameters (varies by table)

    Returns:
        Table value with NEC reference
    """
    tools = get_knowledge_tools()
    return tools.nec_table_lookup(table_id, lookup_params)


if __name__ == "__main__":
    # Test the knowledge tools
    print("=== Testing NEC Knowledge Tools ===\n")

    tools = NECKnowledgeTools()

    # Test 1: NEC search
    print("1. Testing nec_search:")
    print(nec_search("conductor ampacity requirements", limit=3))
    print("\n" + "="*80 + "\n")

    # Test 2: Exception search
    print("2. Testing nec_exception_search:")
    print(nec_exception_search("240.4", "small conductors", limit=3))
    print("\n" + "="*80 + "\n")

    # Test 3: Table lookup (ampacity)
    print("3. Testing nec_table_lookup (ampacity):")
    print(nec_table_lookup("Table 310.16",
                          conductor_size="12 AWG",
                          temperature_rating="75°C",
                          conductor_type="copper"))
    print("\n" + "="*80 + "\n")

    # Test 4: Table lookup (working space)
    print("4. Testing nec_table_lookup (working space):")
    print(nec_table_lookup("Table 110.26(A)(1)",
                          voltage_to_ground=120,
                          condition=1))
