from turtle import *

def rectangle(width, height):
    for i in range(0,2):
        sarah.forward(width)
        sarah.right(90)
        sarah.forward(height)
        sarah.right(90)

def triangle(length):
    for i in range(0,3):
        sarah.forward(length)
        sarah.left(120)
    
def house_boat(width, height):
    triangle(height)
    rectangle(height, height)
    sarah.right(90)
    sarah.forward(height)
    sarah.left(90)
    sarah.penup()
    sarah.back(abs(width/2-height/2))
    sarah.pendown()
    rectangle(width, height/2)

sarah = Turtle()
sarah.color("red")
canvas = Screen()
canvas.setup(700,700)
house_boat(250, 100)
canvas.exitonclick()