#Q7. Generator and Datetime Module (3 Marks)
#Create a generator function that generates dates for the next 7 days starting f
#Use the datetime module.
#Sample Output:
#2026-11-19
#2026-11-20
#2026-11-21
#2026-11-22
#2026-11-23
#32026-11-24
from datetime import date,timedelta
def g():
    today=date.today()
    for i in range(7):
        yield today+timedelta(days=i)
for d in g():
    print(d)
