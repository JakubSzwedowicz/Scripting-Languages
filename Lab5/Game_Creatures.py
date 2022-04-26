import random


class Creature:
    _object_ID = 0

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
        self._health -= self._calculate_dmg(dmg)
        return self._health

    def _calculate_dmg(self, dmg: int) -> int:
        return max(0, (dmg - self._armor))

    def __name__(self):
        return 'Create of name = {0}'.format(self.__class__._object_ID)


class Spider(Creature):
    _object_ID = 1

    def __init__(self, *args, jump: int):
        super().__init__(*args)
        self.jump = jump

    @property
    def jump(self):
        return self._jump

    @jump.setter
    def jump(self, new_jump: int):
        if type(new_jump) != int:
            raise Exception("Jump attribute has to be of type int")
        else:
            self._jump = new_jump


class Goblin(Creature):
    _object_ID = 2

    def __init__(self, *args, physical_reduction: float):
        super().__init__(*args)
        self.physical_reduction = physical_reduction

    def _calculate_dmg(self, dmg: int) -> int:
        dmg = super()._calculate_dmg(dmg)
        return self.physical_reduction * dmg

    @property
    def physical_reduction(self):
        return self._jump

    @physical_reduction.setter
    def physical_reduction(self, new_physical_reduction: float):
        if type(new_physical_reduction) != float:
            raise Exception("Physical_reduction attribute has to be of type float")
        else:
            self._physical_reduction = new_physical_reduction


class Basilisk(Creature):
    _object_ID = 3

    def __init__(self, *args, jump: int):
        super().__init__(*args)
        self._strength = 1e3
        self.jump = jump

    def attack(self):
        return self._strength

    @property
    def jump(self):
        return self._jump

    @jump.setter
    def jump(self, new_jump: int):
        if type(new_jump) != int:
            raise Exception("Jump attribute has to be of type int")
        else:
            self._jump = new_jump


class GoblinShaman(Goblin):
    _object_ID = 4

    def __init__(self, *args, physical_reduction: float, mana: int, **damage_spells: dict):
        super().__init__(*args, physical_reduction=physical_reduction)
        self.mana = mana
        self.damage_spells = damage_spells

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana: int):
        if type(new_mana) != int:
            raise Exception("Mana attribute has to be of type int")
        else:
            self._mana = new_mana

    def cast_spell(self) -> int:
        spell = random.choice(list(self.damage_spells.values()))
        if self.mana - spell[0] >= 0:
            self.mana -= spell[0]
            return spell[1]
        return 0

    def attack(self):
        is_casting_spell = random.uniform(0, 100) > 50
        dmg = 0
        if is_casting_spell:
            dmg = self.cast_spell()
        else:
            dmg = super().attack()
        return dmg


class BlackSpider(Spider):
    _object_ID = 5

    def __init__(self, *args):
        super.__init__(*args)
