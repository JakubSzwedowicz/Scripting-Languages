# Author: Jakub Szwedowicz
# Date: 31.03.2022
# e-mail: kuba.szwedowicz@gmail.com
from time import time_ns


def task_2():
    numbers = [x for x in range(0, 100000000)]
    # print(sum(numbers))
    sum = list_sum(numbers)
    print('Sum of numbers equals {0}'.format(sum))


class Timer:
    def __init__(self, func):
        self._func = func
        self._start = 0
        self._end = 0
        self._diff = 0

    def __call__(self, *args, **kwargs):
        self._start = time_ns()
        ret = self._func(*args, **kwargs)
        self._end = time_ns()
        self._diff = self._end - self._start
        print('Calling function took {0} [ms]'.format(self._diff / 1e6))
        return ret


@Timer
def list_sum(numers: list) -> int:
    return sum(numers)
