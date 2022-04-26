# Author: Jakub Szwedowicz
# Date: 21.04.2022
# e-mail: kuba.szwedowicz@gmail.com
from timeit import default_timer
import platform
import psutil
import pandas as pd

all_cases = []
by_date = {}
by_country = {}

def modification():
    clear_data()
    task_1()

    int_entered = False
    length = 0
    while not int_entered:
        try:
            length = int(input('Enter the length of the tuple for all_cases you are going to print: '))
            if 0 <= length <= len(all_cases[0]):
                int_entered = True
            else:
                raise RuntimeError('Out of bound integer!')
        except ValueError:
            print('Please enter an integer! ')
        except RuntimeError as err:
            print(err)

    for data in all_cases:
        print(data[:length])


def task_1():
    clear_data()

    countries = ['aaa', 'aab', 'aac']
    years = [1111, 1112, 1113]
    months = [1, 2, 3]
    days = [11, 12, 13]
    deaths = [123, 124, 125]
    cases = [321, 432, 543]

    for i in range(0, len(countries)):
        all_cases.append((countries[i], years[i], months[i], days[i], deaths[i], cases[i]))
        by_date[(years[i], months[i], days[i])] = [(countries[i], deaths[i], cases[i])]
        by_country[countries[i]] = [(years[i], months[i], days[i], deaths[i], cases[i])]

    file_name = 'Covid.txt'
    with open(file_name, 'r') as f:
        next(f)
        for line in f:
            data = line.split()
            day, month, year, cases, deaths = map(int, data[1:6])
            country = data[6]
            all_cases.append((country, year, month, day, deaths, cases))
            if (year, month, day) in by_date:
                by_date[(year, month, day)].append((country, deaths, cases))
            else:
                by_date[(year, month, day)] = [(country, deaths, cases)]

            if country in by_country:
                by_country[country].append((year, month, day, deaths, cases))
            else:
                by_country[country] = [(year, month, day, deaths, cases)]


def task_2():
    @Timer
    def for_date_a(year, month, day):
        sum_deaths = 0
        sum_cases = 0
        for _, y, m, d, deaths, cases in all_cases:
            if y == year and m == month and d == day:
                sum_deaths += deaths
                sum_cases += cases
        return sum_deaths, sum_cases

    @Timer
    def for_date_d(year, month, day):
        sum_deaths = 0
        sum_cases = 0

        if (year, month, day) in by_date:
            for _, deaths, cases in by_date[(year, month, day)]:
                sum_deaths += deaths
                sum_cases += cases
        return sum_deaths, sum_cases

    @Timer
    def for_date_c(year, month, day):
        sum_deaths = 0
        sum_cases = 0

        for _, data in by_country.items():
            for y, m, d, deaths, cases in data:
                if y == year and m == month and d == day:
                    sum_deaths += deaths
                    sum_cases += cases
        return sum_deaths, sum_cases

    clear_data()
    task_1()
    print(for_date_a(2020, 9, 10))
    print(for_date_d(2020, 9, 10))
    print(for_date_c(2020, 9, 10))


def task_3():
    @Timer
    def for_country_a(country):
        sum_deaths = 0
        sum_cases = 0
        for c, _, _, _, deaths, cases in all_cases:
            if c == country:
                sum_deaths += deaths
                sum_cases += cases
        return sum_deaths, sum_cases

    @Timer
    def for_country_d(country):
        sum_deaths = 0
        sum_cases = 0

        for values in by_date.values():
            for c, deaths, cases in values:
                if c == country:
                    sum_deaths += deaths
                    sum_cases += cases
        return sum_deaths, sum_cases

    @Timer
    def for_country_c(country):
        sum_deaths = 0
        sum_cases = 0

        if country in by_country:
            for _, _, _, deaths, cases in by_country[country]:
                sum_deaths += deaths
                sum_cases += cases
        return sum_deaths, sum_cases

    clear_data()
    task_1()
    print(for_country_a('Afghanistan'))
    print(for_country_d('Afghanistan'))
    print(for_country_c('Afghanistan'))


def task_4():
    @Timer
    def for_date_country_a(year, month, day, country):
        sum_deaths = 0
        sum_cases = 0
        for c, y, m, d, deaths, cases in all_cases:
            if c == country and y == year and m == month and d == day:
                sum_deaths += deaths
                sum_cases += cases
        return sum_deaths, sum_cases

    @Timer
    def for_date_country_d(year, month, day, country):
        sum_deaths = 0
        sum_cases = 0

        if (year, month, day) in by_date:
            for c, deaths, cases in by_date[(year, month, day)]:
                if c == country:
                    sum_deaths += deaths
                    sum_cases += cases
        return sum_deaths, sum_cases

    @Timer
    def for_date_country_c(year, month, day, country):
        sum_deaths = 0
        sum_cases = 0

        if country in by_country:
            for y, m, d, deaths, cases in by_country[country]:
                if y == year and m == month and d == day:
                    sum_deaths += deaths
                    sum_cases += cases
        return sum_deaths, sum_cases

    clear_data()
    task_1()
    print(for_date_country_a(2020, 9, 10, 'Afghanistan'))
    print(for_date_country_d(2020, 9, 10, 'Afghanistan'))
    print(for_date_country_c(2020, 9, 10, 'Afghanistan'))


def task_5():
    def print_machine():
        print("=" * 40, "System Information", "=" * 40)
        uname = platform.uname()
        # OS
        print(f"System: {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        # CPU
        print("=" * 20, "CPU", "=" * 20)
        print(f"Processor: {uname.processor}")
        print(
            f"Number of physical and logical cores: ({psutil.cpu_count(logical=False)}, {psutil.cpu_count(logical=True)})")
        print(f"Current, Min and Max CPU frequency: ({psutil.cpu_freq()})")
        # Ram
        print("=" * 20, "RAM", "=" * 20)
        print(f"Total RAM installed: {round(psutil.virtual_memory().total / 1000000000, 2)} GB")
        print(f"Available RAM: {round(psutil.virtual_memory().available / 1000000000, 2)} GB")
        print(f"Used RAM: {round(psutil.virtual_memory().used / 1000000000, 2)} GB")

    print_machine()
    task_2()
    task_3()
    task_4()
    print(Timer.df)


def clear_data():
    all_cases.clear()
    by_date.clear()
    by_country.clear()


class Timer:
    columns_names = ['all_cases [ms]', 'by_date [ms]', 'by_country [ms]']
    data_counter = 0
    row_name = ''
    row_data = []
    # df = pd.DataFrame(columns=['year, month, day', 'country', 'year, month, day, country'], index=['all_cases', 'by_date', 'by_country'])
    df = pd.DataFrame(columns=columns_names)

    def __init__(self, function):
        self._f = function
        self._start = 0
        self._end = 0
        self._diff = 0

    def __call__(self, *args, **kwargs):
        self._start = default_timer()
        ret = self._f(*args, **kwargs)
        self._end = default_timer()
        self._diff = self._end - self._start
        self._log_data()

        print('Calling function {} took {} [ms]'.format(self._f.__name__, self._diff / 1e6))
        return ret

    def _log_data(self):
        if Timer.data_counter == 0:
            Timer.row_name = str(self._f.__code__.co_varnames[:self._f.__code__.co_argcount])

        Timer.row_data.append(self._diff * 1000)
        if Timer.data_counter == 2:
            Timer.df = pd.concat(
                [Timer.df, pd.DataFrame([Timer.row_data], index=[Timer.row_name], columns=Timer.columns_names)])
            Timer.row_data.clear()
            Timer.data_counter = 0
        else:
            Timer.data_counter += 1
