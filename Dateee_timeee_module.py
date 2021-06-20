import datetime

x = datetime.datetime.now()
#in x datetime object is stored
'''
datetime.datetime.now() attribute returns current date with accurate time 
in format 
2021-06-20 13:59:17.403459
year-month-day  hour:minute:second:millisecond
'''
print(x)

print(type(x))
#x here is datetime.datetime object

#there are a few attributes that can be passed in datetime.datetime() objects
print(x.year) #returns the no of year
print(x.month) #returns month
print(x.day) #returns no of day
print(x.time()) #returns time
print(x.ctime()) #returns date time in ctime format (weekday month day time year)
print(x.now()) #returns date and time
print(x.replace(year=2018)) #replace the year no with 2018


#if we dont pass .now attribute (which actually points in the current time) then we must pass arguments
#for year month day time to create a datetime.datetime object

y = datetime.datetime(year=2026, month= 1, day= 13, second=1)
'''
he datetime() class requires three parameters to create a date: year, month, day.
The datetime() class also takes parameters for time and timezone (hour, minute, 
second, microsecond, tzone), but they are optional, and has a default 
value of 0, (None for timezone).
'''
"""
While costumely creating datetime.datetime object , we arguments such as year month and day must
be passed compulsarily, while other arguments such as hour min and sec is not compulsari
if hour min and sec is not passed then by default it is 00:00:00
/
/
whereas if we any value to hour or min or sec argument then the value will be replaced whereas the 
one that arent passed will remain as 00
"""
print(y)


#strftime()
'''
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter
, format, to specify the format of the returned string:
'''
"""
strctime() attributes can be called with datetime.datetime
ojects. (i.e ) time in format year,month,day hour,min,sec,millisec,timezone

"""
print(y.strftime("%B"))
#%B means full name of month

print(y.strftime("%b"))
#%B means short name of month

print(y.strftime("%a"))
#%a means short name of weekday

print(y.strftime("%A"))
#%A means full name of month

print(y.strftime("%w"))
#%w means weekday as number 0 is sunday

print(y.strftime("%d"))
#%d means day of month

print(y.strftime("%m"))
#%m means month as number (01-12)

print(y.strftime("%y"))
#%y means short version of year like 19 for 2019

print(y.strftime("%Y"))
#%Y means full version of year like 2019

print(y.strftime("%H"))
#%H means no of hour (0-23)

print(y.strftime("%I"))
#%I means no of hour in 12 hour format (00-12)

print(y.strftime("%p"))
#%p means AM/PM

print(y.strftime("%M"))
#%M means no of minutes (00-59)

print(y.strftime("%S"))
#%S means no of seconds(00-59)

print(y.strftime("%f"))
#%f means no of microseconds (000000-999999)

print(y.strftime("%H"))
#%H means no of hour (0-23)

print(y.strftime("%j"))
#%j means no of day of the year(001-366) eg:276

print(y.strftime("%U"))
#%U means week no of year (00-53) sunday as a first day of week

print(y.strftime("%W"))
#%W means  week no of year (00-53) monday as a first day of week

print(y.strftime("%c"))
#%c means local version of date and time
#like that given by ctime() in time module
#mon jan 13 02:22:09 2019

print(y.strftime("%x"))
#%x means local version of date (12/22/20)mon-day-year

print(y.strftime("%X"))
#%X means local version of time (22:32:00) hour-min-sec

print(y.strftime("%H"))
#%H means no of hour (0-23)


####COnverting timestamp to datetime object and datetime obj to timestamp
from _datetime import datetime

now = datetime.now()
print(type(now)) #returns datetime.datetime obj

timestamp = datetime.timestamp(now)
print(type(timestamp))
print(timestamp)
#returns type float because timestamp is a float number

date_time_obj = datetime.fromtimestamp(timestamp)
print(type(date_time_obj))
#returns datetime.datetime object
print(date_time_obj)