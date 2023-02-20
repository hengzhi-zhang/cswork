# File: PanamaFlag.py
# Student: Hengzhi Zhang
# UT EID: hz6984
# Course Name: CS303E
#
# Date: 11/17/2021
# Description of Program: This program utilizes Python Turtle graphics to draw a complete map of Panama.
myBlue = (0, 32, 91)
myRed = (191, 13, 62)
white = (255, 255, 255)
import turtle

def drawRectangle ( ttl , x , y , length, width ):

    ttl . penup () # raise the pen
    ttl . goto (x,y) # move to starting position
    ttl . setheading (0) # point turtle east
    ttl . pendown () # lower the pen
    ttl . forward ( length ) # move forward length ;
    ttl . right (90) # turn right 90 degrees
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(length)
    ttl.right(90)
    ttl.forward(width)
    ttl . penup () # raise the pen

def drawStar (ttl, x, y, size):

    ttl.penup()
    ttl.goto(x,y)
    ttl.setheading(0)
    ttl.pendown()
    for x in range(5):
        ttl.forward(size)
        ttl.right(144)
        ttl.forward(size)
        ttl.left(72)
    ttl.penup()


if __name__ == '__main__':

    Bob = turtle.Turtle()
    Bob.speed(10)
    Bob.pensize(.1)
    Bob.pencolor("black")
    Bob.screen.colormode(255)

    Bob.fillcolor(white)
    Bob.begin_fill()
    drawRectangle ( Bob , -350, 200, 300, 200 )
    Bob.end_fill()

    Bob.fillcolor(myRed)
    Bob.begin_fill()
    drawRectangle(Bob, -50, 200, 300, 200)
    Bob.end_fill()

    Bob.fillcolor(white)
    Bob.begin_fill()
    drawRectangle(Bob, -50, 0, 300, 200)
    Bob.end_fill()

    Bob.fillcolor(myBlue)
    Bob.begin_fill()
    drawRectangle(Bob, -350, 0, 300, 200)
    Bob.end_fill()

    Bob.pencolor(myBlue)
    Bob.fillcolor(myBlue)
    Bob.begin_fill()
    drawStar(Bob, -200, 115, 40)
    Bob.end_fill()

    Bob.pencolor(myRed)
    Bob.fillcolor(myRed)
    Bob.begin_fill()
    drawStar(Bob, 110, -85, 40)
    Bob.end_fill()

    turtle.done()