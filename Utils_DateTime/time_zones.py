"""
There are two types of datetime objects:
- Naive, they do not contain information about timezones
- Aware, they do contain information about timezones

A time zone's offset refers to how many hours the timezone is from UTC.
"""
import datetime
import time

print('USING TIME\n')

# GMT (Greenwich Mean Time) is a timezone
print(time.gmtime(0))  # beginning of the epoch

time_zone_offset = time.timezone  # Offset of the local (non-DST) timezone
time_zone_offset_dst = time.altzone  # Offset of the local (DST) timezone

print(f'Non-DST offset: {time_zone_offset}')
print(f'DST offset: {time_zone_offset_dst}')
print(f'Current time zone: {time.tzname[0]}')

# DST (Daylight Saving Time)
print(f'DST: {time.daylight}')

if time.daylight != 0:
    print('\tDST is in effect for this location.')
    print(f'\tDST timezone: {time.tzname[1]}')

# UTC (Coordinated Universal Time) is a time standard
# Aka Zulu Time (military and navigation)
# strftime() method allows to set the displaying format
print('\nLocal time: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print('UTC time: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

print('=' * 30)
print('USING DATETIME\n')

# Naive time, has no timezone info
local_time_naive = datetime.datetime.now()

print(f'Naive local time: {local_time_naive}')
print(f'Naive local time tzinfo: {local_time_naive.tzinfo}')

# Aware time, has tz info
local_timezone = datetime.timezone(datetime.timedelta(seconds=time.altzone))
print(f'Local timezone: {local_timezone}')

local_time_aware = local_time_naive.astimezone(tz=local_timezone)
print(f'Aware local time: {local_time_aware}')
print(f'Aware local time tzinfo: {local_time_aware.tzinfo}')

utc_time_naive = datetime.datetime.utcnow()
print(f'\nNaive UTC {utc_time_naive}')

# Timezone for UTC
utc_timezone = datetime.timezone.utc
print(utc_timezone)

utc_time_aware = utc_time_naive.astimezone(tz=utc_timezone)
print(f'Aware UTC: {utc_time_aware}')

print('=' * 30)

# Conversion from local to UTC
my_time = datetime.datetime(2020, 12, 12, 5, 12, 24, tzinfo=local_timezone)
print(f'My time in local: {my_time}')
my_time_utc = my_time.astimezone(tz=utc_timezone)
print(f'My time in UTC: {my_time_utc}')
