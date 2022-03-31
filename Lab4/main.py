from Devices import Controller
from Calculator import Calculator
from Game import Creature

def main():
    # task1()
    task2()
    task3()


def task1():
    list_dev = [Controller(auto=False) for x in range(0, 4)]

    for i in range(0, 4):
        print('Devices: ', list_dev[i])
        setattr(list_dev[i], 'number', i)
        list_dev[i].auto = True

    print('Device [1] after the change of "auto": ', list_dev[1])


def task2():
    cal = Calculator(0.3)
    price = 100
    usd_eu_without_cut = cal.calculate_price_usd_eu(price)
    usd_eu_with_cut = cal.calculate_price_usd_eu_with_shops_cut(price)
    print('Price {0} PLN \nWithout the cut: {1:.2f} USD and {2:.2f} EU\n, with the cut: {3:.2f} USD and {4:.2f} EU.'.format(
        price, usd_eu_without_cut[0], usd_eu_without_cut[1], usd_eu_with_cut[0], usd_eu_with_cut[1]))

    products = {'Bike': 1000, 'Towel': 100, 'Keyboard': 250}
    products_prices = []
    for k, v in products.items():
        usd_eu_without_cut = cal.calculate_price_usd_eu(v)
        usd_eu_with_cut = cal.calculate_price_usd_eu_with_shops_cut(v)
        products_prices.append([k, usd_eu_without_cut, usd_eu_with_cut])


def task3():
    c1 = Creature(name='Goblin1', strength=10, dexterity=20, health=100, armor=5)
    c2 = Creature(name='Goblin2', strength=10, dexterity=20, health=100, armor=5)
    c3 = Creature(name='Spider1', strength=10, dexterity=20, health=100, armor=5)

    print('Move equals: ', c1.move())
    print('{0} has {1} hp left'.format(c2.name, c2.take_dmg(c1.attack())))


if __name__ == '__main__':
    main()
