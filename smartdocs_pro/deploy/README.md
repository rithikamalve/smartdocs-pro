# SmartDocs Pro Deployment

## Docker Backend

Build and run the backend locally:

```bash
docker build -f deploy/Dockerfile -t smartdocs-backend .
docker run --env-file .env -p 5000:5000 smartdocs-backend
```

## Render.com Deployment

- Connect your repo to [Render.com](https://render.com/)
- Add your secrets to the Render dashboard or use `.env`
- Deploy using the provided `render.yaml`
- Health check: `/status` endpoint

## GitHub Actions CI/CD

- On push to `main`, tests in `tests/` are run automatically
- Add deployment steps as needed

## Environment Variables

- `GROQ_API_KEY` - Your Groq API key
- `HF_API_KEY` - Your Hugging Face API key
- `DATABASE_URL` - SQLite DB path (default: `sqlite:///smartdocs.db`)
- `LOG_LEVEL` - Logging level (default: `INFO`)

## Frontend

- Deploy Streamlit frontend separately (e.g., Streamlit Cloud)
- Set `API_URL` in Streamlit secrets to point to your backend 