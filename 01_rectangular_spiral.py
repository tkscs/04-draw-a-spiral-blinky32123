import turtle

"""
Make a rectangular spiral (see the README.md for an example)
"""

### YOUR CODE STARTS HERE
x = 40
for i in range(1, 10):
    turtle.forward(x*1)
    turtle.right(90)
    turtle.forward(x*1.5)
    turtle.right(90)
    x = x - 5
### YOUR CODE ENDS HERE

turtle.exitonclick()