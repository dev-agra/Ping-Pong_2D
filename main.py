from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
from lines import Line

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Ping Pong 1990")
screen.tracer(0)

rpaddle = Paddle((373, 10))
pong = Ball()
score = Scoreboard()
lines = Line()
lpaddle = Paddle((-380, 10))

screen.listen()
screen.onkey(rpaddle.up, "Up")
screen.onkey(rpaddle.down, "Down")
screen.onkey(lpaddle.up, "w")
screen.onkey(lpaddle.down, "s")

is_on = True
while is_on:
    time.sleep(pong.speed)
    screen.update()
    pong.move()

    # Detecting Collision with the wall
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()

    # Detecting Collision with Paddle
    if pong.distance(rpaddle) < 50 and pong.xcor() > 340:
        pong.bounce_x()

    elif pong.distance(lpaddle) < 50 and pong.xcor() < -340:
        pong.bounce_x()

    # Detect if the R Paddle misses
    if pong.xcor() > 380:
        pong.reset_position()
        score.left_score()

    # Detect if the L Paddle misses
    if pong.xcor() < -380:
        pong.reset_position()
        score.right_score()
screen.exitonclick()
