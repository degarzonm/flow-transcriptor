from ibm_credentials import load_credentials
from ws_client import ws_transcriptor

if __name__ == "__main__":
    ws_uri = load_credentials()
    tt=ws_transcriptor(uri = ws_uri, timeout= 10,log=True,)
    print(tt)