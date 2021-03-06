import os
import RPi.GPIO as GPIO
import time
 

GPIO.setmode(GPIO.BCM)
 

GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
   
    GPIO.output(GPIO_TRIGGER, True)
 
    
    time.sleep(0.0002)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
  
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
  
    TimeElapsed = StopTime - StartTime

    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
            if dist<=50:
                os.system("fswebcam -F 3 image.jpg")
            else:
                print("shouldnt take pic")
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
                



