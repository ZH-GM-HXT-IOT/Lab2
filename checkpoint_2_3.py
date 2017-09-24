from machine import Pin
import machine
import time

def my_callback(p):
    interrupt_state = machine.disable_irq()
    print('in interrupt')
    time.sleep_ms(800)
    print(11111)
    machine.enable_irq(interrupt_state)
    return

p2 = Pin(2, Pin.IN)
p2.irq(trigger=Pin.IRQ_FALLING|Pin.IRQ_RISING, handler=my_callback)
