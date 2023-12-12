#Current Date and Time (datetime.datetime.now()):
from datetime import datetime
current_datetime = datetime.now()
print(current_datetime) #2023-11-02 15:04:10.549369

#--------------------------------------------
#Date Formatting:
from datetime import datetime
current_datetime = datetime.now()
formatted_date = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_date) #2023-11-02 15:04:10

#--------------------------------------------
#Date Arithmetic:
from datetime import datetime, timedelta
current_datetime = datetime.now()
one_day = timedelta(days=1)
yesterday = current_datetime - one_day
print(yesterday) #2023-11-01 15:04:10.549369


#--------------------------------------------
#Parsing Dates from Strings:
from datetime import datetime
date_string = '2023-11-02'
parsed_date = datetime.strptime(date_string, '%Y-%m-%d')
print(parsed_date)#2023-11-02 00:00:00

#--------------------------------------------
#Date Components (year, month, day, hour, minute, second):
from datetime import datetime
current_datetime = datetime.now()
year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
hour = current_datetime.hour
minute = current_datetime.minute
second = current_datetime.second
print(year, month, day, hour, minute, second) #2023 11 2 15 4 10

#--------------------------------------------
#Date Comparison:
from datetime import datetime
date1 = datetime(2023, 11, 1)
date2 = datetime(2023, 11, 2)
if date1 < date2:
    print("date1 is earlier than date2")# date1 is earlier than date2
    
#--------------------------------------------
    
#Date Range (datetime.timedelta):
from datetime import datetime, timedelta
start_date = datetime(2023, 11, 1)
end_date = start_date + timedelta(days=7)
print(start_date, end_date)#2023-11-01 00:00:00 2023-11-08 00:00:00
#--------------------------------------------

#Weekday (0 = Monday, 6 = Sunday):
from datetime import datetime
current_datetime = datetime.now()
weekday = current_datetime.weekday()
print("Weekday:", weekday) #Weekday: 3
#--------------------------------------------