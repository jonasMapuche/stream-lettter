import serial
import time

while True:
    try: 
        arduino = serial.Serial('COM10', 9600)
        print('Arduino connected...')
        break
    except:
        pass

while (1):
    arduino.write(b"Hello from Raspberry Pi!\n")
    line = arduino.readline().decode('utf-8').rstrip()
    print(line)
    time.sleep(1)
