from random import randint
from typing import Set


class LuckDipTicketList:
    def __init__(self, number_of_tickets: int = 5, ticket_cost: float = 2.5):
        self.tickets = [LuckDipTicket(ticket_cost=ticket_cost) for _ in range(number_of_tickets)]
        self.total_cost = sum(ticket.ticket_cost for ticket in self.tickets)

    def __repr__(self):
        return (
            f"lucky dip tickets: {len(self.tickets)}"
        )


class LuckDipTicket:
    def __init__(self, ticket_cost: float = 2.5):
        self.main_numbers = self.get_main_numbers()
        self.lucky_numbers = self.get_lucky_star_numbers()
        self.winner = False
        self.matches = 0
        self.ticket_cost = ticket_cost

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
