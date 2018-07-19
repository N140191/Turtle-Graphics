import turtle
from turtle import *
import math
sh=turtle.Turtle()
sh.color("red","yellow")
sh.begin_fill()
sh.speed(190)
for i in range(2905):
    sh.speed(190)
    sh.forward(10)
    sh.left(math.sin(i/10)*26)
    sh.left(20)
sh.end_fill()
turtle.done()
