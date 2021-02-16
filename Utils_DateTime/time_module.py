"""
The time module reads the system's clock.
The Unix epoch is a time reference commonly used in programming:
12 AM on January 1, 1970, Coordinated Universal Time (UTC).
"""
import time

# Times
print(time.localtime())  # local time - no @ will display current time, if @timestamp, will display accordingly
print(time.time())  # epoch timestamp - seconds until now since the start of the epoch

# strftime stands for string format time, method that print the time in a nicer way
print('The epoch of this system started at ' + time.strftime('%c', time.gmtime(0)))
print(time.gmtime())

# Convert a time expressed in seconds since the epoch to a string representing local time
print(time.ctime())

print('=' * 30)

# the next code counts the lapse time between the two inputs
input('Enter to start counting')
start_time = time.time()

for i in range(2):
    print('Tick . . .')
    # sleep function sets the code in standby for @seconds
    time.sleep(1)
    print('Tock . . .')
    time.sleep(1)

input('Enter to stop counting...')
end_time = time.time()

"""
Pressing Ctrl+C will not interrupt time.sleep() calls in IDLE.
IDLE waits until the entire pause is over before raising the KeyboardInterrupt exception.
To work around this problem, instead of having a single time.sleep(30) call to pause for 30 seconds,
use a for loop to make 30 calls to time.sleep(1)
"""

print('Started at ' + time.strftime('%X', time.localtime(start_time)) + ' local time')
print('Ended at ' + time.strftime('%X', time.localtime(end_time)) + ' local time')

print('=' * 30)

# Dates
time_here = time.localtime()
print('Year:', time_here[0])
print('Month:', time_here.tm_mon)  # because it's a named tuple, can be called through index or name

# strftime allow to set the desired displaying format
print('Local time is ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
