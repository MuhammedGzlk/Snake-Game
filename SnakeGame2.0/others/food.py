from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, food_type="normal"):
        super().__init__()
        self.food_type = food_type
        self.shape("circle")
        self.penup()
        if self.food_type == "normal":
            self.color("red")
            self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        elif self.food_type == "speed":
            self.color("blue")
            self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        elif self.food_type == "bonus":
            self.color("gold")
            self.shapesize(stretch_len=1, stretch_wid=1)
        self.spawn()
    def spawn(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)
