from contextlib import contextmanager

from pytest import mark, raises

from draw import Draw, DrawCompleteError


class TestDraw:

    @contextmanager
    def does_not_raise():
        yield

    def test_new_draw(self):

        d = Draw()

        assert len(d.main_numbers) == 0
        assert len(d.lucky_numbers) == 0

    @mark.parametrize(
        "draws, expected_totals, expectation",
        [
            ((1, 0), (1, 0), does_not_raise()),
            ((3, 0), (3, 0), does_not_raise()),
            ((5, 0), (5, 0), does_not_raise()),
            ((5, 1), (5, 1), does_not_raise()),
            ((5, 2), (5, 2), does_not_raise()),
            ((6, 0), (5, 2), raises(DrawCompleteError)),
            ((6, 3), (5, 2), raises(DrawCompleteError))
        ]
    )
    def test_draw(self, draws, expected_totals, expectation):
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

