# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def task_1() -> None:
    products = {'Bread': [2, 23, 15],
                'Milk': [1, 0, 3],
                'Tomatoes': [1, 0, 20],
                'Eggs': [12, 0, 4],
                'Onions': [1, 23, 5],
                'Fisg': [2, 23, 60]}

    categories = ['Product', 'Amount', 'Vat', 'Price']
    for cat in categories:
        print('{0:25s}'.format(cat), end='')
    print('')
    for product, data in products.items():
        print('{0:25s}'.format(product), end='')
        for d in data:
            print('{0:25d}'.format(d), end='')
        print('')


def task_2() -> None:
    from Devices import Controller
    from datetime import time
    c = Controller()
    c._dayNightSensor._nightHours = [time(0), time(23)]
    c.auto = True
    for hour in range(0, 23):
        c._dayNightSensor._nightHours[0] = time(hour)
        c.update()
        print('Are lights turned off at {0} hour = {1}'.format(hour, c.lightsTurned))


def task_3() -> None:
    nUsers = 2
    emails = [input('Please input user email: ') for _ in range(0, nUsers)]

    domains = [domain.split('@')[1] for domain in emails]

    print('Users input {0} different domains: \n {1}'.format(len(domains), domains))


def findDiv(num):
    eveness = 2
    if num % eveness == 0: return eveness
    elif num == 1: return 0

    import math
    div = 3
    while div <= math.sqrt(num):
        if num % div == 0:
            return div
        div += 2
    return 0


def task_4() -> None:
    # First
    numbers = [19, 3, 15, 42, 98, 16, 9, 23, 4, 1]

    primes = []
    for maybePrime in numbers:
        div = findDiv(maybePrime)
        if div == 0:
            primes.append(maybePrime)
        else:
            print('Divisor for number {} is {}'.format(maybePrime, div))
    print('primes = {}'.format(primes))

    print('Default numbers =', numbers)
    # Second
    ascendingNumbers = sorted(numbers)
    print('Ascending = ', ascendingNumbers)
    descendingNumbers = sorted(numbers, reverse=True)
    print('Descending = ', descendingNumbers)

    # Third
    firstThreeSorted = sorted(numbers[0:3])
    print('First three sorted = ', firstThreeSorted)


def task_5():
    # simplified knapsack problem
    trucks = [[]]
    sizes = [12, 5, 8, 8, 23, 15, 7, 8, 9, 12, 34, 6, 9, 16, 8, 23, 12, 7, 5, 3]
    max_size = 100

    sizes.sort(reverse=True)
    for package in sizes:
        if max_size - package < 0:
            max_size = 100
            trucks.append([])
        max_size -= package
        trucks[-1].append(package)

    for t in trucks:
        print('Possible arrangement = ', t)

def task_6():
    from JSOS import JSOS
    jsos = JSOS()

    employees = 3
    for _ in range (0, employees):
        jsos.add_new()


def main():
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    task_5()
    task_6()


if __name__ == '__main__':
    main()
