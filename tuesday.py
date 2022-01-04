from datetime import datetime
from typing import Optional

from draw import Draw
from lucky_dip_ticket import LuckDipTicketList


class ResultsAlreadyCheckedError(Exception):
    def __init__(self, time_checked: datetime):
        self.message: str = f"results where checked at: {time_checked}"
        super().__init__(self.message)


class Tuesday:
    def __init__(self, draw: Draw, tickets: LuckDipTicketList):
        self.draw: Draw = draw
        self.tickets: LuckDipTicketList = tickets
        self.draw_checked: bool = False
        self.time_checked: Optional[datetime] = None
        self.number_jackpots: int = 1

    def check_results(self) -> None:

        if not self.draw_checked:

            for ticket in self.tickets.tickets:
                draw_main_numbers = self.draw.main_numbers

                for m_number in draw_main_numbers:
                    ticket.main_number_match_check(m_number)

                for l_number in self.draw.lucky_numbers:
                    ticket.lucky_number_match_check(l_number)

                if ticket.prize_identifier == 25:
                    self.number_jackpots += 1
                    self.tickets.has_jackpot = True

            # Separate as need to know how many jackpots?
            for ticket in self.tickets.tickets:
                try:
                    if ticket.prize_identifier == 25:
                        factor = self.number_jackpots
                    else:
                        factor = 1

                    ticket.prize = (
                        self.draw.prize_allocation[ticket.prize_identifier] / factor
                    )
                except KeyError:
                    ticket.prize = 0

            self.time_checked = datetime.now()
            self.draw_checked = True
        else:
            raise ResultsAlreadyCheckedError(time_checked=self.time_checked)

    def get_winners(self):

        winners = [ticket for ticket in self.tickets.tickets if ticket.winner]

        winners_sorted = sorted(
            winners,
            key=lambda x: (
                x.main_matches_count,
                x.total_matches,
                x.lucky_matches_count,
            ),
            reverse=True,
        )

        return winners_sorted


if __name__ == "__main__":
    ticket_list = LuckDipTicketList(number_of_tickets=100)
    the_draw = Draw()
    the_draw.auto_draw_all()
    w = Tuesday(the_draw, ticket_list)
