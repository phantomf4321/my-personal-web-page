from datetime import datetime
date = datetime.now()

date = datetime.strptime(date, "%d/%m/%Y")
print(date)