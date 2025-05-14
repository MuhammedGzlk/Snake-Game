from turtle import Screen
from A_PROJECT_Intermediate.New_Snake_Game.others.snake import Snake_S
from A_PROJECT_Intermediate.New_Snake_Game.others.food import Food
from A_PROJECT_Intermediate.New_Snake_Game.Data.score import Scoreboard
from A_PROJECT_Intermediate.New_Snake_Game.Data.high_score_manager import HighScoreManager
from A_PROJECT_Intermediate.New_Snake_Game.GUII.get_username_gui import get_username
import time
import random

FODS = ['normal', 'speed', 'bonus']

username = get_username()
if not username:
    exit()

manager = HighScoreManager()
user_high_score = manager.get_high_score(username)

window = Screen()
window.setup(height=600, width=600)
window.title('NEW SNAKE')
window.bgcolor('green')
window.tracer(0)

snake = Snake_S()
food = Food('normal')
scoreboard = Scoreboard(username, user_high_score)

window.listen()
window.onkey(snake.up, 'w')
window.onkey(snake.down, 's')
window.onkey(snake.right, 'd')
window.onkey(snake.left, 'a')

game_is_on = True
while game_is_on:
    window.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        food.hideturtle()
        food.clear()
        food_type = random.choice(FODS) if scoreboard.get_score() > 2 else 'normal'
        food = Food(food_type)
        snake.extend()

        if food_type == 'speed':
            snake.speed_up()
            scoreboard.increase_score()
            snake.extend()

        elif food_type == 'bonus':
            scoreboard.increase_bonus_score()
            snake.extend()
        else:
            scoreboard.increase_score()
            snake.extend()

    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        snake.wrap_around(600, 600)

    if snake.check_self_collision():
        scoreboard.game_over()
        manager.update_score(username, scoreboard.get_score())
        game_is_on = False

window.exitonclick()
