import random, math

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
        pass

    def ability(self):
        return int(random.uniform(3, 18))


def modifier(constitution):
    return int(math.floor((constitution - 10) / 2))
