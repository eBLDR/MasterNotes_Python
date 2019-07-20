# Basic guide of random module.
import random

# random float value from [0.0 to 1.0)
ran_float = random.random()
print(ran_float)

# random integer value in range [min, max], both included
ran_int = random.randint(1, 4)
print(ran_int)

# random integer value in range ([start, stop), step)
print(random.randrange(5, 26, 5))

# random float value in range [start, stop]
print(random.uniform(1.0, 3.5))

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# shuffle(seq) will randomize the order of a sequence
print(abc)
print('Shuffling . . .')
random.shuffle(abc)
print(abc)

# choice(seq) returns one random element from sequence - supports (almost) any kind of object type
string = 'abcdefghijk'
print(random.choice(abc))
print(random.choice(string))

# sample(seq, n) will return a list with n random samples from sequence
ran_sample = random.sample(abc, 3)
print(ran_sample)
