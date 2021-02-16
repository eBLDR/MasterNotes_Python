import datetime
from time import sleep

now = datetime.datetime.now()  # Returns information the local time at the moment of execution
print(now)
print(type(now))

print(now.date())  # Date only
print(now.time())  # Time only

# To combine date and time
print(datetime.datetime.combine(now.date(), now.time()))  # Merges date and time

utc_now = datetime.datetime.utcnow()  # utc time
print(utc_now)
print(utc_now.min.time())  # Today earliest
print(utc_now.max.time())  # Today latest

print(datetime.date.today())  # Only today's date

print('=' * 10)

# Specific calls
print('Year:', now.year)
print('Month:', now.month)
print('Day:', now.day)
print('Hour:', now.hour)
print('Minute:', now.minute)
print('Second:', now.second)
print('Weekday:', now.weekday())

# String format datetime
# Converting datetime object into str and personalize the format
datetime_to_str = now.strftime('%I:%M %p')
print(datetime_to_str)
print(type(datetime_to_str))

# Using ISO 8601 standard for time
print(datetime.datetime.now().isoformat())

"""
Datetime strftime/strptime directive

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

# String parse time
# Converting str into datetime object
oct_21 = datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
print(oct_21)
print(type(oct_21))

print('=' * 30)

# We can create date specific datetime objects
new_year_2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)  # @(y, m, d, h, m, s)

# Datetime objects can be compared
print(new_year_2016 < now)

print(new_year_2016.timestamp())  # Seconds since epoch

# Also from a timestamp
random_epoch = 10000
random_time = datetime.datetime.fromtimestamp(random_epoch)
print(random_time)

print('=' * 30)

# Using timedelta data type - it's  duration of time rather than a moment in time
delta = datetime.timedelta(weeks=0, days=11, hours=10, minutes=5, seconds=12, milliseconds=0, microseconds=1)
# there are no month and year argument because they don't have the same length throughout the calendar

print(delta)
print(delta.total_seconds())  # total seconds in the period

print(now + delta)  # we can perform date arithmetic

print('=' * 30)

# pausing until a specific date
future = datetime.datetime(2020, 1, 1, 0, 0, 0)
try:
    print('We are waiting until {}...\nPress Ctrl+C for Keyboard Interruption!'.format(future))
    while future > datetime.datetime.now():
        sleep(1)
    print('Welcome to the future!')
except KeyboardInterrupt:
    print('Interrupted - Sick of waiting.')
