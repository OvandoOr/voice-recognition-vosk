from voice_recognition import voice_recognition, ini_voice_recognition, end_voice_recognition

stream, p, rec = ini_voice_recognition()

while True:
    word = voice_recognition(stream, rec)
    if word != "":
        print(word)
    if word == "terminar":
        break

end_voice_recognition(stream, p)