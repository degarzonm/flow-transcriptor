import json
import threading
import websocket
import time

from audio_stream import read_audio
from audio_stream import RATE
from utils import format_and_print

FINALS = []
LAST = None
TRANSCRIPT = ""

def on_message(ws, message, log = False):
    global LAST
    try:
        data = json.loads(message)
        if "results" in data and data["results"]:
            transcript = data['results'][0]['alternatives'][0]['transcript']
            word_confidences = data['results'][0]['alternatives'][0]['word_confidence']
            long_transcript = "".join([x['results'][0]['alternatives'][0]['transcript'] for x in FINALS])
            
            if data["results"][0]["final"]:
                #clear_console()
                FINALS.append(data)
                LAST = None
            else:
                LAST = data
            if log: 
                #if transcript not null
                format_and_print(transcript, word_confidences)
                print(long_transcript)

    except KeyError as e:
        print(f"Key error: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")


def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg, log = False):
    global LAST
    global TRANSCRIPT
    if log:
        print("*stop recording")
        print("closing connection")
    
    if LAST:
        FINALS.append(LAST)
    TRANSCRIPT = "".join([x['results'][0]['alternatives'][0]['transcript'] for x in FINALS])
    if log: print("final Transcript:" + TRANSCRIPT)

def on_open(ws, timeout):
    data = {
        "action": "start",
        "content-type": f"audio/l16;rate={RATE}",
        "interim_results": True,
        "low_latency": True,
        "word_confidence": True,
        "timestamps": True,
        "max_alternatives": 2
    }
    ws.send(json.dumps(data).encode('utf8'))
    threading.Thread(target=read_audio, args=[ws, timeout]).start()

def ws_transcriptor(uri, timeout=10, log = False):
    ws = websocket.WebSocketApp(uri, on_open=lambda 
                                ws: on_open(ws, timeout), 
                                    on_message=lambda 
                                ws,message: on_message(ws, message, log), 
                                    on_error=on_error, 
                                    on_close=lambda 
                                ws, close_status_code, close_msg: on_close(ws, close_status_code, close_msg, log))
    
    wst = threading.Thread(target=ws.run_forever)
    wst.start()
    try:
        while wst.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        ws.close()
    finally:
        return TRANSCRIPT
    