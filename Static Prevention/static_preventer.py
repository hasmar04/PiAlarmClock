import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.OUT)
print("Startup Complete")

while 1:
    fh=open("/proc/asound/card1/pcm0p/sub0/status","r") # replace 1 in card1 with number from aplay -l
    sound = fh.read()
    sound = sound.strip()
    fh.close()
    if (sound == "closed"):
        GPIO.output(20,GPIO.LOW)
    else:
        GPIO.output(20,GPIO.HIGH)
