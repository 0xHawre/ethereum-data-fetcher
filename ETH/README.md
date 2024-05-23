Ethereum Data Fetcher
This Python script fetches Ethereum gas price data from a specified RPC endpoint. It makes repeated requests to the endpoint, logs the response, and includes a timestamp and call count for each request.

Prerequisites
Ensure you have Python and the requests package installed on your system.

Install Python
If Python is not already installed, you can install it using the following commands:

bash
Copy code
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
Install Required Python Packages
Install the requests package using pip:

bash
Copy code
pip3 install requests
Configuration
RPC URL
Replace the placeholder URL in the RPC_URLS list with your own Ethereum RPC endpoint URLs. Example:

python
Copy code
RPC_URLS = [
    "https://eth1.lava.build/lava-referer-your-unique-id/", # replace with your RPC
    # Add more URLs as needed
]
Usage
Create a Directory for the Script:

bash
Copy code
mkdir ETH
cd ETH
Create the Script File:

Create a new Python file named ETH.py using nano or your preferred text editor:

bash
Copy code
nano ETH.py
Copy and Paste the Script:

Copy the following script into ETH.py:

python
Copy code
import requests
import json
import time
from datetime import datetime
import random

RPC_URLS = [
    "https://youre RPC" # replace with your RPC
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
            sleep_interval = random.randint(10, 25)
            time.sleep(sleep_interval)

if __name__ == "__main__":
    main()
Save and Exit: Save the file and exit the text editor (for nano, press CTRL + X, then Y, and Enter).

Install and Use Screen:

Install screen to run the script in a detached session:

bash
Copy code
sudo apt install screen -y
Start a new screen session:

bash
Copy code
screen -S eth
Run the Script:

Execute the script using Python 3:

bash
Copy code
python3 ETH.py
Detach from the Screen Session:

Detach from the screen session without stopping the script by pressing CTRL + A, then D.

Reattach to the Screen Session:

To reattach to the screen session later, use:

bash
Copy code
screen -r eth
Example Output
plaintext
Copy code
[2024-05-24 12:00:00] RPC Call Count: 1
Ethereum Data from https://eth1.lava.build/lava-referer-your-unique-id/: 
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x09184e72a000"
}
