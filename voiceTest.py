import wave
import sys
import subprocess
import json
from vosk import Model, KaldiRecognizer, SetLogLevel


def voice_recognition(file_name):
    # You can set log level to -1 to disable debug messages
    SetLogLevel(-1)

    subprocess.call(['converter/ffmpeg/bin/ffmpeg.exe', '-hide_banner', '-loglevel', 'warning', '-y', '-i', file_name, 
                    '-acodec', 'pcm_s16le', '-ac', '1', '-ar', '16000', 'out.wav'])

    wf = wave.open('out.wav', "rb")


    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        sys.exit(1)

    model = Model("model/vosk-model-small-es-0.42")

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    #rec.SetPartialWords(True)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        rec.AcceptWaveform(data)

    resp = json.loads(rec.FinalResult())

    return resp['text']
