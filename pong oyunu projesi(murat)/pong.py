import time
from turtle import Screen
from paddle import paddle

# Ekranı oluştur
Screen = Screen()
Screen.setup(width=800, height=600)
Screen.bgcolor("black")
Screen.title("pong oyunu")
screen.tracer(0)

# Nesneleri oluştur
r_paddle = paddle(350, 0))
l_paddle = paddle(-350, 0))
ball = ball()
scoreboard = scoreboard

# Kontroller
Screen.listen()
Screen.onkeypress(r_paddle.up"Up")
Screen.onkeypress(r_paddle.down,"Down")\
screen.onkeypress(l_paddle.up,"w")
Screen.onkeypress()l_paddle.down,"s")

# Oyun döngüsü
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    Screen.update()
    ball.move()

# üst alt kenarlardan sekme
if ball.ycor() > 280 or
ball.ycor() < -280:
        ball.bounce_y()

#paddle çarpışması
if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(1_paddle) < 50 and ball.xcor() < -320):
ball.bounce_x()

# sağ paddle kaçırdı
if ball.xcor() > 380:
      ball.reset_position()
      scoreboard.1_point()

# sol paddle kaçırdı
if ball.xcor() < -380:
      ball.reset_position()
      scoreboard.r_position()

#kazanan kontrolü
if scoreboard.1_score == 5 or
scoreboard.r_score == 5:
game_is_on = False
scoreboard.game_over()

Screen.exitonclick()

from turtle import turtles

class paddle(Turtle)
      def__init__(self, position)
    super().__init__()
self.shape("square")
self.color("white")
self.shasepize(stretch_wid=5 stretch_len=1)
self.penup()
self.goto(position)
  def up(self):
      if self.ycor() < 250:
           self.goto(self.xcor()
                     self.ycor() + 20)
           def down(self):
        if self.ycor() > -240
      self.goto(self.xcor()self.ycor() - 20)

      from turtle import Turtle

class ball(Turtle):
     def__init__(self):
     super().__init__()
     self.shape("circle")
     self.color("white")
     self.penup()
     self.x_move = 10
     self.y_move = 10
     self.move_speed = 0.05

     def move (self):
          new_x = self xcor() + self.x_move
          new_y = self.ycor() + self.y_move
          self.goto(new_x, new_x)
          def bounce_y(self):
self.y_move *= -1

def bounce_x(self):
     self.x_move *= 0.9
     hızlan
     def reset-possition(self):
     self.goto(0, 0)
     self.move_speed = 0.05
     self.bounce_x()

from turtle import Turtle

class scorboard(turtle):
     def__init__(self):
     super().__init__()
     self.color("white")
     self.hideturtle()
    self.l_ score = 0
    self.r_ score = 0
    self.update_scorboard()

def update_scorboard(self):
     self.clear()
     self.goto(-100, 230)
     self.write(self.l_score align= "center",font=("courier"  50,"normal"))
     self.goto(-100, 23*)
     self.write(self.r_score,align="center", font=("courrier",50,"normal"))
     def1_point(self):
     self.l_score +=1
     self.update_scorboard()
     def r.point(self):
self.r_score += 1
self.update_scorboard()

def game_over(self):
     self.goto(0, 0)
     winner = "sol" if
self.l_score = 5 else "sağ"
self.write(f"(winner)"oyuncu kazandı)! , align="center"
font=("courier", 24 "bold"))