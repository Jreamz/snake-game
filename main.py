from turtle import Screen
from snake import Snake
from food import Food
from score import Score

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SN4K3")
screen.tracer(0)

score = Score()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend()
        score.add_score()

    #detect collision with boundary
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.snakes[1::]:
        if snake.head.distance(segment) < 10:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
