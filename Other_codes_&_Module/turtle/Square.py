import turtle

# Create a turtle object
t = turtle.Turtle()

# Set speed (1 to 10 or "fastest")
t.speed(2)

# Draw a square
for _ in range(8):
    t.forward(100)  # move forward 100 pixels
    t.right(90)     # turn right 90 degrees

# Keep window open
turtle.done()
