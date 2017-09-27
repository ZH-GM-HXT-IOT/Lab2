import machine
import time
from machine import PWM, Pin

act_flag = 0

def my_callback(p):
    interrupt_state = machine.disable_irq()
    global act_flag
    if (act_flag == 0):
        act_flag = 1
    else:
        act_flag = 0

    time.sleep_ms(500)
    
    
    machine.enable_irq(interrupt_state)
    return

#############init##########################3
adc=machine.ADC(0)                #adc 
pwm1=PWM(machine.Pin(13))         #pwm
pwm2=PWM(machine.Pin(15))         
pwm1.freq(60)
pwm2.freq(60)

p2 = Pin(2, Pin.IN)               #interrupt       
p2.irq(trigger=Pin.IRQ_FALLING|Pin.IRQ_RISING, handler=my_callback)




while(1):
    #print (act_flag)
    #time.sleep_ms(500)
    if (act_flag == 1):
        sen=adc.read()
        pwm1.duty(sen)
        pwm2.duty(sen)


