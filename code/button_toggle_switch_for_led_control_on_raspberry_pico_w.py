from machine import Pin
from time import sleep

ledpin = 15
myled = Pin(ledpin, Pin.OUT)

butpin = 14
mybutton = Pin(butpin, Pin.IN, Pin.PULL_UP)
butoldstate = 1
butnewstate = 1
ledstate = False

while True:
    butnewstate = mybutton.value()
    if(butnewstate == 1 and butoldstate == 0):
        ledstate = not ledstate
        myled.value(ledstate)
    print(ledstate, butnewstate)
    butoldstate = butnewstate
    sleep(.1)