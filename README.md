# Token Risk Analyzer

A transparent heuristic scoring demo that flags missing or concerning token metadata supplied as JSON. It does not predict scams or investment performance.

**Status:** Prototype · **Stage:** portfolio prototype

## Stack
Python 3.11+, pytest

## Quick start
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

See the project-specific instructions below. This repository is an independently developed portfolio prototype, not a production financial system.

## Safety and limitations
- No real-money transactions are performed.
- No private keys, seed phrases, API secrets, or credentials belong in source control.
- Review dependencies, configure secrets through environment variables, and obtain an independent security review before production use.
