import time
# perf_counter is a more precise counter than time(), it's also monotonic,
# which means that time can only go in one direction
# perf_counter is actually a second counter that starts as soon the computer is turned on

print('time():', time.time())
print('perf_counter()', time.perf_counter())

print('=' * 20)

# CPU PROCESSING TIME
# Time that the cpu takes for processing the code
cpu_start = time.process_time()

for i in range(10000):
    j = 2 ** i
cpu_end = time.process_time()

print(cpu_start)
print(cpu_end)

