from ibm_credentials import load_credentials
from ws_client import websocket_client

if __name__ == "__main__":
    ws_uri = load_credentials()
    websocket_client(ws_uri, 30)