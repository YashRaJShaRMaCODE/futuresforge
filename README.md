# FutureForge — Binance Futures testnet CLI

FutureForge is a local learning tool for previewing and placing USDⓈ-M Futures market and limit orders on the Binance Futures **testnet**. The client is hard-wired to testnet; this project does not provide a mainnet trading mode, financial advice, or a real-money trading service.

## Setup

Use Python 3.10 or later. Preview commands need only the Python standard library. To submit testnet orders, create a virtual environment and install the exchange client:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Add Futures testnet API credentials to `.env` only if you plan to submit orders. Keep withdrawals disabled, never reuse mainnet credentials, and do not commit `.env` or `bot.log`.

## Preview and place testnet orders

Commands preview by default: they validate and print the order without loading credentials, contacting Binance, or creating a log file.

```powershell
python src/market_orders.py BTCUSDT BUY 0.01
python src/limit_order.py BTCUSDT SELL 0.01 65000
```

To explicitly place a testnet order, append `--submit-testnet`:

```powershell
python src/market_orders.py BTCUSDT BUY 0.01 --submit-testnet
python src/limit_order.py BTCUSDT SELL 0.01 65000 --submit-testnet
```

The exchange remains responsible for symbol-specific quantity and price filters. Start with small testnet orders and check the returned status. A limit order can remain open until it fills or is cancelled in the Binance testnet interface.

## Checks

```powershell
python -m unittest discover -s tests
python -m compileall -q src tests
ruff check src tests
ruff format --check src tests
```

GitHub Actions runs these checks on every push and pull request. The preview tests remove API credentials from their environment and use `python -S`, so they cannot place orders or create a log file.

Only market and limit order entry points are implemented. TWAP, stop-limit, grid, and OCO features from earlier drafts are not included.

## Product scope

This is a local CLI, not a hosted trading SaaS: it has no user accounts, signal service, customer data store, billing or validated paying customers. Keep testnet credentials on your own machine; never put exchange credentials in a public build, web frontend or shared CI runner. Its honest current role is a public developer-education project for Python developers learning exchange API workflows. A one-off workshop could cover safe local setup, order previews, testnet-only submission and failure handling, but validate demand before offering it; there is no subscription or revenue claim today.

`free-for.dev` is not a reason to host this tool or expose API keys. The current preview mode works with Python's standard library, and public-repository CI can run the credential-free tests without exchange secrets.
