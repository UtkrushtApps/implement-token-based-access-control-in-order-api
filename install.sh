#!/bin/bash
set -e

# Create and activate virtual environment
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

echo "[install.sh] Python virtual environment set up and dependencies installed."
