import sys
from business_logic import LogicImpl
from console import get_integer, get_string, print_choice_menu
from helpers import Settings, DataRecord, sort_data_record_date, sort_data_record_cases, sort_data_record_deaths
from gui import set_check_actions_callback, set_load_file_callback, set_new_command_callback, GUI

DEFAULT_DATE_INDEX = 0
DEFAULT_DAY_INDEX = 1
DEFAULT_MONTH_INDEX = 2
DEFAULT_YEAR_INDEX = 3
DEFAULT_CASES_INDEX = 4
DEFAULT_DEATHS_INDEX = 5
DEFAULT_COUNTRY_INDEX = 6
DEFAULT_CONTINENT_INDEX = 10


class App:
    def __init__(self):
        self._logic = LogicImpl()
        self._gui = GUI() if App._version_with_gui() else None

        # set_new_command_callback(self._request.add_cmd)
        # set_load_file_callback(self.load_data)
        # set_check_actions_callback(self.check_for_actions)

    @staticmethod
    def _version_with_gui() -> bool:
        return any(arg in sys.argv for arg in ['-g', '--gui'])



        self.set_continents(available_continents)
        self.set_countries(available_countries)

    def set_continents(self, continents):
        self._request.set_continents(continents)

    def set_countries(self, countries):
        self._request.set_countries(countries)

    def run(self):
        if self._gui:
            self._gui.run()
        else:
            self._logic.run()




    def terminate(self):
        self._should_terminate = True

    def parse_settings(self):
        queries = self._request.get_execution_sequence()
        self._settings = Settings()

        if not self._settings.add_new_config(queries):
            return False

        return True

    def get_valid_records(self):
        sum = 0
        valid_records = []
        for record in self._file_data:
            if record.is_valid(self._settings):
                valid_records.append(record)
                if self._settings.type == "deaths":
                    sum += record.get_deaths()
                else:
                    sum += record.get_cases()

        if self._settings.sort_type:
            valid_records = self.sort_data(valid_records)
        return valid_records

    def show_data(self):
        valid_records = self.get_valid_records()
        for record in valid_records:
            log_info(str(record))
        if self.__settings.total:
            log_info(f"Total value for {self.__settings.type}: {sum}")
        if self.__gui:
            self.__gui.add_text_to_main_area(valid_records)

    def sort_data(self, data):
        reverse = False if self.__settings.sort_order == "ascending" else True
        if self.__settings.sort_type:
            if self.__settings.sort_type == "date":
                return sorted(data, key=sort_data_record_date, reverse=reverse)
            if self.__settings.sort_type == "cases":
                return sorted(data, key=sort_data_record_cases, reverse=reverse)
            if self.__settings.sort_type == "deaths":
                return sorted(data, key=sort_data_record_deaths, reverse=reverse)

    def check_for_actions(self):
        if not self.__request.get_execution_sequence():
            return

        last_query = self.__request.get_execution_sequence()[-1]
        if last_query == "exit":
            self.terminate()
        elif last_query == "reset":
            self.__request.reset_sequence()
            self.__request.remove_last_query()
        elif last_query == "show":
            if self.parse_settings():
                self.show_data()
            self.__request.remove_last_query()

    def should_terminate(self):
        return self.__should_terminate

    def __parse_data_tokens(self, tokens):
        record = DataRecord()
        if len(tokens) < 11:
            return None

        return (
            record.add_date(tokens[DEFAULT_DAY_INDEX], tokens[DEFAULT_MONTH_INDEX])
                .add_day(tokens[DEFAULT_DAY_INDEX])
                .add_cases(tokens[DEFAULT_CASES_INDEX])
                .add_deaths(tokens[DEFAULT_DEATHS_INDEX])
                .add_country(tokens[DEFAULT_COUNTRY_INDEX])
                .add_continent(tokens[DEFAULT_CONTINENT_INDEX])
        )
