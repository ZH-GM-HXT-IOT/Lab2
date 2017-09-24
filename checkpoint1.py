import machine
import time
from machine import PWM, Pin
adc=machine.ADC(0)
pwm1=PWM(machine.Pin(13))
pwm2=PWM(machine.Pin(15))

pwm1.freq(60)
pwm2.freq(60)
while(1):
    sen=adc.read()
    pwm1.duty(sen)
    pwm2.duty(sen)
 
