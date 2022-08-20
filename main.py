from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def clockwise():
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)


def counter_clock():
    current_heading = tim.heading()
    tim.setheading(current_heading - 10)


def clear():
    screen.reset()


screen.onkeypress(fun=forward, key="w")
screen.onkeypress(fun=backward, key="s")
screen.onkeypress(fun=clockwise, key="d")
screen.onkeypress(fun=counter_clock, key="a")
screen.onkeypress(fun=clear, key="c")

screen.exitonclick()