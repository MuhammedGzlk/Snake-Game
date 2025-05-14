from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake_S:
    def __init__(self):
        self.segments = []
        self.speed = 10
        self.speed_multiplier = 1.05
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('black')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Yılanın son segmentinden yeni segment ekle
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(self.speed)

    def wrap_around(self, screen_width, screen_height):
        x = self.head.xcor()
        y = self.head.ycor()
        if x > screen_width / 2:
            self.head.setx(-screen_width / 2)
        elif x < -screen_width / 2:
            self.head.setx(screen_width / 2)
        if y > screen_height / 2:
            self.head.sety(-screen_height / 2)
        elif y < -screen_height / 2:
            self.head.sety(screen_height / 2)

    def speed_up(self):
        self.speed *= self.speed_multiplier

    def check_self_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
