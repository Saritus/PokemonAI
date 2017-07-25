from data import get_pokemon


class Pokemon:
    def __init__(self, index):
        self.data = get_pokemon(index)
        self.types = [
            self.data["Type1"],
            self.data["Type2"]
        ]
        self.stats = {
            "Hit Points": 0,
            "Attack": 0,
            "Defense": 0,
            "Special": 0,
            "Speed": 0
        }


def main():
    return


if __name__ == "__main__":
    main()
