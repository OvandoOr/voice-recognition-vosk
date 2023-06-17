import json
import pyaudio
from vosk import Model, KaldiRecognizer, SetLogLevel

chunk = 8192  # Tamaño del fragmento de audio
formato = pyaudio.paInt16  # Formato de los datos de audio
canales = 1  # Número de canales (mono)
rate = 16000  # Tasa de muestreo en Hz


def voice_recognition():

    p = pyaudio.PyAudio()

    # Configurar el micrófono como fuente de audio
    stream = p.open(format=formato,
                    channels=canales,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    stream.start_stream()
    # Grabar audio durante 2 segundos
    print("Grabando...")
    data = stream.read(chunk*2)
    print("Grabación finalizada.")
    word = ""

    SetLogLevel(0)
    
    model = Model("model/vosk-model-small-es-0.42")
    rec = KaldiRecognizer(model, rate)
    rec.SetWords(True)

    
    rec.AcceptWaveform(data)
    resp = json.loads(rec.FinalResult())

    word = resp['text']

    stream.stop_stream()
    stream.close()
    p.terminate()

    p = pyaudio.PyAudio()

    # Open a .Stream object to write the WAV file to
    # 'output = True' indicates that the sound will be played rather than recorded
    stream = p.open(format=formato,
                    channels=canales,
                    rate=rate,
                    output = True)

    # Play the sound by writing the audio data to the stream
    
    stream.write(data)

    # Close and terminate the stream
    stream.close()
    p.terminate()

    return word
