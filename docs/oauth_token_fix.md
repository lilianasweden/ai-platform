# Fix: OAuth token refresh
Handle 401 responses mid-session by automatically refreshing expired tokens.
Previously caused silent failures in long-running agent sessions.
