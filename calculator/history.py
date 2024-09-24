from typing import List
from calculator.calculation import Calculation


class History:
    history = List[Calculation] = []

    @classmethod
    def addCalculation(cls, cal: Calculation):
        cls.history.append(cal)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history

    @classmethod
    def clear_history(cls):
        cls.history.clear

    @classmethod
    def print_history(cls):
        output = ""
        for cal in cls.history:
            output += cal.print_calculation(cal)
        return output