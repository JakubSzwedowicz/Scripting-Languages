# Author: Jakub Szwedowicz
# Date: 10.03.2022
# e-mail: kuba.szwedowicz@gmail.com
import random
from datetime import datetime, time


class WeatherSensor:
    def __init__(self):
        self._isRaining = False
        self._isMisty = False

    def _update(self):
        self._isRaining = random.randint(0, 100) < 1
        self._isMisty = random.randint(0, 100) < 1

    def areBadConditions(self):
        self._update()
        return self._isRaining or self._isMisty


class DayNightSensor:
    def __init__(self):
        self._nightHours = [time(8), time(20)]
        self._currTime = None

    def _update(self):
        self._currTime = datetime.now().time()

    def isNight(self):
        self._update()
        return self._currTime < self._nightHours[0] or self._currTime > self._nightHours[1]


class Controller:
    def __init__(self, weatherSeonsor=WeatherSensor(), dayNightSensor=DayNightSensor()):
        self.lightsTurned = False
        self.auto = False
        self._weatherSensor = weatherSeonsor
        self._dayNightSensor = dayNightSensor

    def update(self):
        if self.auto and (self._weatherSensor.areBadConditions() or self._dayNightSensor.isNight()):
            self.lightsTurned = True

