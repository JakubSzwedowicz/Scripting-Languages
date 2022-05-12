# Author: Jakub Szwedowicz
# Date: 12.05.2022
# e-mail: kuba.szwedowicz@gmail.com

from console import print_choice_menu, get_integer, get_string
from logger import Logger


class LogicImpl:
    def __init__(self):
        self._request = TaskRequest()
        self._file_data = []
        self._working = True
        self._settings = None
        self._logger = Logger()

    def run(self):
        while self._working:
            print_choice_menu()
            self.get_input()

    def get_input(self):
        input = get_integer(message='Choice')
        if input == 1:
            filename = get_string(message='Filename')
            self.load_data(filename)
            self._logger.log_info(f'Filename "{filename}" with data loaded.')
        elif input == 2:
            filename = get_string(message='Log filename')
            self._logger.set_logger_file(filename)
        elif input == 3:
            query_str = get_string(message='Query string')
            self._request.add_cmd(query_str)
            self._logger.log_info(f'Query "{query_str}" inserted.')
        elif input == 4:
            print(self._request.get_execution_sequence())

        self.check_for_actions()


'''
dateRep	day	month	year	cases	deaths	countriesAndTerritories	geoId	countryterritoryCode	popData2019	continentExp	Cumulative_number_for_14_days_of_COVID-19_cases_per_100000
25.11.2020	25	11	2020	185	13	Afghanistan	AF	AFG	38041757	Asia	7,1999829
'''
def load_data(self, filename: str) -> None:
    try:
        with open(filename, 'r') as file:
            next(file)
            for line in file.readlines():
                data = line.split()
                date = data[0]
                d, m, y, cases, deaths = map(int, data[1:6])
                country, geoID, country_code = data[6:9]
                population = map(int, data[9: 10])
                continent = data[10]
                covid_ratio = float(data[11])
                record = self.__parse_data_tokens(tokens)

                if record:
                    self._file_data.append(record)
                    available_countries.add(tokens[DEFAULT_COUNTRY_INDEX].lower())
                    available_continents.add(
                        tokens[DEFAULT_CONTINENT_INDEX].lower()
                    )
        except:
            return