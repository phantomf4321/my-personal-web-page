from datetime import datetime

class Defaults:

    def get_current_time():
        date = datetime.now()
        date = date.strftime("%Y/%m/%d")

        return date


D1 = Defaults
print(D1.get_current_time())