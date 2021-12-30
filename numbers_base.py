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
