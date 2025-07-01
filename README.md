# SecAuditBot

SecAuditBot is an AI-enhanced network security audit tool that scans, analyzes, and generates human-friendly reports.

## Features
- Port scanning with Nmap
- Shodan exposed service checks
- AI-generated audit summary
- PDF export

## Stack
Python, FastAPI, python-nmap, Shodan, OpenAI API

## Setup
1. Clone the repo
2. Add `.env` with your OpenAI & Shodan API keys
3. Install deps: `pip install -r requirements.txt`
4. Run FastAPI: `uvicorn app.main:app --reload`
