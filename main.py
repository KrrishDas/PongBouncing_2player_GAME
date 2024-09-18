from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

Rpaddle = Paddle(x=350, y=0)
Lpaddle = Paddle(x=-350, y=0)
ball = Ball()
score_r = Scoreboard(175, 240)
score_l = Scoreboard(-175, 240)
t=0.1


screen.listen()
screen.onkey(key="Up", fun=Rpaddle.Up)
screen.onkey(key="Down", fun=Rpaddle.Down)
screen.onkey(key="w", fun=Lpaddle.Up)
screen.onkey(key="s", fun=Lpaddle.Down)

game_is_on = True
while game_is_on:

   screen.update()
   time.sleep(t)
   ball.move()

   ball_hit_paddle = False

   # detecting collision of ball with top and bottom walls
   if ball.xcor() >= 0:
      if ball.ycor() >= 270 or ball.ycor() <=-270:
         ball_hit_paddle = True
         ball.bounce_y()
   elif ball.xcor() < 0:
      if ball.ycor() >= 270 or ball.ycor() <= -270:
         ball_hit_paddle = True
         ball.bounce_y()

   # detecting collision with paddle

   if ball.distance(Rpaddle) <= 40 and ball.xcor() >= 320:
      ball.bounce_x()
      t *= 0.8
   elif ball.distance(Lpaddle) <= 40 and ball.xcor() <= -320:
      ball.bounce_x()
      t *= 0.8

   #detecting if ball goes out of bounds
   if ball_hit_paddle == False:
      if ball.xcor() > 380:
         score_l.inc_score()
         ball.goto(0,0)
         ball.bounce_x()
         time.sleep(0.5)
         t = 0.1
      elif ball.xcor() < -380:
         score_r.inc_score()
         ball.goto(0,0)
         time.sleep(0.5)
         ball.bounce_x()
         t = 0.1

   if score_l.score == 10 or score_r.score == 10:
      break

score_r.game_over()
screen.exitonclick()