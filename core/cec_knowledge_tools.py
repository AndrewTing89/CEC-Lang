"""
CEC Unified Tools - California Electrical Code Search
Provides CEC 2022 lookups for the unified agent (California-first architecture)

Tools:
1. cec_search - General rule and section search for CEC 2022
2. cec_exception_search - Targeted exception finding within CEC
3. compare_with_nec - Cross-reference CEC with NEC to identify differences
"""
import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add project root to path for imports
current_dir = Path(__file__).parent
project_root = current_dir.parent
sys.path.insert(0, str(project_root))

# Load environment variables from .env file BEFORE importing opensearch client
from dotenv import load_dotenv
load_dotenv()

# Import our components
from core.opensearch_hybrid_client import get_cec_hybrid_client, get_hybrid_client


class CECKnowledgeTools:
    """
    Unified tool system for CEC (California Electrical Code)
    Provides hybrid search for CEC 2022 content
    """

    def __init__(self):
        """Initialize CEC tools with search component"""
        self.search_client = get_cec_hybrid_client()
        self.nec_search_client = get_hybrid_client()  # For NEC comparison

        # Check availability
        self.search_available = self.search_client.is_available
        print(f"CEC Search available: {self.search_available}")

    def cec_search(self,
                   query: str,
                   article_filter: Optional[str] = None,
                   limit: int = 5) -> str:
        """
        Search CEC 2022 for rules, sections, and requirements

        This tool performs hybrid search (BM25 + vector) to find relevant
        CEC content based on your query. Use this for finding:
        - California-specific electrical requirements
        - CEC section text and interpretations
        - Rule applicability in California
        - Code requirements for California scenarios

        Args:
            query: Search query describing what you're looking for
            article_filter: Optional article number to filter results (e.g., "310", "240")
            limit: Maximum number of results to return (default: 5)

        Returns:
            Formatted string with CEC sections and their content
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
            return f"No CEC content found for query: {query}"

        if len(results) == 1 and "error" in results[0]:
            return f"Search error: {results[0]['error']}"

        # Format results
        output = [f"CEC 2022 search results for: '{query}'"]
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
                citation = f"CEC 2022 Section {section}"
            elif article:
                citation = f"CEC 2022 Article {article}"
            else:
                citation = "CEC 2022"

            output.append(f"Result {i} [{citation}] (relevance: {score:.2f})")
            output.append(f"{content}")
            output.append("")

        return "\n".join(output)

    def cec_exception_search(self,
                            base_rule: str,
                            context: Optional[str] = None,
                            limit: int = 5) -> str:
        """
        Search for CEC exceptions related to a base rule

        This tool specifically searches for exceptions, overrides, and
        alternative methods that may modify or supersede a base CEC rule.
        Use this whenever you:
        - Find a base rule and need to check for exceptions
        - Need to verify if alternative methods are permitted
        - Want to find "shall not apply" or "not required" conditions

        Args:
            base_rule: The base CEC rule/section (e.g., "310.16", "240.4", "250.32")
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
        output = [f"CEC 2022 exceptions for base rule: {base_rule}"]
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
                output.append(f"Exception {i} [CEC 2022 Section {section}] (relevance: {score:.2f})")
                output.append(f"{content}")
                output.append("")

        if not exception_found:
            output.append(f"No explicit exceptions found for {base_rule}.")
            output.append("The base rule likely applies without modification.")

        return "\n".join(output)

    def compare_with_nec(self,
                         section: str,
                         query: Optional[str] = None,
                         limit: int = 3) -> str:
        """
        Compare CEC content with NEC to identify differences

        This tool searches both CEC 2022 and NEC 2023 for the same topic
        and highlights any differences. Use this when:
        - User asks about national vs California requirements
        - You want to note that CEC differs from base NEC
        - Checking if a CA-specific amendment applies

        Args:
            section: The section number to compare (e.g., "408.2", "210.12")
            query: Optional query to refine the comparison context
            limit: Maximum results from each index (default: 3)

        Returns:
            Formatted comparison showing CEC vs NEC content
        """
        # Build search query
        search_query = section
        if query:
            search_query = f"{section} {query}"

        # Search CEC
        cec_results = self.search_client.hybrid_search(
            query=search_query,
            limit=limit
        )

        # Search NEC
        nec_results = self.nec_search_client.hybrid_search(
            query=search_query,
            limit=limit
        )

        # Format comparison
        output = [f"CEC vs NEC Comparison for: {section}"]
        if query:
            output.append(f"Context: {query}")
        output.append("")
        output.append("=" * 60)

        # CEC Results
        output.append("**California Electrical Code (CEC 2022):**")
        if cec_results and not (len(cec_results) == 1 and "error" in cec_results[0]):
            for i, result in enumerate(cec_results, 1):
                sec = result.get('section', 'Unknown')
                content = result.get('content', '')[:500]
                output.append(f"\n[CEC Section {sec}]")
                output.append(f"{content}...")
        else:
            output.append("No CEC content found for this section.")

        output.append("")
        output.append("-" * 60)

        # NEC Results
        output.append("**National Electrical Code (NEC 2023):**")
        if nec_results and not (len(nec_results) == 1 and "error" in nec_results[0]):
            for i, result in enumerate(nec_results, 1):
                sec = result.get('section', 'Unknown')
                content = result.get('content', '')[:500]
                output.append(f"\n[NEC Section {sec}]")
                output.append(f"{content}...")
        else:
            output.append("No NEC content found for this section.")

        output.append("")
        output.append("=" * 60)

        # Add interpretation note
        output.append("")
        output.append("**Note:** Review the content above to determine if CEC has California-specific")
        output.append("amendments. Look for [CEC] markers or content differences.")

        # Add teaser for detailed NEC calculation
        output.append("")
        output.append("---")
        output.append("TIP: Want a detailed calculation using NEC rules? Just ask:")
        output.append("'Show me the full NEC calculation' or 'What would this be under NEC?'")

        return "\n".join(output)


# Singleton instance
_tools_instance = None

def get_cec_knowledge_tools() -> CECKnowledgeTools:
    """Get or create singleton CEC unified tools instance"""
    global _tools_instance
    if _tools_instance is None:
        _tools_instance = CECKnowledgeTools()
    return _tools_instance


# Standalone function wrappers for Gemini function calling
def cec_search(query: str, article_filter: Optional[str] = None, limit: int = 5) -> str:
    """
    Search CEC 2022 for rules, sections, and requirements

    Args:
        query: What you're searching for
        article_filter: Optional article number to filter (e.g., "310")
        limit: Max results (default: 5)

    Returns:
        CEC search results with citations
    """
    tools = get_cec_knowledge_tools()
    return tools.cec_search(query, article_filter, limit)


def cec_exception_search(base_rule: str, context: Optional[str] = None, limit: int = 5) -> str:
    """
    Search for exceptions to a base CEC rule

    Args:
        base_rule: Base CEC section (e.g., "240.4", "310.16")
        context: Optional context (e.g., "small conductors")
        limit: Max results (default: 5)

    Returns:
        Exception information with citations
    """
    tools = get_cec_knowledge_tools()
    return tools.cec_exception_search(base_rule, context, limit)


def compare_with_nec(section: str, query: Optional[str] = None, limit: int = 3) -> str:
    """
    Compare CEC with NEC to identify differences

    Args:
        section: Section number to compare (e.g., "408.2")
        query: Optional context to refine comparison
        limit: Max results from each index (default: 3)

    Returns:
        Comparison showing CEC vs NEC content
    """
    tools = get_cec_knowledge_tools()
    return tools.compare_with_nec(section, query, limit)


if __name__ == "__main__":
    # Test the CEC unified tools
    print("=== Testing CEC Unified Tools ===\n")

    tools = CECKnowledgeTools()

    # Test 1: CEC search
    print("1. Testing cec_search:")
    print(cec_search("GFCI requirements kitchen", limit=3))
    print("\n" + "="*80 + "\n")

    # Test 2: Exception search
    print("2. Testing cec_exception_search:")
    print(cec_exception_search("210.8", "kitchen", limit=3))
    print("\n" + "="*80 + "\n")

    # Test 3: Compare with NEC
    print("3. Testing compare_with_nec:")
    print(compare_with_nec("408.2", "panelboard spaces", limit=2))
    print("\n" + "="*80 + "\n")
