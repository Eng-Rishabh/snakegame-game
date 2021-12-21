from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
coordinate_sys = [-280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 20, 40, 60, 80, 100,
                  120, 140, 160, 180, 200, 220, 240, 260, 280]
food = Food()
game_on = True
snakes = []

snake = Snake()
scoreboard = Scoreboard()


def start_again():
    global game_on
    snake.start_again()
    # you can use this feature
    # food.goto(random.choice(coordinate_sys), random.choice(coordinate_sys))
    game_on = True
    game()


screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")
screen.onkey(start_again, "c")


def game():
    score = 0
    scoreboard.update_board(score)
    global game_on
    while game_on:
        screen.update()
        time.sleep(.1)
        snake.move()
        # Detect collision with food and food is 10 * 10 pixel
        if snake.head.distance(food) < 15:
            food.new_location()
            snake.more_part()
            score += 1
            scoreboard.update_board(score)
        # detect collision with board
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_on = False
            scoreboard.game_over()
        # if head collision with tail
        for part in snake.snakes[1:]:
            if snake.head.distance(part) < 10:
                game_on = False
                scoreboard.game_over()


screen.exitonclick()
