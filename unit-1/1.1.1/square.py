import turtle as trtl


def draw_square(size: int, painter: trtl.Turtle, color: str = "black"):
    painter.pencolor(color)
    for i in range(4):
        painter.forward(size)
        painter.right(90)


painter = trtl.Turtle()
draw_square(150, painter)

wn = trtl.Screen()
wn.mainloop()