import serial
import time

while True:
    try: 
        arduino = serial.Serial('COM10', 115200)
        print('Arduino connected...')
        break
    except:
        pass

while True:
    msg = str(arduino.readline().decode('utf-8').rstrip())
    print(msg)
    time.sleep(1)
