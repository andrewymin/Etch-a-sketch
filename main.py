from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def clear_screen():
    tim.speed("fastest")
    tim.home()
    tim.clear()
    tim.speed("normal")


screen.onkeypress(fun=move_forwards, key="w")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeypress(fun=move_left, key="a")
screen.onkeypress(fun=move_right, key="d")
screen.onkeypress(fun=clear_screen, key="c")
screen.listen()
screen.exitonclick()
