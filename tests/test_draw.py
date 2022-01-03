from contextlib import contextmanager
from typing import Tuple

from pytest import mark, raises

from draw import Draw, DrawCompleteError


class TestDraw:
    @contextmanager
    def does_not_raise():
        yield

    @mark.parametrize(
        "total_prize_money, expected_total_prize_money",
        [
            (5000, 5000.00),
            (1000000.00, 1000000.00),
        ],
    )
    def test_new_draw(
        self, total_prize_money: float, expected_total_prize_money: float
    ):

        d = Draw(total_prize_money=total_prize_money)

        assert len(d.main_numbers) == 0
        assert len(d.lucky_numbers) == 0
        assert d.total_prize_money == expected_total_prize_money

    @mark.parametrize(
        "draws, expected_totals, expectation",
        [
            ((1, 0), (1, 0), does_not_raise()),
            ((3, 0), (3, 0), does_not_raise()),
            ((5, 0), (5, 0), does_not_raise()),
            ((5, 1), (5, 1), does_not_raise()),
            ((5, 2), (5, 2), does_not_raise()),
            ((6, 0), (5, 2), raises(DrawCompleteError)),
            ((6, 3), (5, 2), raises(DrawCompleteError)),
        ],
    )
    def test_draw(self, draws: Tuple[int], expected_totals: Tuple[int], expectation):
        with expectation:
            d = Draw()
            exp_main_numbers, exp_lucky_numbers = expected_totals
            main_draws, lucky_draws = draws

            for _ in range(main_draws):
                d.draw_main_number()
            assert len(d.main_numbers) == exp_main_numbers

            for _ in range(lucky_draws):
                d.draw_lucky_number()
            assert len(d.lucky_numbers) == exp_lucky_numbers

    def test_auto_draw(self):

        d = Draw()

        d.auto_draw_all()

        assert len(d.main_numbers) == d.TOTAL_MAIN_NUMBERS
        assert len(d.lucky_numbers) == d.TOTAL_LUCKY_NUMBERS
