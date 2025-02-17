import turtle

# Function to draw a square
def drawSquare(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Function to fill a corner with a smaller square
def fillCorner(george, corner):
    # Draw big square
    drawSquare(george, 100)

    if corner == 1:
        george.begin_fill()
        drawSquare(george, 50)
        george.end_fill()
    elif corner == 2:
        george.forward(50)
        george.begin_fill()
        drawSquare(george, 50)
        george.end_fill()

# Main function
def main():
    myTurtle = turtle.Turtle()
    
    # Draw the main square
    drawSquare(myTurtle, 100)
    
    # Fill the top-right corner with a smaller square
    fillCorner(myTurtle, 1)

    myTurtle.hideturtle()
    turtle.done()

# Run the main function
main()
