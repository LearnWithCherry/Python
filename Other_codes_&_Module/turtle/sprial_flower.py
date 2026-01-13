import turtle
import colorsys

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🌸 Spiral Flower - Python Art")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest
pen.width(2)
pen.hideturtle()

# Colors setup
hue = 0
n = 36  # Number of petals
colors = [colorsys.hsv_to_rgb(hue + i/n, 1, 1) for i in range(n)]

# Convert RGB float to turtle color
colors = [(r, g, b) for r, g, b in colors]
screen.colormode(1.0)

# Draw the flower
for i in range(360):
    pen.color(colors[i % n])
    pen.forward(i * 3 / n + i)
    pen.left(59)
    pen.forward(i * 3 / n + i)
    pen.left(60)

# Keep window open
turtle.done()
