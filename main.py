
import turtle
from turtle import *


turtle.penup()
turtle.setpos(-250,-250)
import random
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def string():
    bruh = random.choice(color_list)
    color = (rgb_to_hex(bruh[0],bruh[1],bruh[2]))
    return color
value = -200
for _ in range(10):
    for _ in range(10):
        turtle.dot(20, string())
        turtle.penup()
        turtle.forward(50)
    turtle.setpos(-250,value)
    value +=50

screen = Screen()
screen.title('Hirst Painting')
screen.exitonclick()
