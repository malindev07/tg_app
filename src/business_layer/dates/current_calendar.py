import calendar as c
import locale

from dataclasses import dataclass, field
from datetime import datetime
from textwrap import indent

from src.business_layer.dates.weekday import NUM_WEEK_DAY

locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")


@dataclass
class CurrentCalendar:

    current_calendar: dict[str, dict[int, str]] = field(default_factory=dict)
    current_year: int = field(default=datetime.now().year)

    def set_current_calendar(self):

        months = list(c.month_name)

        for num_month in range(1, 13):
            month = months[num_month]
            inner_days = c.monthcalendar(self.current_year, num_month)

            for days in inner_days:
                for day in range(len(days)):
                    if days[day] != 0:

                        if month not in self.current_calendar:
                            self.current_calendar[month] = {
                                days[day]: NUM_WEEK_DAY[day]
                            }
                        else:
                            self.current_calendar[month][days[day]] = NUM_WEEK_DAY[day]

    def get_current_calendar(self):
        print(self.current_calendar)
        return self.current_calendar


test = CurrentCalendar()

test.set_current_calendar()
test.get_current_calendar()
