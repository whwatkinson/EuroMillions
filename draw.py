from typing import Set
from random import randint

from numbers_base import NumbersBase


MAIN_NUMBERS = 5
LUCKY_NUMBERS = 2
NUMBER_MAIN_NUMBERS = 50
NUMBER_LUCKY_NUMBERS = 12


class DrawCompleteError(Exception):
    def __init__(self, number_of_draws):
        self.message = f"{number_of_draws} main numbers have already been drawn"
        super().__init__(self.message)


class Draw(NumbersBase):
    def __init__(self, total_prize_money: int = 1000000):
        self.total_prize_money = total_prize_money
        self.main_numbers = self.new_draw(numbers_drawn=None)
        self.lucky_numbers = self.new_draw(numbers_drawn=None)

    @staticmethod
    def new_draw(numbers_drawn) -> Set[int]:
        if not numbers_drawn:
            return set()
        else:
            return numbers_drawn

    @staticmethod
    def draw_random_number(numbers: Set[int], upper_bound: int):
        drawing = True
        while drawing:
            number = randint(1, upper_bound)
            if number in numbers:
                continue
            else:
                numbers.add(number)
                drawing = False
        return numbers

    def draw_main_number(self):

        if len(self.main_numbers) == MAIN_NUMBERS:
            raise DrawCompleteError(number_of_draws=MAIN_NUMBERS)

        self.draw_random_number(self.main_numbers, NUMBER_MAIN_NUMBERS)

    def draw_lucky_number(self):

        if len(self.lucky_numbers) == LUCKY_NUMBERS:
            raise DrawCompleteError(number_of_draws=LUCKY_NUMBERS)

        self.draw_random_number(self.lucky_numbers, NUMBER_LUCKY_NUMBERS)

    def __repr__(self):
        return (
            f"total prize money: {self.total_prize_money}\n"
            f"main numbers:      {self.repr_formatter(self.main_numbers)}\n"
            f"lucky numbers:     {self.repr_formatter(self.lucky_numbers)}"
        )

    def __hash__(self):
        return hash(f"{sorted(list(self.main_numbers))}") + hash(f"{sorted(list(self.lucky_numbers))}")

