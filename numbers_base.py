from typing import Optional, Set


class NumbersBase:
    TOTAL_MAIN_NUMBERS = 5
    TOTAL_LUCKY_NUMBERS = 2
    MAIN_NUMBERS = 50
    LUCKY_NUMBERS = 12

    @staticmethod
    def repr_formatter(numbers) -> str:
        if not numbers:
            return "{}"

        else:
            return numbers

    @staticmethod
    def clean_set(numbers_drawn: Optional[Set[int]] = None) -> Set[int]:
        """
        To create a new set as they are mutable and we want to add incrementally
        :param numbers_drawn:
        :return: A new set
        """
        if not numbers_drawn:
            return set()
        else:
            return numbers_drawn
