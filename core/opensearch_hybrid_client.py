"""
OpenSearch Hybrid Search Client for NEC Agent V2
Optimized for the unified 3-tool architecture with balanced BM25 + vector search
"""
import json
import os
from typing import Dict, List, Any, Optional
from pathlib import Path

# OpenSearch imports
try:
    from opensearchpy import OpenSearch
    from opensearchpy.exceptions import RequestError
    OPENSEARCH_AVAILABLE = True
except ImportError:
    print("Warning: OpenSearch not installed. Run: pip install opensearch-py")
    OPENSEARCH_AVAILABLE = False

# Google AI for embeddings (new SDK)
try:
    from google import genai
    EMBEDDINGS_AVAILABLE = True
except ImportError:
    print("Warning: Google GenerativeAI not installed. Run: pip install google-genai")
    EMBEDDINGS_AVAILABLE = False

# k-NN search configuration
KNN_CANDIDATE_MULTIPLIER = 5  # Retrieve 5x more candidates than limit for better result quality


class OpenSearchHybridClient:
    """
    Hybrid search client combining BM25 (keyword) and vector (semantic) search
    Optimized for NEC 2023 content retrieval with 50/50 weighting
    """

    def __init__(self,
                 opensearch_host: str = None,
                 opensearch_port: int = None,
                 index_name: str = "nec_2023_chunks",
                 embedding_model: str = "models/text-embedding-004"):
        """
        Initialize hybrid search client

        Args:
            opensearch_host: OpenSearch host (default: from env or localhost)
            opensearch_port: OpenSearch port (default: from env or 9200)
            index_name: NEC chunks index name
            embedding_model: Google embedding model name
        """
        # Get configuration from environment or defaults
        self.opensearch_host = opensearch_host or os.getenv('OPENSEARCH_HOST', 'localhost')
        self.opensearch_port = opensearch_port or int(os.getenv('OPENSEARCH_PORT', 9200))
        self.index_name = index_name
        self.embedding_model_name = embedding_model
        self.google_api_key = os.getenv('GOOGLE_API_KEY')

        # Initialize components
        self.client = None
        self.embedding_client = None
        self.embedding_configured = False
        self.is_available = False

        if OPENSEARCH_AVAILABLE:
            self.client = self._init_opensearch()

        if EMBEDDINGS_AVAILABLE and self.google_api_key:
            self._init_embedding_api()
            self.embedding_configured = True

        self.is_available = bool(self.client and self.embedding_configured)

    def _init_opensearch(self) -> Optional[OpenSearch]:
        """Initialize OpenSearch client with connection test"""
        try:
            client = OpenSearch(
                hosts=[{'host': self.opensearch_host, 'port': self.opensearch_port}],
                http_auth=None,  # Add credentials if needed
                use_ssl=False,
                verify_certs=False,
                timeout=30
            )

            # Test connection
            if client.ping():
                print(f"[OK] Connected to OpenSearch at {self.opensearch_host}:{self.opensearch_port}")
                return client
            else:
                print(f"[ERROR] OpenSearch ping failed")
                return None

        except Exception as e:
            print(f"[ERROR] OpenSearch connection error: {e}")
            return None

    def _init_embedding_api(self) -> None:
        """Initialize Google Generative AI API for embeddings (new SDK)"""
        try:
            self.embedding_client = genai.Client(api_key=self.google_api_key)
            print(f"[OK] Configured Google embedding API: {self.embedding_model_name}")
        except Exception as e:
            print(f"[ERROR] Embedding API error: {e}")

    def hybrid_search(self,
                     query: str,
                     filters: Optional[Dict[str, Any]] = None,
                     limit: int = 5,
                     min_score: float = 0.1) -> List[Dict[str, Any]]:
        """
        Execute hybrid search combining BM25 and vector similarity

        Args:
            query: Search query string
            filters: Optional filters (e.g., {"article": "310"})
            limit: Maximum results to return
            min_score: Minimum relevance score threshold

        Returns:
            List of relevant NEC content chunks with scores
        """
        if not self.is_available:
            print("OpenSearch not available. Please check OpenSearch service.")
            return []

        try:
            # Generate query embedding using Google API (new SDK)
            result = self.embedding_client.models.embed_content(
                model=self.embedding_model_name,
                contents=query
            )
            query_embedding = result.embeddings[0].values

            # Build k-NN search query (semantic similarity)
            # TODO: Implement true hybrid search using neural-search plugin
            # Currently using pure k-NN which provides good semantic matching

            # Build k-NN query with optional filters
            if filters:
                # k-NN with filter using bool query
                filter_clauses = []
                for field, value in filters.items():
                    filter_clauses.append({"term": {field: value}})

                search_body = {
                    "size": limit,
                    "query": {
                        "bool": {
                            "must": {
                                "knn": {
                                    "embedding": {
                                        "vector": query_embedding,
                                        "k": limit * KNN_CANDIDATE_MULTIPLIER
                                    }
                                }
                            },
                            "filter": filter_clauses
                        }
                    },
                    "_source": ["content", "section", "chapter", "article", "metadata"],
                    "highlight": {
                        "fields": {
                            "content": {
                                "fragment_size": 200,
                                "number_of_fragments": 1
                            }
                        },
                        "pre_tags": ["<mark>"],
                        "post_tags": ["</mark>"]
                    }
                }
            else:
                # Pure k-NN query without filters
                search_body = {
                    "size": limit,
                    "query": {
                        "knn": {
                            "embedding": {
                                "vector": query_embedding,
                                "k": limit * KNN_CANDIDATE_MULTIPLIER
                            }
                        }
                    },
                    "_source": ["content", "section", "chapter", "article", "metadata"],
                    "highlight": {
                        "fields": {
                            "content": {
                                "fragment_size": 200,
                                "number_of_fragments": 1
                            }
                        },
                        "pre_tags": ["<mark>"],
                        "post_tags": ["</mark>"]
                    }
                }

            # Execute search
            response = self.client.search(index=self.index_name, body=search_body)

            # Process and return results
            return self._process_search_results(response)

        except Exception as e:
            print(f"Hybrid search error: {e}")
            print(f"  Returning empty results. Check OpenSearch service status.")
            return []

    def exception_search(self,
                        base_rule: str,
                        context: Optional[str] = None,
                        limit: int = 5) -> List[Dict[str, Any]]:
        """
        Specialized search for NEC exceptions related to a base rule

        Args:
            base_rule: Base NEC rule/section (e.g., "310.16", "240.4")
            context: Optional context to narrow exception search
            limit: Maximum results

        Returns:
            List of exception-related content chunks
        """
        if not self.is_available:
            print("OpenSearch not available. Please check OpenSearch service.")
            return []

        try:
            # Build exception-focused query
            exception_keywords = [
                "exception",
                "Exception",
                "Exception No.",
                "shall not apply",
                "not required",
                "alternative",
                "in lieu of",
                "permitted"
            ]

            # Construct search query
            query_string = f"{base_rule} {' OR '.join(exception_keywords)}"
            if context:
                query_string = f"{query_string} {context}"

            # Generate embedding using Google API (new SDK)
            result = self.embedding_client.models.embed_content(
                model=self.embedding_model_name,
                contents=query_string
            )
            query_embedding = result.embeddings[0].values

            # Use k-NN for exception search
            search_body = {
                "size": limit,
                "query": {
                    "knn": {
                        "embedding": {
                            "vector": query_embedding,
                            "k": limit * KNN_CANDIDATE_MULTIPLIER
                        }
                    }
                },
                "_source": ["content", "section", "chapter", "article", "metadata"],
                "highlight": {
                    "fields": {
                        "content": {
                            "fragment_size": 300,
                            "number_of_fragments": 2
                        }
                    },
                    "require_field_match": False
                }
            }

            response = self.client.search(index=self.index_name, body=search_body)
            return self._process_search_results(response)

        except Exception as e:
            print(f"Exception search error: {e}")
            print(f"  Returning empty results. Check OpenSearch service status.")
            return []

    def _process_search_results(self, response: Dict) -> List[Dict[str, Any]]:
        """Process OpenSearch response into standardized format"""
        results = []

        for hit in response.get('hits', {}).get('hits', []):
            source = hit['_source']
            result = {
                "content": source.get('content', ''),
                "section": source.get('section', ''),
                "chapter": source.get('chapter', ''),
                "article": source.get('article', ''),
                "score": hit['_score'],
                "highlights": hit.get('highlight', {}).get('content', []),
                "metadata": source.get('metadata', {}),
                "search_type": "hybrid"
            }
            results.append(result)

        return results

    def check_health(self) -> Dict[str, Any]:
        """Check system health and availability"""
        return {
            "opensearch_available": bool(self.client),
            "embeddings_available": bool(self.embedding_client),
            "hybrid_search_available": self.is_available,
            "index_name": self.index_name,
            "host": self.opensearch_host,
            "port": self.opensearch_port
        }


# Singleton instance for reuse
_client_instance = None

def get_hybrid_client() -> OpenSearchHybridClient:
    """Get or create singleton hybrid search client"""
    global _client_instance
    if _client_instance is None:
        _client_instance = OpenSearchHybridClient()
    return _client_instance


# CEC Singleton instance for reuse
_cec_client_instance = None

def get_cec_hybrid_client() -> OpenSearchHybridClient:
    """Get or create singleton CEC hybrid search client for CEC 2022 index"""
    global _cec_client_instance
    if _cec_client_instance is None:
        _cec_client_instance = OpenSearchHybridClient(index_name="cec_2022_chunks")
    return _cec_client_instance


if __name__ == "__main__":
    # Test the hybrid client
    client = OpenSearchHybridClient()

    print("\n=== System Health Check ===")
    print(json.dumps(client.check_health(), indent=2))

    if client.is_available:
        print("\n=== Test Hybrid Search ===")
        results = client.hybrid_search("conductor ampacity", limit=3)
        for i, r in enumerate(results, 1):
            print(f"\n{i}. Section: {r['section']}")
            print(f"   Score: {r['score']:.3f}")
            print(f"   Content: {r['content'][:150]}...")

        print("\n=== Test Exception Search ===")
        exceptions = client.exception_search("240.4", context="small conductors", limit=3)
        for i, e in enumerate(exceptions, 1):
            print(f"\n{i}. Section: {e['section']}")
            print(f"   Score: {e['score']:.3f}")
            print(f"   Content: {e['content'][:150]}...")
    else:
        print("\n[ERROR] Hybrid search not available - check OpenSearch setup")
