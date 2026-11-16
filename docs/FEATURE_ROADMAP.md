# FutureForge feature roadmap

Impact and effort are estimates. The actual product is a local, testnet-only order-entry CLI. Do not add mainnet execution, financial advice, trading signals, or claims of profit.

| # | Feature | User problem | Alternative gap to validate | Impact | Effort |
|---:|---|---|---|---|---|
| 1 | Verbose order preview with normalized parameters | Learners need to understand exactly what the CLI will send | Generic exchange libraries require users to construct payloads | High | Low |
| 2 | Symbol filter preflight | Invalid quantity/price steps cause rejected orders | Exchange filters are easy to miss when starting from raw APIs | High | Medium |
| 3 | Human-readable API error guide | Raw exchange errors are difficult for learners to debug | Large frameworks have broad docs rather than this narrow flow | High | Medium |
| 4 | Testnet connectivity and clock check | Users cannot tell bad network/key configuration from code errors | Testnet setup and API errors are often mixed together | High | Medium |
| 5 | Credentials permission preflight | Overbroad API permissions increase key risk | Setup docs cannot verify safe permissions automatically | High | Medium |
| 6 | Mock exchange adapter for offline exercises | Students need predictable tests without an account | External demo servers can fail or change | High | Medium |
| 7 | Order lifecycle walkthrough | Learners need to understand accepted/open/filled/rejected states | Entry-only examples stop before lifecycle handling | High | Medium |
| 8 | Cancel testnet order command | Open limit orders need a safe cleanup path | Many minimal examples only place orders | High | Medium |
| 9 | Idempotent client order IDs | Retries may duplicate an order | Beginners need retry safety explained | High | Medium |
| 10 | Dry-run JSON export | Learners need a machine-readable request preview | Console output is hard to include in lab materials | Medium | Low |
| 11 | Instructor exercise pack | Teachers need reusable test cases and answer keys | Framework docs are not a short workshop curriculum | Medium | Medium |
| 12 | Testnet state snapshot | Learners need to compare order state before and after actions | Remote demos reset or expire state | Medium | Medium |
| 13 | Python version and dependency preflight | Setup fails before learners understand the API | Framework installations can be heavier than a tiny CLI | Medium | Low |
| 14 | Replayable, credential-free fixtures | Maintainers need regression coverage across exchange errors | External APIs are unstable in CI | Medium | Medium |
| 15 | Workshop completion and feedback flow | A potential paid educator needs evidence of learner progress | Open-source tools do not provide a guided workshop path | Low | Medium |

## Build rule

Implement only after learner/instructor interviews. Keep all automated checks credential-free. Any exchange submission stays behind explicit `--submit-testnet`; never use mainnet credentials or add a real-money switch. The current safe preview and testnet-only submission already cover the foundational flow.
