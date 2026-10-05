# Vector search configuration
INDEX_TYPE = "hnsw"
SIMILARITY_METRIC = "cosine"

# Fix: increased timeout and added retry for slow shard responses
# Queries were timing out under load when >2 shards responded slowly
QUERY_TIMEOUT_MS = 800   # was 200ms — too aggressive for p99 latency
MAX_RETRIES = 3
RETRY_BACKOFF_MS = 50
TOP_K_RESULTS = 10
