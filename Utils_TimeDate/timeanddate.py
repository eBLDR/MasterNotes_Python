"""
The time module reads the system's clock.
The Unix epoch is a time reference commonly used in programming:
12 AM on January 1, 1970, Coordinated Universal Time (UTC).
"""

import time

print("\nUSING TIME\n")

# TIMES
print(time.localtime())     # local time - no @ will display current time, if @timestamp, will display accordingly
print(time.time())          # epoch timestamp - seconds until now since the start of the epoch
# strftime stands for string format time, method that print the time in a nicer way
print('The epoch of this system started at ' + time.strftime('%c', time.gmtime(0)))
print(time.gmtime())

print('=' * 30)

# the next code counts the lapse time between the two inputs
input('Enter to start counting')
startTime = time.time()

for i in range(2
               ):
    print('Tick . . .')
    # sleep function sets the code in standby for @seconds
    time.sleep(1)
    print('Tock . . .')
    time.sleep(1)

input('Enter to stop counting...')
endTime = time.time()

"""
Pressing CTRL-C will not interrupt time.sleep() calls in IDLE.
IDLE waits until the entire pause is over before raising the KeyboardInterrupt exception.
To work around this problem, instead of having a single time.sleep(30) call to pause for 30 seconds,
use a for loop to make 30 calls to time.sleep(1)
"""

print('Started at ' + time.strftime('%X', time.localtime(startTime)) + ' local time')
print('Ended at ' + time.strftime('%X', time.localtime(endTime)) + ' local time')

print('=' * 30)

# DATES
timeHere = time.localtime()
print('Year:', timeHere[0])
print('Month:', timeHere.tm_mon)  # because it's a named tuple, can be called through index or name

# strftime allow to set the desired displaying format
print('Local time is ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

import datetime

print("\nUSING DATETIME\n")

now = datetime.datetime.now()  # returns information about time at the moment of execution
print(now)
print(type(now))

# specific calls
print('Year:', now.year)
print('Month:', now.month)
print('Day:', now.day)
print('Hour:', now.hour)
print('Minute:', now.minute)
print('Second:', now.second)

# using strftime() to convert datetime into str and personalize the format
datetime_to_str = now.strftime('%I:%M %p')
print(datetime_to_str)
print(type(datetime_to_str))

"""
Datetime strftime directive

%Y - Year with century, as in '2014'
%y - Year without century, '00' to '99' (1970 to 2069)
%m - Month as a decimal number, '01' to '12'
%B - Full month name, as in 'November'
%b - Abbreviated month name, as in 'Nov'
%d - Day of the month, '01' to '31'
%j - Day of the year, '001' to '366'
%w - Day of the week, '0' (Sunday) to '6' (Saturday)
%A - Full weekday name, as in 'Monday'
%a - Abbreviated weekday name, as in 'Mon'
%H - Hour (24-hour clock), '00' to '23'
%I - Hour (12-hour clock), '01' to '12'
%M - Minute, '00' to '59'
%S - Second, '00' to '59'
%p - 'AM' or 'PM'
%% - Literal '%' character
"""

# converting str into datetime object
oct_21 = datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
print(oct_21)
print(type(oct_21))

print('=' * 30)

# we can create date specific datetime objects
newyear2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)  # @(y, m, d, h, m, s)
print(newyear2016 < now)

# also from a timestamp
random_epoch = 10000
random_time = datetime.datetime.fromtimestamp(random_epoch)
print(random_time)

print('=' * 30)

# using timedelta data type - it's  duration of time rather than a moment in time
delta = datetime.timedelta(weeks=0, days=11, hours=10, minutes=5, seconds=12, milliseconds=0, microseconds=1)
# there are no month and year argument because they don't have the same length throughout the calendar

print(delta)
print(delta.total_seconds())  # total seconds in the period

print(now + delta)  # we can perform date arithmetic

print('=' * 30)

# pausing until a specific date
future = datetime.datetime(2020, 1, 1, 0, 0, 0)
try:
    print("""We are waiting until {}...
    Press Ctrl+C for Keyboard Interruption!""".format(future))
    while future > datetime.datetime.now():
        time.sleep(1)
    print('Welcome to the future!')
except KeyboardInterrupt:
    print('Interrupted - Sick of waiting.')
