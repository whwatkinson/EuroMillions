from draw import Draw
from lucky_dip_ticket import LuckDipTicket, LuckDipTicketList


class Wednesday:
    def __init__(self, draw: Draw, ticket: LuckDipTicket):
        self.draw = draw
        self.ticket = ticket

    def check_results(self):
        pass
