import string
import random
import time  # importing time is an optional feature

# valid characters
possible_characters = string.ascii_letters + string.digits + \
                      string.punctuation + ' '

while True:
    target = input('Enter target text: ')
    if target:
        break
    else:
        print('Must be something, anything, but something!')

# setting first combination
attempt_this = ''.join(random.choice(possible_characters)
                       for i in range(len(target)))

generation = 0  # counting number of attempts

completed = False

while not completed:
    print(attempt_this)
    attempt_next = ''
    completed = True
    for i in range(len(target)):
        if attempt_this[i] != target[i]:
            completed = False
            attempt_next += random.choice(possible_characters)
        else:
            attempt_next += target[i]
    generation += 1
    attempt_this = attempt_next
    time.sleep(0.01)  # to make it look cool

print('Target matched! It took {} generation/s!'.format(generation))
