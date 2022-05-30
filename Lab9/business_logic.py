# Author: Jakub Szwedowicz
# Date: 12.05.2022
# e-mail: kuba.szwedowicz@gmail.com
import datetime
from datetime import date
from console import print_choice_menu, get_integer, get_string
from logger import Logger
from request import Request


class LogicImpl:
    def __init__(self):
        self._request = Request()
        self._file_data = []
        self._filtered = []
        self._available_countries = set()
        self._available_continents = set()
        self._working = True
        self._settings = None
        self._logger = Logger()

    def run(self):
        while self._working:
            print_choice_menu()
            self.get_input()

    def get_input(self):
        input = get_integer(message='Choice')
        if input == 0:
            self._working = False
        elif input == 1:
            # filename = get_string(message='Filename')
            filename = 'Covid.txt'
            self.load_data(filename)
            self._logger.log_info(f'Filename "{filename}" with data loaded.')
        elif input == 2:
            filename = get_string(message='Log filename')
            self._logger.set_logger_file(filename)
        elif input == 3:
            query_str = get_string(message='Query string')
            self._request.add_command(query_str)
            self._logger.log_info(f'Query "{query_str}" inserted.')
        elif input == 4:
            self._filtered = self._request.filter(self._file_data)
            print(*self._filtered, sep='\n')

        # self.check_for_actions()

    '''
    dateRep	day	month	year	cases	deaths	countriesAndTerritories	geoId	countryterritoryCode	popData2019	continentExp	Cumulative_number_for_14_days_of_COVID-19_cases_per_100000
    25.11.2020	25	11	2020	185	13	Afghanistan	AF	AFG	38041757	Asia	7,1999829
    '''

    def load_data(self, filename: str) -> None:
        try:
            with open(filename, 'r') as file:
                next(file)
                data_dummies = [[0, 0, 0], 0, 0, 0, 0, 0, 'N/D', 'N/D', 'N/D', 0, 'N/D', '0,0']
                target_length = len(data_dummies)
                for line in file.readlines():
                    data = line.split()
                    data = data[:target_length] + data_dummies[len(data): target_length]
                    # (abc := data[0].split('.')).reverse()
                    (date := data[0].split('.')).reverse()
                    date = datetime.date(*map(int, date))
                    d, m, y, cases, deaths = map(int, data[1:6])
                    country, geoID, country_code = data[6:9]
                    population = data[9]
                    continent = data[10]
                    covid_ratio = float(data[11].replace(',', '.'))

                    record = [date, d, m, y, cases, deaths, country, geoID, country_code, population, continent,
                              covid_ratio]
                    self._file_data.append(record)
                    self._available_countries.add(country.lower())
                    self._available_continents.add(continent.lower())
        except IOError as ex:
            print(ex)
        return


def _parse_data_tokens(self, *tokens) -> list:
    pass
