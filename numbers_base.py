from typing import Optional, Set


class NumbersBase:
    TOTAL_MAIN_NUMBERS = 5
    TOTAL_LUCKY_NUMBERS = 2
    MAIN_NUMBERS = 50
    LUCKY_NUMBERS = 12
    main_numbers: set
    lucky_numbers: set



    @staticmethod
    def repr_formatter(numbers: Set[int]) -> str:
        """
        Handles the formatting of the numbers for the repr.
        :param numbers: The lotto numbers
        :return: A cleaned string
        """

        return str(numbers) if numbers else "{}"

    @staticmethod
    def clean_set(numbers_drawn: Optional[Set[int]] = None) -> Set[int]:
        """
        To create a new set as they are mutable and we want to add incrementally
        :param numbers_drawn: The number drawn from the bowl
        :return: A new set
        """
        if not numbers_drawn:
            return set()
        else:
            return numbers_drawn

    def __eq__(self, other) -> int:
        """
        An attempt to compare the tickets
        :param other: The other ticket
        :return: True is the tickets are the same
        """
        h1 = hash(f"{sorted(list(self.main_numbers))}") + hash(
            f"{sorted(list(self.lucky_numbers))}"
        )
        h2 = hash(f"{sorted(list(other.main_numbers))}") + hash(
            f"{sorted(list(other.lucky_numbers))}"
        )
        return h1 == h2
