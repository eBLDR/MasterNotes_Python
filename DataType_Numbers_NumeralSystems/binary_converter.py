max_power = 11
powers = []

for power in range(max_power, -1, -1):  # backwards iteration
    powers.append(2 ** power)

print(powers)
x = int(input(f"Enter a number (< {2 ** max_power}): "))

b = ""

for power in powers:
    bit = x // power
    b += str(bit)
    x %= power

for i in range(len(b)):
    end_char = "" if (len(b) - i - 1) % 4 != 0 else " "
    print(b[i], end=end_char)
