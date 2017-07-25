from data import get_pokemon, get_move
import random


class Pokemon:
    def __init__(self, index, level=5, ivs=None, moves=None):
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
        self.name = data["Name"]
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
        self.currHP = self.stats["HP"]
        if moves is None:
            self.moves = [
                Move(random.randint(0, 164)),
                Move(random.randint(0, 164)),
                Move(random.randint(0, 164)),
                Move(random.randint(0, 164))
            ]
        else:
            self.moves = moves

    def attack(self, attack, opponent):
        damage = self.moves[attack].power
        opponent.currHP = max(0, opponent.currHP - damage)
        self.moves[attack].pp -= 1
        return

    def get_info(self):
        return "Name: {}\nHP: {}\nMove 1: {}\nMove 2: {}\nMove 3: {}\nMove 4: {}" \
            .format(self.name, self.currHP, self.moves[0].get_info(), self.moves[1].get_info(), self.moves[2].get_info(), self.moves[3].get_info())


class Fight:
    def __init__(self, myPokemon, otherPokemon):
        self.myPokemon = myPokemon
        self.otherPokemon = otherPokemon
        return

    def get_info(self):
        return "{}\n\n{}".format(self.myPokemon.get_info(), self.otherPokemon.get_info())


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

    def get_info(self):
        return {'PP': self.pp,
                'Acc.': self.acc,
                'Name': self.name,
                'Power': self.power,
                'Cat.': self.category,
                'Type': self.type
                }


def main():
    return


if __name__ == "__main__":
    main()
