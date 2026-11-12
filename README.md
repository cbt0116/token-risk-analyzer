# Token Risk Analyzer

A small Python prototype that reviews supplied token metadata and returns transparent heuristic flags for manual follow-up.

The project demonstrates basic Python logic and pytest testing around common token-risk signals. It does **not** connect to a blockchain, retrieve or verify token data, detect scams, or assess whether an investment is suitable.

## What it checks

The `analyze(token)` function in `risk.py` accepts a Python dictionary and evaluates these fields:

| Input field | Current heuristic |
|---|---|
| `contract_verified` | Adds a flag unless the supplied value is truthy |
| `owner_can_mint` | Adds a flag when truthy; defaults to `True` if missing |
| `owner_can_pause` | Adds a flag when truthy; defaults to `True` if missing |
| `liquidity_locked` | Adds a flag unless the value is exactly `True` |
| `holder_count` | Adds a flag when below 100; defaults to 0 if missing |

The function returns:
- `flags`: a list of explanatory messages
- `flag_count`: number of generated flags
- `assessment`: currently always `manual_review_required`
- `disclaimer`: a reminder that the output is heuristic only

These checks are intentionally simple. The result depends entirely on the accuracy and context of the input values.

## Requirements

- Python 3.11 or newer
- pytest 8.x for running the test suite

No external runtime dependencies are currently required by `risk.py`.

## Installation

Clone the repository:

```bash
git clone https://github.com/cbt0116/token-risk-analyzer.git
cd token-risk-analyzer
```

Create and activate a virtual environment.

**Windows PowerShell**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the development dependency:

```bash
pip install -r requirements.txt
```

## Run the example

Run the built-in sample:

```bash
python risk.py
```

Or call the function from another Python file:

```python
from risk import analyze

token_metadata = {
    "contract_verified": False,
    "owner_can_mint": True,
    "owner_can_pause": False,
    "liquidity_locked": False,
    "holder_count": 25,
}

result = analyze(token_metadata)

for flag in result["flags"]:
    print("-", flag)

print("Assessment:", result["assessment"])
print("Flag count:", result["flag_count"])
```

## Tests

Run the current pytest suite:

```bash
pytest
```

The existing test checks that missing verification and reported owner minting capability produce flags, and that the assessment remains `manual_review_required`.

Further useful tests would cover each individual signal, missing fields, boundary values such as a holder count of 100, and unexpected input types.

## Limitations and interpretation

- The tool analyzes only values supplied by the caller; it does not fetch on-chain data.
- It does not verify source code, ownership permissions, liquidity locks, or holder counts.
- A low holder count or an unlocked-liquidity flag is not proof of malicious activity.
- A verified contract or locked liquidity does not establish that a token is safe.
- The holder-count threshold is a simple example, not a validated risk model.
- The function does not calculate a probability, investment score, or buy/sell recommendation.
- The output is not a smart-contract audit, scam detector, or financial advice.

Always verify data independently and conduct manual technical review. Never rely on this prototype to make financial decisions.

## Potential improvements

- Add strict input validation and a documented input schema
- Add tests for all rules and boundary conditions
- Distinguish missing, unknown, and explicitly false metadata
- Include provenance and timestamps for externally sourced data if data integrations are added
- Add a CLI that accepts a JSON input file
- Add optional read-only blockchain data integrations, with source and freshness metadata

## License

No repository-level LICENSE file is currently documented. Add one to clarify reuse and distribution terms.
