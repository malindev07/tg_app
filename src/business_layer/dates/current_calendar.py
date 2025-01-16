import calendar as c
import locale

from dataclasses import dataclass, field
from datetime import datetime
from weekday import NUM_WEEK_DAY


@dataclass
class CurrentCalendar:

    month_dates: dict[str, list[list[int]]] = field(default_factory=dict)
    current_year: int = field(default=datetime.now().year)

    def set_month_dates(self):
        locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

        for i in range(1, 13):
            self.month_dates[list(c.month_name)[i]] = c.monthcalendar(
                self.current_year, i
            )


# test = CurrentCalendar()
# test.set_month_dates()
#
# # print(test.month_dates)
# print(datetime.now().month)
#
# for item in test.month_dates["Февраль"]:
#     for elem in range(len(item)):
#         print(NUM_WEEK_DAY[elem], item[elem])
