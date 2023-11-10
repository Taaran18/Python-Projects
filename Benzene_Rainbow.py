import turtle

# Define a list of colors
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# Create a turtle object
t = turtle.Pen()

# Set the background color to black
turtle.bgcolor("black")

# Loop to draw a colorful pattern
for x in range(360):
    # Set the pen color based on the current iteration
    t.pencolor(colors[x % 6])

    # Set the pen width based on the current iteration
    t.width(x / 100 + 1)

    # Move the turtle forward by the current iteration value
    t.forward(x)

    # Turn the turtle left by 59 degrees
    t.left(59)

# Keep the window open until the user closes it
turtle.done()