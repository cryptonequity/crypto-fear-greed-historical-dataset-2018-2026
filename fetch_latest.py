import json
import urllib.request

ENDPOINTS = {
    "fear_and_greed": "https://cryptonequity.com/history/data/fng_history_2018_2026.json",
    "btc_history": "https://cryptonequity.com/history/data/prices/btc_history.json",
    "eth_history": "https://cryptonequity.com/history/data/prices/eth_history.json",
    "sol_history": "https://cryptonequity.com/history/data/prices/sol_history.json",
    "hype_history": "https://cryptonequity.com/history/data/prices/hype_history.json",
}

def fetch_dataset(name: str, url: str) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": "CryptonEquity-Dataset-Client/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        records = data.get("records", [])
        print(f"[{name}] Loaded {len(records)} records. Latest: {records[-1] if records else 'N/A'}")

if __name__ == "__main__":
    for key, endpoint in ENDPOINTS.items():
        fetch_dataset(key, endpoint)
