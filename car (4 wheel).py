# -*- coding: utf-8 -*-

#导入gpio的模块
import RPi.GPIO as GPIO
import time
#import keys
 
#设置gpio口的模式
GPIO.setmode(GPIO.BOARD)
 
#定义信号接口gpio口
INT1 = 31
INT2 = 33
INT3 = 35
INT4 = 37 # back wheel

INT5 = 7
INT6 = 11
INT7 = 13
INT8 = 15
#设置gpio口为输出
GPIO.setup(INT1,GPIO.OUT)
GPIO.setup(INT2,GPIO.OUT)
GPIO.setup(INT3,GPIO.OUT)
GPIO.setup(INT4,GPIO.OUT)
GPIO.setup(INT5,GPIO.OUT)
GPIO.setup(INT6,GPIO.OUT)
GPIO.setup(INT7,GPIO.OUT)
GPIO.setup(INT8,GPIO.OUT)
GPIO.output(INT1,False)
GPIO.output(INT2,False)
GPIO.output(INT3,False)
GPIO.output(INT4,False)
GPIO.output(INT5,False)
GPIO.output(INT6,False)
GPIO.output(INT7,False)
GPIO.output(INT8,False)

def stop ():
    GPIO.output(INT1,False)
    GPIO.output(INT2,False)
    GPIO.output(INT3,False)
    GPIO.output(INT4,False)
    GPIO.output(INT5,False)
    GPIO.output(INT6,False)
    GPIO.output(INT7,False)
    GPIO.output(INT8,False)

def run ():
    GPIO.output(INT1,GPIO.LOW)
    GPIO.output(INT2,GPIO.HIGH)
    GPIO.output(INT3,GPIO.HIGH)
    GPIO.output(INT4,GPIO.LOW)
    GPIO.output(INT5,GPIO.HIGH)
    GPIO.output(INT6,GPIO.LOW)
    GPIO.output(INT7,GPIO.LOW)
    GPIO.output(INT8,GPIO.HIGH)





def back ():
    GPIO.output(INT1,GPIO.HIGH)
    GPIO.output(INT2,GPIO.LOW)
    GPIO.output(INT3,GPIO.LOW)
    GPIO.output(INT4,GPIO.HIGH)
    GPIO.output(INT5,GPIO.LOW)
    GPIO.output(INT6,GPIO.HIGH)
    GPIO.output(INT7,GPIO.HIGH)
    GPIO.output(INT8,GPIO.LOW)
    
    
def left ():
    GPIO.output(INT1,GPIO.LOW)
    GPIO.output(INT2,GPIO.HIGH)
    GPIO.output(INT3,False)
    GPIO.output(INT4,False)
    GPIO.output(INT5,GPIO.HIGH)
    GPIO.output(INT6,GPIO.LOW)
    GPIO.output(INT7,False)
    GPIO.output(INT8,False)
    
    
def right ():
    GPIO.output(INT1,False)
    GPIO.output(INT2,False)
    GPIO.output(INT3,GPIO.HIGH)
    GPIO.output(INT4,GPIO.LOW)
    GPIO.output(INT5,False)
    GPIO.output(INT6,False)
    GPIO.output(INT7,GPIO.LOW)
    GPIO.output(INT8,GPIO.HIGH)








touch = input (" : ") #reading keyboard


while (touch != "o"):
    touch = input(" : ")
    if (touch == "w"):
         run ()
    elif (touch == "s"):
        back ()
    elif (touch == "o"):
        stop ()
        GPIO.cleanup ()
    elif (touch == "a"):
        left ()
        time.sleep (1)
        stop ()
    elif (touch == "d"):
        right ()
        time.sleep (1)
        stop ()
    else:
        stop ()
