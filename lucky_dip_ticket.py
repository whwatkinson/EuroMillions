from random import randint
from typing import Set


class LuckDipTicket:
    def __init__(self):
        self.main_numbers = self.get_main_numbers()
        self.lucky_numbers = self.get_main_numbers()
        self.winner = False
        self.matches = 0

    @staticmethod
    def get_random_numbers(total_numbers: int, upper_bound: int):
        numbers = set()
        while len(numbers) != total_numbers:
            number = randint(1, upper_bound)
            if number not in numbers:
                numbers.add(number)
            else:
                continue
        return numbers

    def get_main_numbers(self) -> Set[int]:
        numbers = self.get_random_numbers(5, 50)
        return numbers

    def get_lucky_star_numbers(self) -> Set[int]:
        numbers = self.get_random_numbers(2, 12)
        return numbers
