# FutureForge

## Learn exchange order APIs on a demo account

FutureForge is a small Python CLI for previewing Binance USDⓈ-M Futures market and limit orders, then optionally submitting them to the exchange testnet.

### Who it may help

Python developers and instructors teaching exchange API request structure, validation, credentials, and order states.

### Safety design

- Preview is the default and does not load credentials or call the exchange.
- Testnet submission requires a separate explicit flag.
- The endpoint is hard-wired to the demo/test environment; no mainnet switch exists.
- CI tests run without exchange credentials.

### Current limits

Only market and limit entry are supported. Exchange filters remain authoritative; testnet is not a guarantee of production execution behavior. There is no strategy engine, trading advice, hosted app, or revenue claim.

### Business hypothesis

A bounded hands-on workshop on safe API order workflows may be sellable to developer learners. Interview instructors and Python developers before setting a price or promising outcomes.
