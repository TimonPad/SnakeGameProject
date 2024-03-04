from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.shnakes = []
        self.create_snake()
        self.head = self.shnakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snakebit(position)


    def move(self):
        for shnake_num in range(len(self.shnakes) - 1, 0, -1):
            new_x = self.shnakes[shnake_num - 1].xcor()
            new_y = self.shnakes[shnake_num - 1].ycor()
            self.shnakes[shnake_num].goto(new_x, new_y)

        self.shnakes[0].forward(MOVE_DISTANCE)
    def add_snakebit(self, position):
        new_shnake = Turtle("square")
        new_shnake.penup()
        new_shnake.color("purple")
        new_shnake.goto(position)
        self.shnakes.append(new_shnake)
    def extend(self):
        #add new segnemnt to snake
        self.add_snakebit(self.shnakes[-1].position())

    def reset(self):
        for shnake in self.shnakes:
            shnake.goto(1000,1000)

        self.shnakes.clear()
        self.create_snake()
        self.head = self.shnakes[0]

    def up(self):
        snake1 = self.shnakes[0]
        if snake1.heading() != DOWN:
            snake1.setheading(UP)
    def down(self):
        snake1 = self.shnakes[0]
        if snake1.heading() != UP:
            snake1.setheading(DOWN)
    def left(self):
        snake1 = self.shnakes[0]
        if snake1.heading() != RIGHT:
            snake1.setheading(LEFT)

    def right(self):
        snake1 = self.shnakes[0]
        if snake1.heading() != LEFT:
            snake1.setheading(RIGHT)
