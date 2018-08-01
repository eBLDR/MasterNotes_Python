# We are using Leibniz formula for Pi
# Pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 ...


def odd_numbers():
    n = 1
    while True:
        yield n
        n += 2


def pi_series():
    odds = odd_numbers()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        # we can have as many yield as desired, code will resume from last yield command
        approximation -= (4 / next(odds))
        yield approximation


approx_pi = pi_series()

for i in range(1000000):
    print(next(approx_pi))
