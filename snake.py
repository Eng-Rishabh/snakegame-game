from turtle import Turtle
# no of the initial bocks of the snake
H = 3
INITIAL_POSITION = (0, 0)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.snake_creator()
        self.head = self.snakes[0]

    def snake_creator(self):
        for d in range(0, H):
            new_snake = Turtle("square")
            new_snake.speed('slow')
            new_snake.hideturtle()
            new_snake.color('white')
            new_snake.penup()
            new_snake.showturtle()
            self.snakes.append(new_snake)

    def more_part(self):
        global H
        new_snake = Turtle("square")
        new_snake.speed('slow')
        new_snake.hideturtle()
        new_snake.color('white')
        new_snake.penup()
        H += 1
        new_snake.goto(self.snakes[-1].position())
        new_snake.showturtle()
        self.snakes.append(new_snake)

    def move(self):
        all_position = [(0, 0)] * H
        all_position[0] = (round(self.snakes[0].position()[0]), round(self.snakes[0].position()[1]))
        # updating the head for moving forward
        self.head.forward(MOVE_DISTANCE)
        # saving the current position of the head for various use
        # snake_0_position = (round(snakes[0].position()[0]), round(snakes[0].position()[1]))
        for i in range(1, H):
            """for snakes tail blocks to follow head"""
            old_position = (round(self.snakes[i].position()[0]), round(self.snakes[i].position()[1]))
            all_position[i] = old_position
            self.snakes[i].goto(all_position[i - 1][0], all_position[i - 1][1])
            self.snakes[i].showturtle()

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def start_again(self):
        self.head.home()
