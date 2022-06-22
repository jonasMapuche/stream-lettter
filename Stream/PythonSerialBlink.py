
import serial
import time

while True:
    try: 
        arduino = serial.Serial('COM10', 9600)
        print('Arduino connected...')
        break
    except:
        pass

while True:
    cmd = input('Write "s" for start or "d" for disable: ')
    if cmd == 's' or cmd == 'd':  
        if cmd == 's':
            cmd = cmd + "\n"
            arduino.write(cmd.encode())
        elif cmd == 'd':
            cmd = cmd + "\n"
            arduino.write(cmd.encode())
        msg = arduino.readline().decode('utf-8').rstrip()
        print(msg)
    else: 
        print('Letra invalida')
    time.sleep(1)