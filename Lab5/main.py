# import Task2

import Game_Creatures


def main():
    #     def __init__(self, name: str, strength: int, health: int, dexterity: int, armor: int):
    shaman = Game_Creatures.GoblinShaman("Shaman goblin", 10, 100, 5, 5, physical_reduction=0.2, mana=100,
                                         damage_spells={"fireball": [10, 25]})

    print(shaman.__name__())

    print('Is goblin = {}'.format(issubclass(shaman.__class__, (Game_Creatures.Goblin))))


if __name__ == '__main__':
    main()
