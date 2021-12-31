from os import path
from random import choice
from uuid import uuid4

NAMES_FP = path.abspath("names.txt")


class Person:
    def __init__(self):
        self.uuid = uuid4()
        self.name = self.random_name(NAMES_FP)

    @staticmethod
    def random_name(file_path: path):
        names = open(file_path).read().splitlines()
        name = choice(names)
        return name

    def __repr__(self):
        return f"person: {self.name}"
