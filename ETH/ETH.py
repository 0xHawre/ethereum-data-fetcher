import requests
import json
import logging
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

RPC_URLS = [
    "https://eth1.lava.build/lava-referer-b3ebd262-006d-4555-8273-6d1508c4e92d/",
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
        logging.error(f"Failed to fetch Ethereum data from {url}: {e}")
        return None

def main():
    usage_count = 0

    def task(url):
        nonlocal usage_count
        eth_data = fetch_ethereum_data(url)
        if eth_data:
            usage_count += 1
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"[{timestamp}] RPC Call Count: {usage_count}\nEthereum Data from {url}: {json.dumps(eth_data, indent=4)}"
            logging.info(log_message)
        else:
            logging.error(f"Failed to fetch Ethereum data from {url}.")

    with ThreadPoolExecutor(max_workers=len(RPC_URLS)) as executor:
        while True:
            futures = [executor.submit(task, url) for url in RPC_URLS]
            for future in as_completed(futures):
                pass  # Ensures that all tasks are completed before continuing

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
    main()
