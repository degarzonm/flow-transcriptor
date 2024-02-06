import pyaudio
import json
from websocket._abnf import ABNF

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def read_audio(ws, timeout):
    p = pyaudio.PyAudio()
    RATE = int(p.get_default_input_device_info()['defaultSampleRate'])
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("* recording")

    for _ in range(0, int(RATE / CHUNK * timeout)):
        data = stream.read(CHUNK)
        try:
            ws.send(data, ABNF.OPCODE_BINARY)
        except:
            print('.',end = '')
    stream.stop_stream()
    stream.close()

    # Send the 'stop' action to indicate that recording is finished
    data = {"action": "stop"}
    ws.send(json.dumps(data).encode('utf8'))
    p.terminate()
    print("* done recording")
    ws.close()