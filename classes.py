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

    def _draw_state(self):
        infos = [
            self.current.get_info(),
            self.opponent.get_info(),
        ]
        infos = np.asarray(infos)
        # print infos.size
        return infos

    def _get_reward(self):
        if self.opponent.currHP is 0:
            return 1
        elif self.current.currHP is 0:
            return -1
        return -0.1

    def _is_over(self):
        if self.current.currHP is 0:
            print "{} lost against {}".format(self.current.name, self.opponent.name)
            return True
        elif self.opponent.currHP is 0:
            print "{} won against {}".format(self.current.name, self.opponent.name)
            return True
        return False

    def observe(self):
        canvas = self._draw_state()
        return canvas.reshape((1, -1))

    def act(self, action):
        self._update_state(action)
        reward = self._get_reward()
        game_over = self._is_over()
        return self.observe(), reward, game_over

    def reset(self):
        self.current = Pokemon()
        self.opponent = Pokemon()


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
        return [
            self.pp,
            self.acc,
            self.power
        ]


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
