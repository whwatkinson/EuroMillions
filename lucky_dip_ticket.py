from random import randint
from typing import Set
from uuid import uuid4

from draw import MAIN_NUMBERS, LUCKY_NUMBERS, NUMBER_MAIN_NUMBERS, NUMBER_LUCKY_NUMBERS
from numbers_base import NumbersBase


class LuckDipTicketList:
    def __init__(self, number_of_tickets: int = 5, ticket_cost: float = 2.5):
        # Unique tickets?
        self.tickets = [LuckDipTicket(ticket_cost=ticket_cost) for _ in range(number_of_tickets)]
        self.total_cost = sum(ticket.ticket_cost for ticket in self.tickets)

    def __repr__(self):
        return (
            f"lucky dip tickets: {len(self.tickets)}"
        )


class LuckDipTicket(NumbersBase):
    def __init__(self, ticket_cost: float = 2.5):
        self.main_numbers = self.get_main_numbers()
        self.lucky_numbers = self.get_lucky_star_numbers()
        self.winner = False
        self.matches = 0
        self.ticket_cost = ticket_cost
        self.uuid = uuid4()

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
        numbers = self.get_random_numbers(MAIN_NUMBERS, NUMBER_MAIN_NUMBERS)
        return numbers

    def get_lucky_star_numbers(self) -> Set[int]:
        numbers = self.get_random_numbers(LUCKY_NUMBERS, NUMBER_LUCKY_NUMBERS)
        return numbers

    def __repr__(self):
        return (
            f"uuid:              {self.uuid}\n"
            f"main numbers:      {self.repr_formatter(self.main_numbers)}\n"
            f"lucky numbers:     {self.repr_formatter(self.lucky_numbers)}"
        )

    def __hash__(self):
        return hash(f"{sorted(list(self.main_numbers))}") + hash(f"{sorted(list(self.lucky_numbers))}")
