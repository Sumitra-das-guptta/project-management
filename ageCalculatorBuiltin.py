from datetime import datetime
from dateutil import relativedelta


def age_calculator(date1, date2):
    diff = relativedelta.relativedelta(date2, date1)
    
    years = diff.years
    months = diff.months
    days = diff.days
    
    print('{} years {} months {} days'.format(years, months, days))
    
date1 = datetime(2021, 3, 15)
date2 = datetime(2026, 3, 14)
age_calculator(date1, date2)
