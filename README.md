# 📊 Crypto Fear & Greed Index Historical Dataset (2018–2026) + 18-Asset Retrospective

Machine-readable daily historical archive of the **Crypto Fear & Greed Index (2018–2026)** alongside multi-year OHLCV price trajectories for **18 major cryptocurrencies** (BTC, ETH, SOL, HYPE, XMR, SUI, TON, ARB, PEPE, and more).

Maintained and updated daily by **[CryptonEquity Institutional Terminal](https://cryptonequity.com/history/)**.

---

## 🔗 Live Interactive Charts & Full Datasets

* **Live Fear & Greed + Price Retrospective Hub:** [CryptonEquity Historical Market Ledger](https://cryptonequity.com/history/)
* **Bitcoin (BTC) All-Time Price & Sentiment Chart:** [BTC Historical Price & Cycle Data](https://cryptonequity.com/history/btc)
* **Ethereum (ETH) Price Trajectory:** [ETH Historical Price Ledger](https://cryptonequity.com/history/eth)
* **Solana (SOL) Cycle Retrospective:** [SOL Historical Price & Volume](https://cryptonequity.com/history/sol)
* **Hyperliquid (HYPE) & Monero (XMR) Data:** [HYPE History](https://cryptonequity.com/history/hype) | [XMR History](https://cryptonequity.com/history/xmr)
* **Real-Time Derivatives & Market Radars:** [Perpetual Funding Rate Heatmap](https://cryptonequity.com/funding-heatmap.php) | [Live Crypto Bubbles Visualizer](https://cryptonequity.com/bubbles/)

---

## 📁 Repository Contents

| File / Endpoint | Format | Description |
| :--- | :--- | :--- |
| `fng_history_2018_2026.json` | JSON | Full daily Fear & Greed Index records (`0–100` score + sentiment classification) from Feb 2018 to 2026. |
| `fng_history_2018_2026.csv` | CSV | Flat tabular format ready for `pandas`, Excel, R, and quantitative backtesting. |
| `fetch_latest.py` | Python | Zero-dependency script to pull live updates directly from CryptonEquity telemetry endpoints. |

---

## 🐍 Quick Start (Python / Pandas)

Load the live dataset directly into a `pandas` DataFrame for quantitative analysis or backtesting:

```python
import pandas as pd

# Load Crypto Fear & Greed Index (2018-2026) directly from CryptonEquity
fng_url = "[https://cryptonequity.com/history/data/fng_history_2018_2026.csv](https://cryptonequity.com/history/data/fng_history_2018_2026.csv)"
df_fng = pd.read_csv(fng_url)
print(df_fng.tail(10))

# Load Bitcoin (BTC) daily OHLCV historical dataset
btc_url = "[https://cryptonequity.com/history/data/prices/btc_history.csv](https://cryptonequity.com/history/data/prices/btc_history.csv)"
df_btc = pd.read_csv(btc_url)
print(df_btc.tail(10))
