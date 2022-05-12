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


    def load_data(self, filename: str) -> None:
        available_continents = set()
        available_countries = set()
        try:
            with open(file_name, 'r') as file:
                for line in file.readlines()[skip:]:
                    tokens = line.split()
                    record = self.__parse_data_tokens(tokens)

                    if record:
                        self._file_data.append(record)
                        available_countries.add(tokens[DEFAULT_COUNTRY_INDEX].lower())
                        available_continents.add(
                            tokens[DEFAULT_CONTINENT_INDEX].lower()
                        )
        except:
            return