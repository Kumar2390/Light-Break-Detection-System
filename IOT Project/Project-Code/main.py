import machine 
from machine import Pin,I2C
from utime import sleep,time
from ssd1306 import SSD1306_I2C

width = 128
height = 64

led = Pin(1,Pin.OUT)
buzzer=Pin(0,Pin.OUT)
i2c = I2C(0,scl = Pin(17), sda = Pin(16), freq=100000)
addr = i2c.scan()[0]
oled = SSD1306_I2C(width,height,i2c,addr)
#oled.poweron()

beam_pin = Pin(15, Pin.IN, Pin.PULL_UP)
old_beam_value = beam_pin.value()
count=0
while True:
    if old_beam_value != beam_pin.value():
        old_beam_value =  old_beam_value
        #print(old_beam_value)
        buzzer.value(1)
        led.value(1)
        sleep(1)
        buzzer.value(0)
        led.value(0)
        oled.text("WELCOME",20,5)
        oled.text("Choor agya",30,14)
        #if old_beam_value==true:
        count=count+1
        oled.text(str(count),30,28)
        oled.show()
        oled.fill(0)
    #time.sleep(0.1)