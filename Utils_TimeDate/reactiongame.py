# REACTION GAME
import random
import time
from time import perf_counter as my_timer  # to rename a method in a more handy way
# perf_counter is a more precise counter than time(), is also monotonic,
# which means that time can only go in one direction
# perf_counter is actually a second counter that starts as soon the computer is turned on

waitTime = random.randint(1, 5)
input("REACTION GAME! Enter when you are ready")
time.sleep(waitTime)
start_time = my_timer()
input('ENTER!')
end_time = my_timer()

print('Your reaction time was {:6.4} seconds'.format(end_time - start_time))
# print(start_time, end_time)
print("=" * 30)

# CPU PROCESSING TIME
# time that the cpu is processing reading our code
from time import process_time as pt

cpuStart = pt()
for i in range(10000):
    j = 2 ** i
cpuEnd = pt()
print(cpuStart)
print(cpuEnd)
