import json
import pyaudio
from vosk import Model, KaldiRecognizer, SetLogLevel

chunk = 8192  # Tamaño del fragmento de audio
formato = pyaudio.paInt16  # Formato de los datos de audio
canales = 1  # Número de canales (mono)
rate = 16000  # Tasa de muestreo en Hz



def voice_recognition(stream, rec):
    # Grabar audio durante 2 segundos
    #print("Grabando...")
    data = stream.read(chunk*2)
    #print("Grabación finalizada.")
    word = ""
    rec.AcceptWaveform(data)
    resp = json.loads(rec.FinalResult())
    #print(resp)
    word = resp['text']

    return word

def ini_voice_recognition():
    SetLogLevel(-1)
    model = Model("model/vosk-model-small-es-0.42")
    rec = KaldiRecognizer(model, rate)
    rec.SetWords(True)
    p = pyaudio.PyAudio()

    # Configurar el micrófono como fuente de audio
    stream = p.open(format=formato,
                    channels=canales,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)
    stream.start_stream()
    return stream, p, rec

def end_voice_recognition(stream, p):
    stream.stop_stream()
    stream.close()
    p.terminate()
