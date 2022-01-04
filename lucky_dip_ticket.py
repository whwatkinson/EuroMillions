from random import randint
from typing import List, Optional, Set
from uuid import UUID, uuid4

from pydantic import BaseModel, validator

from numbers_base import NumbersBase


class ExportTicket(BaseModel):
    uuid: UUID
    ticket_cost: float
    main_numbers: Set[int]
    main_matches_count: int
    main_matches: Optional[Set[int]]
    lucky_numbers: Set[int]
    lucky_matches_count: int
    lucky_matches: Optional[Set[int]]
    winner: bool
    has_all_main_numbers: bool
    has_both_lucky_numbers: bool
    total_matches: int
    prize: int
    prize_identifier: int

    def names(self):
        return self.__fields__.keys()

    @validator("main_matches", "lucky_matches")
    def set_to_tuple(cls, value) -> Optional[Set[int]]:

        if len(value) == 0:
            return None
        else:
            return value


class LuckDipTicket(NumbersBase):
    # could use a data class?
    def __init__(self, ticket_cost: float = 2.5):
        self.uuid: UUID = uuid4()
        self.ticket_cost: float = ticket_cost
        self.main_numbers: Set[int] = self.get_main_numbers()
        self.main_matches_count: int = 0
        self.main_matches: Set[int] = self.clean_set()
        self.lucky_numbers: Set[int] = self.get_lucky_numbers()
        self.lucky_matches_count: int = 0
        self.lucky_matches: Set[int] = self.clean_set()
        self.winner: bool = False
        self.has_all_main_numbers: bool = False
        self.has_both_lucky_numbers: bool = False
        self.prize: float = 0
        self.prize_identifier: int = 0

    @property
    def total_matches(self):
        return self.main_matches_count + self.lucky_matches_count

    def main_number_match_check(self, number_drawn: int) -> None:
        """
        Checks the main numbers of the ticket
        :param number_drawn: The number drawn from the bowl
        :return:
        """
        if number_drawn in self.main_numbers:
            self.main_matches_count += 1
            self.main_matches.add(number_drawn)
            # TODO needs a test
            self.winner = True
            self.prize_identifier += 1

            if self.main_matches_count == self.TOTAL_MAIN_NUMBERS:
                self.has_all_main_numbers = True

    def lucky_number_match_check(self, number_drawn: int) -> None:
        """
        Checks the lucky numbers of the ticket
        :param number_drawn: The number drawn from the bowl
        :return:
        """
        if number_drawn in self.lucky_numbers:
            self.lucky_matches_count += 1
            self.lucky_matches.add(number_drawn)
            # TODO needs a test
            self.winner = True
            self.prize_identifier += 10

            if self.lucky_matches_count == self.TOTAL_LUCKY_NUMBERS:
                self.has_both_lucky_numbers = True

    @staticmethod
    def get_random_numbers(total_numbers: int, upper_bound: int) -> Set[int]:
        """
        Get an arbitary sized set of random numbers
        :param total_numbers: The length of the desired set
        :param upper_bound: The size of the set to be drawn from
        :return:
        """
        numbers = set()
        while len(numbers) != total_numbers:
            number = randint(1, upper_bound)
            if number not in numbers:
                numbers.add(number)
            else:
                continue
        return numbers

    def get_main_numbers(self) -> Set[int]:
        """
        Method to get the main numbers
        :return:
        """
        numbers = self.get_random_numbers(self.TOTAL_MAIN_NUMBERS, self.MAIN_NUMBERS)
        return numbers

    def get_lucky_numbers(self) -> Set[int]:
        """
        Method to get the lucky numbers
        :return:
        """
        numbers = self.get_random_numbers(self.TOTAL_LUCKY_NUMBERS, self.LUCKY_NUMBERS)
        return numbers

    def prepare_ticket_for_export(self) -> ExportTicket:
        # TODO fix ugh kludge...
        d = {k: v for k, v in self.__dict__.items()}
        d["total_matches"] = self.total_matches
        export_ticket = ExportTicket(**d)
        return export_ticket

    def __repr__(self) -> str:
        return (
            f"uuid:              {self.uuid}\n"
            f"main numbers:      {self.repr_formatter(self.main_numbers)}\n"
            f"lucky numbers:     {self.repr_formatter(self.lucky_numbers)}"
        )


class LuckDipTicketList:
    def __init__(
        self,
        number_of_tickets: int = 5,
        ticket_cost: float = 2.5,
        duplicate_tickets: bool = False,
    ):
        self.tickets: List[LuckDipTicket] = self.get_tickets(
            number_of_tickets, ticket_cost, duplicate_tickets
        )
        self.total_cost: float = sum(ticket.ticket_cost for ticket in self.tickets)
        self.duplicate_tickets: bool = duplicate_tickets

    @property
    def total_winnings(self):
        return sum(ticket.prize for ticket in self.tickets)

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

    def __repr__(self) -> str:
        return (
            f"lucky dip tickets: {len(self.tickets)}\n"
            f"duplicate tickets: {self.duplicate_tickets}"
        )
