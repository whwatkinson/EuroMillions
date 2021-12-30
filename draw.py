from random import randint


class DrawCompleteError(Exception):
    def __init__(self):
        self.message = "5 main numbers have already been drawn"
        super().__init__(self.message)


class Draw:
    def __init__(self, total_prize_money: int = 1000000):
        self.total_prize_money = total_prize_money
        self.main_numbers = self.new_draw(numbers_drawn=None)
        self.lucky_numbers = self.new_draw(numbers_drawn=None)

    @staticmethod
    def new_draw(numbers_drawn):
        if not numbers_drawn:
            return set()
        else:
            return numbers_drawn

    def draw_main_number(self):

        if len(self.main_numbers) == 5:
            raise DrawCompleteError

        drawing = True

        while drawing:
            number = randint(1, 50)
            if number in self.main_numbers:
                continue
            else:
                self.main_numbers.add(number)
                drawing = False

    def draw_lucky_number(self):

        if len(self.main_numbers) == 2:
            raise DrawCompleteError

        drawing = True

        while drawing:
            number = randint(1, 12)
            if number in self.main_numbers:
                continue
            else:
                self.lucky_numbers.add(number)
                drawing = False

    @staticmethod
    def repr_formatter(numbers) -> str:
        if not numbers:
            return "{}"

        else:
            return numbers

    def __repr__(self):
        return (
            f"total prize money: {self.total_prize_money}\n"
            f"main numbers:      {self.repr_formatter(self.main_numbers)}\n"
            f"lucky numbers:     {self.repr_formatter(self.lucky_numbers)}"
        )

    def __hash__(self):
        return hash(f"{sorted(list(self.main_numbers))}") + hash(f"{sorted(list(self.lucky_numbers))}")

