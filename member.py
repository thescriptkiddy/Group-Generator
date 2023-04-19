import random
from turtle import Turtle

LIST_OF_COLORS = ["red", "green", "black", "yellow", "blue", "orange", "purple"]
# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Member(Turtle):

    def __init__(self, name):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.member_name = name
        self.color(random.choice(LIST_OF_COLORS))
        self.goto(0, 0)
        self.write({self.member_name}, align="right", font=("Courier", 10, "normal"))



