from pytest import mark

from lucky_dip_ticket import LuckDipTicket


class TestTicket:

    def test_get_main_numbers(self):

        t = LuckDipTicket()

        test_main_numbers = t.get_main_numbers()
        assert len(test_main_numbers) == 5

        for number in test_main_numbers:
            assert 0 < number < 51

    def test_get_lucky_star_numbers(self):

        t = LuckDipTicket()

        test_main_numbers = t.get_lucky_star_numbers()
        assert len(test_main_numbers) == 2

        for number in test_main_numbers:
            assert 0 < number < 12
