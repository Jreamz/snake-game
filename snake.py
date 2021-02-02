from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for snake_index in START_POSITION:
            self.add_snake(snake_index)

    def add_snake(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.add_snake(self.snakes[-1].position())

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
