# External API client configuration
BASE_URL = "https://api.ai-platform.internal"
DEFAULT_TIMEOUT = 30

# Fix: added exponential backoff for 429 rate limit responses
# Without this, burst traffic caused cascading failures across services
RATE_LIMIT_RETRY_ENABLED = True
MAX_RETRY_ATTEMPTS = 5
INITIAL_BACKOFF_S = 1
BACKOFF_MULTIPLIER = 2
JITTER_ENABLED = True
