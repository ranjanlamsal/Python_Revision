import time

'''inside time module there is a time function that gives
no of ticks. 1 ticks = 1 sec
The time() function returns the number of seconds passed since epoch.

For Unix system, January 1, 1970, 00:00:00 at UTC is epoch (the point where time begins).

'''

#lets calculate no of ticks(seconds) taken by for loop and while loop
k = 0

initial_time = time.time()
#initial time is no of sec sinch epoc in this moment
while (k < 100):
    print("This is a loophole")
    k += 1
print("While loop ran in", time.time() - initial_time, "seconds")
#at this moment time.time - initial gives (no of sec since epoch in time moment - initial) = no of seconds for execution


initial2 = time.time()
for i in range(100):
    print("This is a loophole")
print("for loop ran in", time.time() - initial2, "seconds")

#here for loop run in time 0.002 sec and while loop run in time 0.0019 seconds


print(time.ctime(0))
'''.ctime() function gives the moment (date with exact time in readable day date and time format)
 when number of second (since epoch) is passed to it. while passing 0 it gives 1977 jan 1 00:00 
at gmt 00:00.
It can be referred as reverse of .time() function'''

print(time.ctime(time.time()))
#here time.time() returned the no of seconds passed since epoch till
# the moment and pass that value in ctime() function which again reversly
#convert no of sec since epoch to readable time format (day date and time)

time.sleep(1)
#The sleep() function suspends (delays) execution of the current thread for the given number of seconds.
#any code after that line will be executed after 10 seconds only


local_time = time.localtime()
'''The localtime() function takes the number of seconds passed
 since epoch as an argument and returns struct_time in local time.
 if no argument is passed to it then it takes time.time() as its argument i.e no of 
 epoch till the time of execution of code'''

print(local_time)

'''struct_time(time structure) is an object in struct_time class in python
which is nothing but a tuple representing time in year, month, day, week and soo on

time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27, 
                    tm_hour=6, tm_min=35, tm_sec=17, 
                    tm_wday=3, tm_yday=361, tm_isdst=0)
                    
Time structure (struct tm) contains a calendar date and time broken down into its components. The structure contains nine members of type int (in any order), which are:

Member  Type    Meaning Range
tm_sec  int seconds after the minute    0-61*
tm_min  int minutes after the hour  0-59
tm_hour int hours since midnight    0-23
tm_mday int day of the month    1-31
tm_mon  int months since January    0-11
tm_year int years since 1900    
tm_wday int days since Sunday   0-6
tm_yday int days since January 1    0-365
tm_isdst    (0 or 1 or neg 1)  int Daylight Saving Time flag
'''
'''
This period—often incorrectly called daylight savings time—begins 
at 2:00 a.m. local time on the second Sunday in March, 
when clocks spring forward an hour. 
Daylight saving time ends at 2:00 a.m. local time 
on the first Sunday in November, when clocks fall back by an hour.

'''

'''
Not this time structure (struct time) has a few attributes auch as
'''
print("year: ", local_time.tm_year)
print("month: ", local_time.tm_mon)
print("day of year: ", local_time.tm_yday)
print("day of month: ", local_time.tm_mday)
print("day of week: ", local_time.tm_wday)
print("hour passed: ", local_time.tm_hour)
print("minutes: ", local_time.tm_min)
print("seconds: ", local_time.tm_sec)
print("Is day light effect active ? : ", local_time.tm_isdst)



'''
time.mktime() known as make time

The mktime() function takes struct_time 
(or a tuple containing 9 elements corresponding to struct_time) 
as an argument and returns the seconds passed since 
epoch in local time. 
Basically, it's the inverse function of localtime()

'''

import time

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

local_time = time.mktime(t)
print("Local time:", local_time)

'''Python time.asctime()
it is same as mktime() but instead of no of seconds passed since it 
returns the readable date time format as string
it may be referred as combination of ctime() function and mktime() function
ctime(mktime(struct value 0r time touple)) = readable date time format
asctime(struct value or time touple) = readable date time format

 '''


'''
time.strftime()
The strftime() function takes struct_time 
(or tuple corresponding to it) as an argument and returns 
a string representing it based on the format code used. 
For example,
'''


named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)