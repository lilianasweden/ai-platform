# DB Connection Pool — Configuration

## Problem
Under high load, integration tests were failing with connection pool exhaustion errors.
The default pool size (5) was insufficient for concurrent test workers.

## Fix
Increased `DB_POOL_SIZE` from 5 → 20 and `DB_POOL_MAX_OVERFLOW` from 10 → 30.
Added pool pre-ping to detect stale connections before checkout.

## Configuration
```python
DB_POOL_SIZE = 20          # was 5
DB_POOL_MAX_OVERFLOW = 30  # was 10
DB_POOL_PRE_PING = True    # new — drops stale connections before use
DB_POOL_TIMEOUT = 30       # seconds before giving up on a connection
```

## Testing
- Ran full integration suite with 8 parallel workers: 0 pool exhaustion errors
- Latency back under 200ms at p95
- No regressions in unit tests

## References
- AIDEV-2 (Jira)
- Fixes flaky test pattern reported in #dev-team
