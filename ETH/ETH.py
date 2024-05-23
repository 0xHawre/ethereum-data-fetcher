import requests
import json
import time
from datetime import datetime
import random

RPC_URLS = [
    "https://eth1.lava.build/lava-referer-fbd614bb-40a2-46c0-9f86-675e78683794/",

]

ETH_METHOD = {
    "jsonrpc": "2.0",
    "method": "eth_gasPrice",
    "id": 1
}

def fetch_ethereum_data(url):
    try:
        response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(ETH_METHOD))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch Ethereum data from {url}: {e}")
        return None

def main():
    usage_count = 0
    while True:
        for url in RPC_URLS:
            eth_data = fetch_ethereum_data(url)
            if eth_data:
                usage_count += 1
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}] RPC Call Count: {usage_count}")
                print(f"Ethereum Data from {url}: {json.dumps(eth_data, indent=4)}")
            else:
                print(f"Failed to fetch Ethereum data from {url}.")

            # Sleep for a random interval between 10 to 25 seconds
            sleep_interval = random.uniform(10, 25)
            time.sleep(sleep_interval)

if __name__ == "__main__":
    main()
