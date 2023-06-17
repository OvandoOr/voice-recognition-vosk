import serial
from voice_recognition import voice_recognition, ini_voice_recognition, end_voice_recognition


# Configurar la conexión serial con Arduino
arduino_port = 'COM3'  # Reemplaza 'COM8' por el puerto serial adecuado
arduino_baudrate = 9600
ser = serial.Serial(arduino_port, arduino_baudrate)
list_adelante = ['adelante', 'de', 'delante']
list_atras = ['atrás', 'tras']
list_izquierda = ['izquierda', 'quisiera', 'izquierdo']
list_derecha = ['derecha', 'hecha', 'derecho']

stream, p, rec = ini_voice_recognition()

while True:
    print('Comience a hablar:')
    ser.write(b'O')
    command = ''
    word = voice_recognition(stream, rec)
    if word != "":
        print(word)
        command = word
    if word == "terminar":
        break
    else:
        command = last_command

    # Controlar los LEDs según los datos filtrados de voz
    if command in list_adelante:
        ser.write(b'S')
        last_command = 'adelante'
        ser.write(b'T')
    elif command in list_atras:
        ser.write(b'B')
        last_command = 'atrás'
        ser.write(b'T')
    elif command in list_izquierda:
        ser.write(b'L')
        last_command = 'izquierda'
        ser.write(b'T')
    elif command in list_derecha:
        ser.write(b'R')
        last_command = 'derecha'
        ser.write(b'T')
    else:
        ser.write(b'Q')
        last_command = 'alto'
        ser.write(b'T')

end_voice_recognition(stream, p)
ser.close()