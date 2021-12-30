from random import randint
from typing import List, Set
from uuid import uuid4

from numbers_base import NumbersBase


class LuckDipTicket(NumbersBase):
    def __init__(self, ticket_cost: float = 2.5):
        self.main_numbers = self.get_main_numbers()
        self.lucky_numbers = self.get_lucky_numbers()
        self.winner = False
        self.main_matches_count = 0
        self.main_matches = self.clean_set()
        self.lucky_matches_count = 0
        self.lucky_matches = self.clean_set()

        self.ticket_cost = ticket_cost
        self.uuid = uuid4()

    def main_number_match_check(self, number_drawn: int) -> None:
        if number_drawn in self.main_numbers:
            self.main_matches_count += 1
            self.main_matches.add(number_drawn)
            self.winner = True

    def lucky_number_match_check(self, number_drawn: int) -> None:
        if number_drawn in self.lucky_numbers:
            self.lucky_matches_count += 1
            self.lucky_matches.add(number_drawn)
            self.winner = True

    @staticmethod
    def get_random_numbers(total_numbers: int, upper_bound: int) -> Set[int]:
        numbers = set()
        while len(numbers) != total_numbers:
            number = randint(1, upper_bound)
            if number not in numbers:
                numbers.add(number)
            else:
                continue
        return numbers

    def get_main_numbers(self) -> Set[int]:
        numbers = self.get_random_numbers(self.TOTAL_MAIN_NUMBERS, self.MAIN_NUMBERS)
        return numbers

    def get_lucky_numbers(self) -> Set[int]:
        numbers = self.get_random_numbers(self.TOTAL_LUCKY_NUMBERS, self.LUCKY_NUMBERS)
        return numbers

    def __repr__(self) -> str:
        return (
            f"uuid:              {self.uuid}\n"
            f"main numbers:      {self.repr_formatter(self.main_numbers)}\n"
            f"lucky numbers:     {self.repr_formatter(self.lucky_numbers)}"
        )

    def __eq__(self, other) -> int:
        h1 = hash(f"{sorted(list(self.main_numbers))}") + hash(
            f"{sorted(list(self.lucky_numbers))}"
        )
        h2 = hash(f"{sorted(list(other.main_numbers))}") + hash(
            f"{sorted(list(other.lucky_numbers))}"
        )
        return h1 == h2


class LuckDipTicketList:
    def __init__(
        self,
        number_of_tickets: int = 5,
        ticket_cost: float = 2.5,
        duplicate_tickets: bool = False,
    ):
        self.tickets = self.get_tickets(
            number_of_tickets, ticket_cost, duplicate_tickets
        )
        self.total_cost = sum(ticket.ticket_cost for ticket in self.tickets)
        self.duplicate_tickets = duplicate_tickets

    @staticmethod
    def get_tickets(
        number_of_tickets: int, ticket_cost: float, duplicate_tickets: bool
    ) -> List[LuckDipTicket]:
        """
        Get the tickets
        :param number_of_tickets: How many tickets
        :param ticket_cost: How much a ticket costs
        :param duplicate_tickets: Allow duplicates
        :return: A list of tickets
        """

        if duplicate_tickets:
            return [
                LuckDipTicket(ticket_cost=ticket_cost) for _ in range(number_of_tickets)
            ]

        else:

            tickets_list = []

            while len(tickets_list) != number_of_tickets:
                ticket = LuckDipTicket(ticket_cost)

                if ticket in tickets_list:
                    continue
                else:
                    tickets_list.append(ticket)

            return tickets_list

    def __repr__(self):
        return (
            f"lucky dip tickets: {len(self.tickets)}\n"
            f"duplicate tickets: {self.duplicate_tickets}"
        )
