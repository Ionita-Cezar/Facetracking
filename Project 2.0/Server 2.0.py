#Raspberry Pi

import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Set pins 11 & 12 as outputs, and define as PWM servo1 & servo2
GPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11, 50)  # pin 11 for servo1
GPIO.setup(15, GPIO.OUT)
servo2 = GPIO.PWM(15, 50)  # pin 12 for servo2

# Start PWM running on both servos, value of 0 (pulse off)
servo1.start(0)
servo2.start(0)
servo1.ChangeDutyCycle(7)
servo2.ChangeDutyCycle(2)
time.sleep(0.1)
servo1.ChangeDutyCycle(0)
servo2.ChangeDutyCycle(0)
consecutiv = 0
counter1 = 7
counter2 = 7

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    HOST = 'xxx.xxx.xxx.xx'
    PORT = xxxxx
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print ("Waiting connection")

    with conn:
        print("Server is connected")
        while True:
            data = conn.recv(2048).decode('utf-8')
            if data:
                print(data)
                x, y = data.split(",")
                print(x)
                print(y)

                if float(x) != 320 and float(y) != 240:
                    if float(x) > 10 and float(x) <= 40:
                        counter1=min(counter1+0.1, 12)
                    else:
                        if float(x) <-10 and float(x) >= -40:
                            counter1=max(counter1-0.1, 2)
                        else:
                            if float(x) > 40:
                                counter1=min(counter1+0.3, 12)
                            else:
                                counter1=max(counter1-0.3, 2)

                    servo1.ChangeDutyCycle(counter1)
                    time.sleep(0.05)
                    servo1.ChangeDutyCycle(0)

                    if float(y) > 10 and float(y) <=-20:
                        counter2=min(counter2+0.05, 10)
                    else:
                        if float(y) <-10 and float(y) >= -20:
                            counter2=max(counter2-0.05, 7)
                        else:
                            if float(y) > 20:
                                counter2=min(counter2+0.2, 10)
                            else:
                                counter2=max(counter2+0.2, 7)

                    servo2.ChangeDutyCycle(counter2)
                    time.sleep(0.05)
                    servo2.ChangeDutyCycle(0)
                    consecutiv=0

                else:
                    if (float(x) == 320 and float(y) == 240 and consecutiv != 15):
                        consecutiv += 1
                    else:
                        servo1.ChangeDutyCycle(7)
                        time.sleep(0.1)
                        servo1.ChangeDutyCycle(0)
                        counter1 = 7
                        servo2.ChangeDutyCycle(7)
                        time.sleep(0.1)
                        servo2.ChangeDutyCycle(0)
                        counter2 = 7
                        consecutiv = 0
                    print("No face detected")

servo1.stop()
servo2.stop()
GPIO.cleanup()
