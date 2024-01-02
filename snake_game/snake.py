from turtle import *

STARTING_POSITION = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        newsegment = Turtle('square')
        newsegment.penup()
        newsegment.color('white')
        newsegment.goto(position)
        self.segments.append(newsegment)

    def reset(self):
        for seg in self.segments:
            seg.goto((1000,1000))
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]
    def extend(self):
        # add new segment to snake
        self.add_segment(self.segments[-1].position())

    def Move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto((new_x, new_y))
        self.head.forward(MOVE_DISTANCE)
        # self.segments[0].left(90)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
