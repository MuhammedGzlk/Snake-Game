from turtle import Screen , Turtle
from snake import Snake
from food import Food
from score_bord import Score
import time

screen =Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game ')
screen.tracer(0)

snake = Snake()
food =Food()
point= Score()

screen.listen()
screen.onkey(snake.up,'w')
screen.onkey(snake.down,'s')
screen.onkey(snake.right,'d')
screen.onkey(snake.left,'a')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        point.increase_score()

    if snake.head.xcor()>288 or snake.head.xcor()< -288 or snake.head.ycor()< -288 or snake.head.ycor()> 288:
        game_is_on = False
        point.game_over()

    for segment in snake.segment:

        if segment == snake.head:
            pass
        elif snake.head.distance(segment)< 10:
            game_is_on = False
            point.game_over()
screen.exitonclick()