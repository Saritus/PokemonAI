from data import get_pokemon, get_move
import random
import time
import math
import numpy as np


class Pokemon:
    def __init__(self, index=0, level=0, ivs=None, moves=None):
        if ivs is None:
            self.ivs = {"HP": random.randint(0, 15),
                        "Attack": random.randint(0, 15),
                        "Defense": random.randint(0, 15),
                        "Special": random.randint(0, 15),
                        "Speed": random.randint(0, 15)
                        }
        else:
            self.ivs = ivs
        if index == 0:
            index = random.randint(1, 151)
        data = get_pokemon(index)
        self.index = index
        self.name = data["Name"]
        self.level = level if level is not 0 else 100
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
        L = self.level
        attack = attack.flatten()[0]

        if self.moves[attack].pp > 0:
            if self.moves[attack].category is "Special":
                A = self.stats["Special"]
                D = opponent.stats["Special"]
            else:
                A = self.stats["Attack"]
                D = opponent.stats["Defense"]
            P = self.moves[attack].power
            damage = int(math.floor(math.floor(2 * L / 5 + 2) * A * P / D) / 50) + 2
            opponent.currHP = max(0, opponent.currHP - damage)
            self.moves[attack].pp -= 1
        else:
            self.currHP = 0
            damage = 0
        print attack, self.moves[attack].pp, damage
        return damage

    def get_info(self):
        info = [
            self.index,
            self.currHP,
            self.stats["HP"],
            self.stats["Attack"],
            self.stats["Defense"],
            self.stats["Special"],
            self.stats["Speed"],
        ]
        info.extend(self.moves[0].get_info())
        info.extend(self.moves[1].get_info())
        info.extend(self.moves[2].get_info())
        info.extend(self.moves[3].get_info())
        return info


class Fight:
    # Done
    def __init__(self):
        self.reset()

    def get_info(self):
        return "###\n{}\n\n{}\n".format(self.pokemon1.get_info(), self.pokemon2.get_info())

    def attack(self, move):
        move = move.flatten()[0]
        self.dmg = self.current.attack(move, self.opponent)
        # print "{} used {}({}). {} Damage".format(self.current.name, self.current.moves[move].name, move, dmg)

        print self.pokemon1.name, self.pokemon1.currHP
        print self.pokemon2.name, self.pokemon2.currHP
        print ""

        return

    def _update_state(self, action):
        self.attack(action)

    # Done
    def _draw_state(self):
        infos = [
            self.pokemon1.currHP,
            self.pokemon2.currHP
        ]
        return np.asarray(infos)

    # Done
    def _get_reward(self):
        if self.currentPokemon == 1:
            return self.pokemon1.currHP if self.pokemon2.currHP is 0 else self.pokemon1.currHP / self.pokemon2.currHP
        else:
            return self.pokemon2.currHP if self.pokemon1.currHP is 0 else self.pokemon2.currHP / self.pokemon1.currHP

    # Done
    def _is_over(self):
        return (self.pokemon1.currHP is 0) or (self.pokemon2.currHP is 0)

    # Done
    def observe(self):
        canvas = self._draw_state()
        return canvas.reshape((1, -1))

    # Done
    def act(self, action):
        self._update_state(action)
        reward = self._get_reward()
        game_over = self._is_over()
        return self.observe(), reward, game_over

    # Done
    def reset(self):
        self.pokemon1 = Pokemon()
        self.pokemon2 = Pokemon()
        self.currentPokemon = 1
        self.state = np.asarray([self.pokemon1.currHP, self.pokemon2.currHP])[np.newaxis]


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
    bulbasaur = Pokemon()
    charmander = Pokemon()
    fight = Fight(bulbasaur, charmander)
    print fight.get_info()
    while not fight.is_over():
        fight.attack(random.randint(0, 3))
        time.sleep(1)
    return


if __name__ == "__main__":
    main()
