#Ethereum Data Fetcher
This Python script fetches Ethereum gas price data from specified RPC endpoints. It makes repeated requests to the endpoints, logs the responses, and includes a timestamp and call count for each request.

##Prerequisites
Ensure you have Python and the requests package installed on your system.

##Install Python
If Python is not already installed, you can install it using the following commands:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
```
##Install Required Python Packages
Install the requests package using pip:
```bash
pip3 install requests
```
##Setup

1.Clone the Repository:
```bash
git clone https://github.com/Hafxhak/ethereum-data-fetcher
cd ethereum-data-fetcher
&& cd ETH
```
2.Edit the Script:
Open the script in a text editor:
```bash
nano ETH.py
```
Replace the placeholder URL in the RPC_URLS list with your own Ethereum RPC endpoint URLs. Example:
```
RPC_URLS = [
    "https://eth1.lava.build/lava-referer-your-unique-id/",  # replace with your RPC
]
```

Save and exit the editor (for nano, press CTRL + X, then Y, and Enter).

##Running the Script

1.Install and Use Screen:
Install screen to run the script in a detached session:

```
sudo apt install screen -y
screen -S eth
```
2.Run the Script:
Execute the script using Python 3:

```bash
python3 ETH.py
```
#Example Output
The script will log the response from the RPC endpoint along with a timestamp and call count for each request. Example output:
```[2024-05-24 12:00:00] RPC Call Count: 1
Ethereum Data from https://eth1.lava.build/lava-referer-your-unique-id/:
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x09184e72a000"
}
```


3.Detach from the Screen Session:

Detach from the screen session without stopping the script by pressing CTRL + A, then D.








