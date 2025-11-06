import turtle

# Create a turtle object
t = turtle.Turtle()
t.shape("maxresdefaul.jpg") # Optional: change the turtle's shape for better visibility
t.penup() # Lift the pen so it doesn't draw while dragging

# Define the drag handler function
def drag_handler(x, y):
    t.ondrag(None)  # Disable dragging during the move
    t.goto(x, y)    # Move the turtle to the new mouse position
    t.ondrag(drag_handler) # Re-enable dragging

# Bind the drag handler to the turtle
t.ondrag(drag_handler)

# Keep the window open
turtle.done()