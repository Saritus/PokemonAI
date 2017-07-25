from data import get_pokemon


class Pokemon:
    def __init__(self, index):
        self.data = get_pokemon(index)
        self.types = [
            self.data["Type1"],
            self.data["Type2"]
        ]


def main():
    return


if __name__ == "__main__":
    main()
