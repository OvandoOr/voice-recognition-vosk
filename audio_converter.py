from voiceExample import voice_recognition

for index in range(1, 12):
    file = 'audio/' + str(index) + '.mp4'   
    print (file, voice_recognition(file))