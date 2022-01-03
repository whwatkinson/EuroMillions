from random import randint
from typing import Set, Union
from uuid import uuid4, UUID

from numbers_base import NumbersBase


class DrawCompleteError(Exception):
    def __init__(self, number_of_draws):
        self.message = f"{number_of_draws} main numbers have already been drawn"
        super().__init__(self.message)


class PrizeMoneyIncorrect(Exception):
    def __init__(self, total_prize_money):
        self.message = f"{total_prize_money} is in the incorrect format"
        super().__init__(self.message)


class Draw(NumbersBase):
    def __init__(self, total_prize_money: Union[float, int] = 1000000.00):
        self.uuid: UUID = uuid4()
        self.total_prize_money: float = self.parse_prize_money(total_prize_money)
        self.main_numbers: Set[int] = self.clean_set()
        self.lucky_numbers: Set[int] = self.clean_set()

    @staticmethod
    def parse_prize_money(total_prize_money: Union[float, int]) -> float:
        try:
            prize = float(total_prize_money)
            return prize
        except ValueError:
            raise PrizeMoneyIncorrect(total_prize_money=total_prize_money)

    @staticmethod
    def draw_random_number(numbers: Set[int], upper_bound: int):
        drawing = True
        # could be done with random0 and choice?
        # would remove the while loops
        while drawing:
            number = randint(1, upper_bound)
            if number in numbers:
                continue
            else:
                numbers.add(number)
                drawing = False

    def draw_main_number(self) -> None:
        """
        Draws one main number
        :return: A random main number
        """
        if len(self.main_numbers) == self.TOTAL_MAIN_NUMBERS:
            raise DrawCompleteError(number_of_draws=self.TOTAL_MAIN_NUMBERS)

        self.draw_random_number(self.main_numbers, self.MAIN_NUMBERS)

    def draw_lucky_number(self) -> None:
        """
        Draws one lucky number
        :return: A random lucky number
        """

        if len(self.lucky_numbers) == self.TOTAL_LUCKY_NUMBERS:
            raise DrawCompleteError(number_of_draws=self.TOTAL_LUCKY_NUMBERS)

        self.draw_random_number(self.lucky_numbers, self.LUCKY_NUMBERS)

    def auto_draw_all(self) -> None:
        """
        Auto runs the draw
        :return: A full complement of main and lucky numbers
        """

        for _ in range(self.TOTAL_MAIN_NUMBERS):
            self.draw_main_number()

        for _ in range(self.TOTAL_LUCKY_NUMBERS):
            self.draw_lucky_number()

    def __repr__(self) -> str:
        return (
            f"total prize money:  £{self.total_prize_money}\n"
            f"main numbers:       {self.repr_formatter(self.main_numbers)}\n"
            f"lucky numbers:      {self.repr_formatter(self.lucky_numbers)}"
        )
