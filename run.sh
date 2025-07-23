#!/bin/bash
set -e

bash install.sh
source .venv/bin/activate

export PYTHONPATH=.

echo "[run.sh] Starting FastAPI app with uvicorn..."
uvicorn app.main:app --host 0.0.0.0 --port 8000
