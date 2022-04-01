from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.shape('circle')
        self.goto(0, 0)
        self.penup()
        self.x_move = 11
        self.y_move = 11
        self.speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed *= 0.9

    def reset_position(self):
        self.speed = 0.1
        self.goto(x=0, y=0)
