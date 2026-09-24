# RAG Pipeline

## Overview
Our RAG (Retrieval-Augmented Generation) pipeline connects internal knowledge bases to AI agents, allowing them to answer questions grounded in up-to-date company data.

## Architecture

```
User query
    │
    ▼
Query embedding (Claude / text-embedding-3)
    │
    ▼
Vector search (Pinecone) ──► Top-K document chunks
    │
    ▼
Context assembly
    │
    ▼
LLM generation (Claude Sonnet)
    │
    ▼
Answer + cited sources
```

## Data Sources Currently Indexed
- HR Knowledge Base (Confluence)
- Engineering Handbook (this repo)
- Product documentation (Notion)
- Support tickets (Zendesk) — last 90 days

## Latency Targets
- Embedding: < 100ms
- Vector search: < 50ms
- LLM generation: < 2s (p95)
- End-to-end: < 3s (p95)

## Known Limitations
- PDFs with scanned content are not indexed (no OCR yet — see Issue #12)
- Confluence pages updated in the last 15 minutes may not be reflected (sync delay)
