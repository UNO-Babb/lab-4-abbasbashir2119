import turtle

# Function to draw a square
def drawSquare(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Function to fill a corner with a smaller square
def fillCorner(alice, corner):
    # Draw big square
    drawSquare(alice, 100)

    if corner == 1:
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()

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
