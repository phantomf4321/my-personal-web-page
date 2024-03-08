from datetime import datetime

class Defaults:

    def get_current_time(self):
        date = datetime.now()
        date = date.strftime("%Y/%m/%d")

        return date