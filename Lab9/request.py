from enum import Enum
from typing import List
import datetime
import calendar

from pytz import country_timezones

DEFAULT_COUNTRY = "Poland"
DEFAULT_CONTINENT = "Europe"


class ParseError(Exception):
    pass


class Command(Enum):
    SET, TOTAL, DEATHS, CASES, SHOW, IN, ON, FROM, TILL, RESET, EXIT = range(0, 11)


class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


class Request:
    class Predicate:
        def __call__(self, *args, **kwargs) -> bool:
            pass

    class PredicateDate(Predicate):
        def __init__(self, first_day: datetime.date, last_day: datetime.date):
            self._first_day = first_day
            self._last_day = last_day

        def __call__(self, *args, **kwargs) -> bool:
            date: datetime.date = args[0]
            return self._first_day <= date <= self._last_day

    class PredicateTerritory(Predicate):
        def __init__(self, country: str, continent: str = None):
            self._country = country
            self._continent = continent

        def __call__(self, *args, **kwargs) -> bool:
            territory: str = args[0]
            return self._test_for_country_or_continent(self._country, territory) \
                   and self._test_for_country_or_continent(self._continent, territory)

        @staticmethod
        def _test_for_country_or_continent(valid: str, tested: str) -> bool:
            if valid:
                return tested == valid
            return True

    def __init__(self):
        self.total_on = False
        self._show_deaths = None
        self._commands_order: List[Request.Predicate] = []

    def reset_sequence(self):
        self._commands_order = []

    def _verify_record(self, record: list) -> bool:
        return all(pred(record) for pred in self._commands_order)

    def filter(self, records: List[list]) -> List[list]:
        filtered = []
        cases_or_deaths_index = 5 if self._show_deaths else 4
        for record in records:
            filtered.append(record) if self._verify_record(record) else None
        return filtered

    def print_cases_or_deaths(self, record: List[list]):
    # def get_execution_sequence(self):
    #     if self.__execution_sequence:
    #         return self.__execution_sequence
    #
    # def remove_last_query(self):
    #     if len(self.__execution_sequence) > 0:
    #         self.__execution_sequence = self.__execution_sequence[:-1]

    def add_command(self, query: str) -> None:
        cmds = [cmd.upper() for cmd in query.split()]

        i = 0
        if i < len(cmds):
            if cmds[i] == Command.SET.name:
                if i + 2 > len(cmds) or cmds[i + 1] != Command.TOTAL.name:
                    raise ParseError
                self._total_on = cmds[i + 2] == Command.ON.name
                i += 3
            elif cmds[i] == Command.SHOW.name:
                if i + 1 < len(cmds):
                    i += 1

                    if cmds[i] == Command.DEATHS.name or cmds[i] == Command.CASES.name:
                        self._show_deaths = cmds[i] == Command.DEATHS.name
                        i += 1
                    else:
                        while i + 1 < len(cmds):  # Show [cases|deaths] xxxxx
                            if cmds[i] == Command.IN.name:
                                i = self._parse_in(cmds, i + 1)
                            elif cmds[i] == Command.ON.name:
                                i = self._parse_on(cmds, i + 1)
                            elif cmds[i] == Command.FROM.name:
                                raise ParseError
                                #i = self._parse_from(cmds, i + 1)
        if i != len(cmds):
            raise ParseError

    def _parse_in(self, query: List[str], i: int) -> int:
        if query[i] in Month:
            month_number = list(calendar.month_name).index(query[i])
            self._commands_order.append(
                Request.PredicateDate(datetime.date(0, month_number, 0), datetime.date(0, month_number, 0)))
        else:  # Country
            self._commands_order.append(Request.PredicateTerritory(query[i]))
        return i + 1

    def _parse_on(self, query: List[str], i: int) -> int:
        if i + 1 >= len(query):
            raise ParseError

        if query[i] in Month:
            month_number = list(calendar.month_name).index(query[i])
            if 0 < int(query[i + 1]) < calendar.monthrange(2020, month_number)[1]:
                self._commands_order.append(Request.PredicateDate(datetime.date(0, month_number, int(query[i + 1])),
                                                                  datetime.date(0, month_number, int(query[i + 1]))))
                return i + 2
        raise ParseError


    def parse_sort(tokens):
        order = None
        data_type = None
        tokens_to_skip = 1

        if len(tokens) > 0:
            if tokens[0] == "date" or tokens[0] == "deaths" or tokens[0] == "cases":
                data_type = tokens[0]

        if len(tokens) > 1:
            if tokens[1] == "ascending" or tokens[1] == "descending":
                order = tokens[1]
                tokens_to_skip = 2

        return (tokens[tokens_to_skip:], [("sort_type", data_type), ("sort_order", order)])

