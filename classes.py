from data import get_pokemon
from math import floor


class Pokemon:
    def __init__(self, index, level=5):
        self.level = level
        self.data = get_pokemon(index)
        self.types = [
            self.data["Type1"],
            self.data["Type2"]
        ]
        B = 1  # B (Base Stat)
        I = 1  # I (Individual Value)
        L = self.level  # L (Level)
        self.stats = {
            "HP": floor((2 * B + I) * L / 100 + 5),
            "Attack": 0,
            "Defense": 0,
            "Special": 0,
            "Speed": 0
        }


def main():
    return


if __name__ == "__main__":
    main()
