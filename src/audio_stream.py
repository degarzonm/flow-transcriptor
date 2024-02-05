import pyaudio
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
    rec = timeout

    for _ in range(0, int(RATE / CHUNK * rec)):
        data = stream.read(CHUNK)
        ws.send(data, ABNF.OPCODE_BINARY)

    stream.stop_stream()
    stream.close()
    print("* done recording")

    data = {"action": "stop"}
    ws.send(json.dumps(data).encode('utf8'))
    p.terminate()