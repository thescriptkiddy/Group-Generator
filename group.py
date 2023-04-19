import random
from turtle import Turtle

LIST_OF_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
LIST_OF_COLORS = ["red", "green", "black", "yellow", "blue", "orange", "purple"]


class Group(Turtle):
    """Generates a new group"""
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(LIST_OF_COLORS))
        self.write(generate_name(), align="right", font=("Courier", 10, "normal"))
        self.goto(-10, 20)


def generate_name():
    """Generates a random name"""
    random_char = random.choice(LIST_OF_CHARS)
    random_num = random.randint(0, 200)
    random_name = f"{random_char}_{random_num}"
    return random_name

