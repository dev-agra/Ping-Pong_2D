from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.shape('square')
        self.shapesize(stretch_wid=30, stretch_len=0.1)
