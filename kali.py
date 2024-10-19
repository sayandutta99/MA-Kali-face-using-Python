from basic import arc, deg2rad
import turtle
from math import sin
from facial import *
from turtle import *

turtle.colormode(255)

# turtle.tracer(0)
# face()
# turtle.screensize(canvwidth=1000, canvheight=300)
turtle.bgcolor(60,80,110)
turtle.tracer(2)

def draw():        
    eyebrow('r', R1 = 300, a1 = 60, a2 = 85, R2 = 260)
    eyebrow('l', R1 = 300, a1 = 60, a2 = 85, R2 = 260)
    eye('third', R11 = 160, a11 = 90, a12 = 105, a13 = 130, a21 = 90, a22 = 100, a23 = 115, offset = 2, r = 42)
    eye('left', R11 = 160, a11 = 90, a12 = 105, a13 = 130, a21 = 90, a22 = 100, a23 = 115, offset = 2, r = 42)    
    eye('right', R11 = 160, a11 = 90, a12 = 105, a13 = 130, a21 = 90, a22 = 100, a23 = 115, offset = 2, r = 42)
    bindi2()
    nose(l = 170, which = 'kali')
    mouth(l = 170)
    
    
try:
    
    draw()
    
    turtle.done()
    turtle.bye()
    
    
    
    
except Exception as e:
    print(e)