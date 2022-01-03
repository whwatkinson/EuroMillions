from typing import Set

from pytest import mark

from lucky_dip_ticket import LuckDipTicket, LuckDipTicketList


class TestLuckyDipTicket:
    def test_new_ticket(self):

        t = LuckDipTicket()

        assert t.winner is False
        assert t.main_matches_count == 0
        assert len(t.main_matches) == 0
        assert t.lucky_matches_count == 0
        assert len(t.lucky_matches) == 0

    def test_get_main_numbers(self):

        t = LuckDipTicket()

        test_main_numbers = t.get_main_numbers()
        assert len(test_main_numbers) == t.TOTAL_MAIN_NUMBERS

        for number in test_main_numbers:
            assert 0 < number <= t.MAIN_NUMBERS

    def test_get_lucky_star_numbers(self):

        t = LuckDipTicket()

        test_lucky_numbers = t.get_lucky_numbers()
        assert len(test_lucky_numbers) == t.TOTAL_LUCKY_NUMBERS

        for number in test_lucky_numbers:
            assert 0 < number <= t.LUCKY_NUMBERS

    @mark.parametrize(
        "number_of_tickets, ticket_cost, expected_cost, number_expected_tickets",
        [(5, 2.5, 12.5, 5), (100, 2.5, 250, 100)],
    )
    def test_lucky_dip_ticket_list(
        self,
        number_of_tickets: int,
        ticket_cost: float,
        expected_cost: float,
        number_expected_tickets: int,
    ):

        tl = LuckDipTicketList(number_of_tickets, ticket_cost)

        assert tl.total_cost == expected_cost
        assert len(tl.tickets) == number_expected_tickets

    def test_lucky_ticket_eq(self):

        t1 = LuckDipTicket()
        t2 = LuckDipTicket()

        assert t1 != t2

        t1.main_numbers = t2.main_numbers = {1, 2, 3, 4, 5}
        t1.lucky_numbers = t2.lucky_numbers = {6, 7}

        assert t1 == t2

    @mark.parametrize(
        "main_numbers, lucky_numbers, number_drawn, lucky, expected_matches_count, expected_matches, expected_winner",
        [
            ({1, 2, 3, 4, 5}, {6, 7}, 1, False, 1, {1}, True),
            ({34, 5, 41, 42, 18}, {6, 7}, 1, False, 0, set(), False),
            ({2, 37, 8, 46, 14}, {9, 10}, 10, True, 1, {10}, True),
            ({34, 10, 47, 50, 25}, {11, 3}, 2, True, 0, set(), False),
        ],
    )
    def test_match_check(
        self,
        main_numbers: Set[int],
        lucky_numbers: Set[int],
        number_drawn: int,
        lucky: bool,
        expected_matches_count: int,
        expected_matches: Set[int],
        expected_winner: bool,
    ):

        test_ticket = LuckDipTicket()
        test_ticket.main_numbers = main_numbers
        test_ticket.lucky_numbers = lucky_numbers

        if lucky:
            test_ticket.lucky_number_match_check(number_drawn)
            assert test_ticket.lucky_matches == expected_matches
            assert test_ticket.lucky_matches_count == expected_matches_count

        else:
            test_ticket.main_number_match_check(number_drawn)
            assert test_ticket.main_matches == expected_matches
            assert test_ticket.main_matches_count == expected_matches_count

        assert test_ticket.winner == expected_winner

    def test_number_match_count(self):

        test_ticket = LuckDipTicket()
        test_ticket.main_numbers = {1, 2, 3, 4, 5}
        test_ticket.lucky_numbers = {6, 7}

        assert test_ticket.has_all_main_numbers is False
        assert test_ticket.has_both_lucky_numbers is False

        for i, _ in enumerate(test_ticket.main_numbers, 1):

            test_ticket.main_number_match_check(i)

        assert test_ticket.main_matches_count == test_ticket.TOTAL_MAIN_NUMBERS
        assert test_ticket.has_all_main_numbers is True

        for i, _ in enumerate(test_ticket.lucky_numbers, 6):

            test_ticket.lucky_number_match_check(i)

        assert test_ticket.lucky_matches_count == test_ticket.TOTAL_LUCKY_NUMBERS
        assert test_ticket.has_both_lucky_numbers is True

    def test_prepare_ticket_for_export(self):

        test_ticket = LuckDipTicket()
        test_ticket.main_numbers = {1, 2, 3, 4, 5}
        test_ticket.lucky_numbers = {6, 7}
        test_ticket.winner = True

        test_export = test_ticket.prepare_ticket_for_export()

        assert test_export["main_numbers"] == {1, 2, 3, 4, 5}
        assert test_export["lucky_numbers"] == {6, 7}
        assert test_export["winner"] is True
