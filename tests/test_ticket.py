from pytest import mark


from lucky_dip_ticket import LuckDipTicket, LuckDipTicketList


class TestTicket:
    def test_ticket(self):

        t = LuckDipTicket()

        assert t.winner is False
        assert t.matches == 0

    def test_get_main_numbers(self):

        t = LuckDipTicket()

        test_main_numbers = t.get_main_numbers()
        assert len(test_main_numbers) == 5

        for number in test_main_numbers:
            assert 0 < number < 51

    def test_get_lucky_star_numbers(self):

        t = LuckDipTicket()

        test_lucky_numbers = t.get_lucky_star_numbers()
        assert len(test_lucky_numbers) == 2

        for number in test_lucky_numbers:
            assert 0 < number < 12

    @mark.parametrize(
        "number_of_tickets, ticket_cost, expected_cost",
        [
            (5, 2.5, 12.5),
            (100, 2.5, 250)
        ]
    )
    def test_lucky_dip_ticket_list(self, number_of_tickets, ticket_cost, expected_cost):

        tl = LuckDipTicketList(number_of_tickets, ticket_cost)

        assert tl.total_cost == expected_cost
