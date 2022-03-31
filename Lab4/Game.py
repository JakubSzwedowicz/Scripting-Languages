import random


class Creature:
    __object_ID = 0

    def __init__(self, name: str, strength: int, health: int, dexterity: int, armor: int):
        self.name = name
        self._strength = strength
        self._dexterity = dexterity
        self._health = health
        self._armor = armor

    def attack(self):
        return random.uniform(0, 1) * self._strength

    def move(self):
        return self._dexterity

    def take_dmg(self, dmg: int) -> int:
        self._health -= max(0, (dmg - self._armor))
        return self._health
