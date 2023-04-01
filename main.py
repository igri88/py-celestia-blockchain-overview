import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

CELESTIA_NODE_URL = "https://celestia.api.explorers.guru/api/v1" # celestia-node API address

@app.route('/')
def index():
    # Getting information about the last block
    response = requests.get(f"{CELESTIA_NODE_URL}/blocks/latest")
    latest_block = response.json()

    # Getting information about the number of connected nodes
    response = requests.get(f"{CELESTIA_NODE_URL}/networks")
    net_info = response.json()

    # Getting information about the number of connected nodes
    response = requests.get(f"{CELESTIA_NODE_URL}/chain")
    chain_info = response.json()

    # Displaying information on a page
    return render_template('index.html', latest_block=latest_block, net_info=net_info, chain_info=chain_info)

if __name__ == '__main__':
    app.run(debug=True, port=2024)
