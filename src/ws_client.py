import json
import threading
import websocket
import time

from audio_stream import read_audio

FINALS = []
LAST = None

def on_message(ws, message):
    global LAST
    data = json.loads(message)
    if "results" in data and data["results"][0]["final"]:
        FINALS.append(data)
        LAST = None
    else:
        LAST = data
    print(data['results'][0]['alternatives'][0]['transcript'])

def on_error(ws, error):
    print(error)

def on_close(ws):
    global LAST
    if LAST:
        FINALS.append(LAST)
    transcript = "".join([x['results'][0]['alternatives'][0]['transcript'] for x in FINALS])
    print(transcript)

def on_open(ws, timeout):
    data = {
        "action": "start",
        "content-type": f"audio/l16;rate={RATE}",
        "continuous": True,
        "interim_results": True,
        "word_confidence": True,
        "timestamps": True,
        "max_alternatives": 2
    }
    ws.send(json.dumps(data).encode('utf8'))
    threading.Thread(target=read_audio, args=[ws, timeout]).start()

def websocket_client(uri, timeout=30):
    ws = websocket.WebSocketApp(uri, on_open=lambda ws: on_open(ws, timeout), 
                                on_message=on_message, on_error=on_error, on_close=on_close)
    wst = threading.Thread(target=ws.run_forever)
    wst.start()
    try:
        while wst.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        ws.close()