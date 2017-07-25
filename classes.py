from data import get_pokemon
import random


class Pokemon:
    def __init__(self, index, level=5, ivs=None):
        if ivs is None:
            self.ivs = {"HP": random.randint(0, 15),
                        "Attack": random.randint(0, 15),
                        "Defense": random.randint(0, 15),
                        "Special": random.randint(0, 15),
                        "Speed": random.randint(0, 15)
                        }
        else:
            self.ivs = ivs
        data = get_pokemon(index)
        self.level = level
        self.types = [
            data["Type1"],
            data["Type2"]
        ]
        self.stats = {
            "HP": int(float(2 * data["HP"] + 2 * self.ivs["HP"]) * self.level / 100 + self.level + 10),
            "Attack": int(float(2 * data["Attack"] + 2 * self.ivs["Attack"]) * self.level / 100 + 5),
            "Defense": int(float(2 * data["Defense"] + 2 * self.ivs["Defense"]) * self.level / 100 + 5),
            "Special": int(float(2 * data["Special"] + 2 * self.ivs["Special"]) * self.level / 100 + 5),
            "Speed": int(float(2 * data["Speed"] + 2 * self.ivs["Speed"]) * self.level / 100 + 5)
        }

class Fight:
    def __init__(self, myPokemon, otherPokemon):
        self.myPokemon = myPokemon
        self.otherPokemon = otherPokemon
        return


class Move:
    def __init__(self, index):
        data = get_move(index)
        self.data = data
        self.pp = data['PP']
        self.acc = data['Acc.']
        self.name = data['Name']
        self.power = data['Power']
        self.effect = data['Effect']
        self.category = data['Cat.']
        self.type = data['Type']
        return

    def print_info(self):
        print {'PP': self.pp,
               'Acc.': self.acc,
               'Name': self.name,
               'Power': self.power,
               'Effect': self.effect,
               'Cat.': self.category,
               'Type': self.type
               }


def main():
    return


if __name__ == "__main__":
    main()
