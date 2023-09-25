import RPi.GPIO as GPIO
import time

buzzer = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setwarnings(False)

pwm = GPIO.PWM(buzzer, 1.0)


scale = [262, 294, 330, 349, 392, 440, 494, 523]

def y():
    pwm.start(50.0)
    
    pwm.ChangerFrequency(scale[0])
    time.sleep(1.0)
    
    pwm.ChangerFrequency(scale[2])
    time.sleep(1.0)
    
    pwm.ChangerFrequency(scale[4])
    time.sleep(1.0)
    
    pwm.ChangerFrequency(scale[7])
    time.sleep(1.0)
    
    pwm.stop()
    
def n():
    pwm.ChangerFrequency(311)
    time.sleep(1.0)
    
    pwm.stop()

GPIO.cleanup()
