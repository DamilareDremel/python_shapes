# Draw square, pentagon, octagon
import turtle
jack = turtle.Turtle()

def shape(sides, length, color, width):
    jack.color(color)
    jack.width(width)
    jack.speed(0)
    for side in range(sides):
        jack.forward(length)
        jack.right(360/sides)

jack.penup()
jack.back(130)
jack.pendown()
shape(4, 20, "cyan", 5)
jack.penup()
jack.forward(50)
jack.pendown()
shape(6, 20, "red", 7)
jack.penup()
jack.forward(70)
jack.pendown()
shape(8, 20, "yellow", 10)
