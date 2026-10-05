# RAG pipeline configuration
EMBEDDING_BATCH_SIZE = 32
MAX_CONTEXT_TOKENS = 4096
VECTOR_CACHE_TTL = 300  # seconds

# Fix: explicitly release embedding model from memory after each batch
# Previously the model was held in memory between requests, causing leak
RELEASE_MODEL_AFTER_BATCH = True
MEMORY_LIMIT_MB = 512
