import serial
import RPi.GPIO as GPIO
import os,time
os.system('sudo chmod -R ugo+rw /dev/ttyS0')

GPIO.setmode(GPIO.BOARD)

port=serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

port.write(str.encode('AT'+'\r'))
rcv =port.read(10)
print(rcv)
time.sleep(1)

port.write(str.encode('ATE0'+'\r'))
rcv= port.read(10)
print(rcv)
time.sleep(1)


port.write(str.encode('AT + CMGF =1'+'\r'))
rcv= port.read(10)
print(rcv)
time.sleep(1)

port.write(str.encode('AT + CNMI=2,1,0,0,0'+'\r'))
rcv= port.read(10)
print(rcv)
time.sleep(1)

port.write(str.encode('AT+CMGS="9723581176"'+'\r'))
rcv= port.read(10)
print(rcv)
time.sleep(1)

port.write(str.encode('Hello user'+'\r'))
rcv= port.read(10)
print(rcv)
time.sleep(1)

port.write(str.encode("\x1A"+'\r'))

for i in range(10):
    rcv=port.read(10)
    print(rcv)
