# Local Development Setup

## Prerequisites
- Python 3.11+
- Docker Desktop
- AWS CLI configured with `dev` profile

## Installation

```bash
git clone https://github.com/lilianasweden/ai-platform
cd ai-platform
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # fill in your API keys
docker-compose up -d  # starts local vector DB and Redis
```

## Running the Agent Framework locally

```bash
python -m agents.server --port 8000
```

Test with:
```bash
curl -X POST http://localhost:8000/agent/run \
  -H "Content-Type: application/json" \
  -d '{"agent": "hr-assistant", "query": "What is the education reimbursement limit?"}'
```

## Environment Variables

| Variable | Description |
|---------|-------------|
| `ANTHROPIC_API_KEY` | Claude API key |
| `PINECONE_API_KEY` | Vector database key |
| `OPENAI_API_KEY` | Fallback model key |
| `RAG_INDEX_NAME` | Pinecone index to query |
