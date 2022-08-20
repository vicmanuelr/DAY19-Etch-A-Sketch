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
    tim.setheading(current_heading + 5)


def counter_clock():
    current_heading = tim.heading()
    tim.setheading(current_heading - 5)


screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=counter_clock, key="a")

screen.exitonclick()