from datetime import datetime
week1 = "12-31-2022 00:00:00"
date_time_obj = str(datetime.strptime(week1,"%m-%d-%Y %H:%M:%S").date())
print(type(date_time_obj))
