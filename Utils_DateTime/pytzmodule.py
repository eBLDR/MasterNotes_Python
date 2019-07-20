"""
All pytz's data comes from the IANA (Internet Assigned Numbers Authority)
Also known as Olser database
"""
import datetime  # datetime is in charge to print the data nicely

import pytz

utc_time = datetime.datetime.utcnow()

# Aware time, has tz info
# the method localize().astimezone() will find out what's the current time in the location
aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print('Aware local time {}, time zone {}'.format(aware_local_time, aware_local_time.tzinfo))
print('Aware UTC {}, time zone {}'.format(aware_utc_time, aware_utc_time.tzinfo))

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)  # tz for timezone, tzed is a type
print('Time in {} is {}'.format(country, local_time))
print('UTC is {}'.format(utc_time))

# print all the strings that pytz.timezone accepts
for x in pytz.all_timezones:
    print(x)

print('=' * 20)

# print all the countries with the corresponding ISO 3166-1 alpha-2
for x in sorted(pytz.country_names):  # pytz.country_names is a dictionary
    print(x + ': ' + pytz.country_names[x])
print('There are {} recognized territories'.format(len(pytz.country_names)))

print('=' * 20)

# to print all the timezone available in a country (if there are) with the current time
for x in sorted(pytz.country_names):
    print('{}: {}'.format(x, pytz.country_names[x]), end=': ')
    if x in pytz.country_timezones:  # pytz.country_timezones is also a dictionary
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print('\t\t{}: {}'.format(zone, local_time))
    else:
        print('\t\tNo time zone defined')
