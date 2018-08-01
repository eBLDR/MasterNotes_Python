import time

print('USING TIME\n')

# GMT (Greenwich Mean Time) is a timezone
print(time.gmtime(0))  # beginning of the epoch

print('The current time zone is {} with an offset of {}'.format(time.tzname[0], time.timezone))

# DST (Daylight Saving Time)
if time.daylight != 0:
    print('\tDST is in effect for this location')
    print('\tDST timezone is ' + time.tzname[1])

# UTC (Coordinated Universal Time) is a time standard
# Aka Zulu Time (military and navigation)
# strftime allow to set the displaying format
print('Local time is ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print('UTC time is ' + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

print('=' * 30)

"""
There are two datetime objects:
- Naive, they do not contain information about timezones
- Aware, they do contain information about timezones
"""

print("\nUSING DATETIME FOR NAIVE TIME\n")

import datetime

# Naive, has no timezone info
local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print('Naive local time {}'.format(local_time))
print('Naive UTC {}'.format(utc_time))

print("\nUSING PYTZ FOR AWARE TIME\n")

import pytz

# Aware, has tz info
# the method localize().astimezone() will find out what's the current time in the location
aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print('Aware local time {}, time zone {}'.format(aware_local_time, aware_local_time.tzinfo))
print('Aware UTC {}, time zone {}'.format(aware_utc_time, aware_utc_time.tzinfo))
