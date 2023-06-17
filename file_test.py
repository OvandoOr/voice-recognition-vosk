from voice_recognition import voice_recognition

for index in range(1, 34):
    file = 'audio/test (' + str(index) + ').mp4'   
    print (file, voice_recognition(file))