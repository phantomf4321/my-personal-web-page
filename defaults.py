from datetime import datetime
from dateutil import relativedelta

class Defaults:

    def get_current_time():
        date = datetime.now()
        date = date.strftime("%Y/%m/%d")

        return date

    def claculate_age(self):
        cur_date = self.get_current_time()
        birth_date = "2001/03/25"
        start_date = datetime.strptime(birth_date, "%Y/%m/%d")
        end_date = datetime.strptime(cur_date, "%Y/%m/%d")

        # Get the relativedelta between two dates
        delta = relativedelta.relativedelta(end_date, start_date)
        print('Years, Months, Days between two dates is')
        print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')


D1 = Defaults
print(D1.get_current_time())