# Pentagon
import turtle
mary = turtle.Turtle()
mycolor = "purple"
go = 100
turn = 72
sides = [1, 2, 3, 4, 5]
mary.color(mycolor)
for side in sides:
    mary.forward(go)
    mary.right(turn)

# Rainbow pentagon
import turtle
terry = turtle.Turtle()
terry.width(10)
rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]
terry.penup()
terry.back(80)
terry.pendown()
for mycolor in rainbow:
    terry.color(mycolor)
    terry.forward(50)
    terry.right(60)
