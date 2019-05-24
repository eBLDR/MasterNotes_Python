"""
There are two types of datetime objects:
- Naive, they do not contain information about timezones
- Aware, they do contain information about timezones

A timezone's offset refers to how many hours the timezone is from UTC.
"""

import time
import datetime

print('USING TIME\n')

# GMT (Greenwich Mean Time) is a timezone
print(time.gmtime(0))  # beginning of the epoch

time_zone_offset = time.timezone  # Offset of the local (non-DST) timezone
time_zone_offset_dst = time.altzone  # Offset of the local (DST) timezone

print('Non-DST offset: {}'.format(time_zone_offset))
print('DST offset: {}'.format(time_zone_offset_dst))

print('T\nhe current time zone: {}'.format(time.tzname[0]))

# DST (Daylight Saving Time)
if time.daylight != 0:
    print('\tDST is in effect for this location')
    print('\tDST timezone: ' + time.tzname[1])

# UTC (Coordinated Universal Time) is a time standard
# Aka Zulu Time (military and navigation)
# strftime allow to set the displaying format
print('\nLocal time: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print('UTC time: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

print('=' * 30)
print('\nUSING DATETIME\n')

# Naive time, has no timezone info
local_time_naive = datetime.datetime.now()

print('Naive local time: {}'.format(local_time_naive))
print('Naive local time tzinfo: {}'.format(local_time_naive.tzinfo))

# Aware time, has tz info
local_timezone = datetime.timezone(datetime.timedelta(seconds=time.altzone))
print(local_timezone)

local_time_aware = local_time_naive.astimezone(tz=local_timezone)
print('Aware local time: {}'.format(local_time_aware))
print('Aware local time tzinfo: {}'.format(local_time_aware.tzinfo))

utc_time_naive = datetime.datetime.utcnow()
print('\nNaive UTC {}'.format(utc_time_naive))

# Timezone for UTC
utc_timezone = datetime.timezone.utc
print(utc_timezone)

utc_time_aware = utc_time_naive.astimezone(tz=utc_timezone)
print('Aware UTC: {}'.format(utc_time_aware))

print('=' * 30)

# Conversion from local to utc
my_time = datetime.datetime(2020, 12, 12, 5, 12, 24, tzinfo=local_timezone)
print('My time in local: {}'.format(my_time))
my_time_utc = my_time.astimezone(tz=utc_timezone)
print('My time in UTC: {}'.format(my_time_utc))
