# Author: Jakub Szwedowicz
# Date: 17.03.2022
# e-mail: kuba.szwedowicz@gmail.com

from datetime import datetime


def task():
    todays_date = datetime.today()
    end_of_curr_year = datetime(todays_date.year, month=12, day=31)
    days_to_end_of_year = (end_of_curr_year - todays_date)

    print('Days to the end of year:', days_to_end_of_year.days)

    print('There are {0} days '
          'or {1} hours '
          'or {2} minutes'
          ' till the end of year'.format(days_to_end_of_year.days,
                                         24 * days_to_end_of_year.days,
                                         24 * 60 * days_to_end_of_year.days))
