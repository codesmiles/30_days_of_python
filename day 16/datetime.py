# import datetime
# print(dir(datetime)) 
# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']



# from datetime import datetime
# # now = datetime.now()
# print(now)                      # 2021-07-08 07:34:46.549883
# day = now.day                   # 8
# month = now.month               # 7
# year = now.year                 # 2021
# hour = now.hour                 # 7
# minute = now.minute             # 38
# second = now.second
# timestamp = now.timestamp()
# print(day, month, year, hour, minute)
# print('timestamp', timestamp)
# print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)