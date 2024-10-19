from basics import arc, deg2rad
import turtle
from math import sin
from facial_features import *
from turtle import *

turtle.colormode(255)

# turtle.tracer(0)
# face()
turtle.bgcolor(254, 222, 0)
turtle.tracer(2)

def draw():        
    eyebrow('r')
    eyebrow('l')
    eye('third')
    eye('left')    
    eye('right')
    bindi()
    nose()
    smile()
    
try:
    
    draw()
    
    turtle.done()
    turtle.bye()
    
    
    
    
except Exception as e:
    print(e)