import turtle
import colorsys

# Create turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
t = turtle.Turtle()
t.speed(0)  # fastest
turtle.colormode(255)
t.width(3.258)

# Set color mode
hue = 0.015


# Draw flower
for i in range(420):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(int(color[0]*255), int(color[1]*255), int(color[2]*255))
    t.forward(i * 1)
    t.left(150)
    t.forward(i * 1)
    t.left(110)
    t.forward(i * 1)
    t.left(150)
    t.forward(i * 1)
    t.left(110)
    hue += 0.015

t.hideturtle()
turtle.done()
