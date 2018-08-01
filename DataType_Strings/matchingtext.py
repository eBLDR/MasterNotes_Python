import string
import random
import time  # importing time is an optional feature

# valid characters
possibleCharacters = string.ascii_letters + string.digits + string.punctuation + ' '

while True:
    target = input("Enter target text: ")
    if target:
        break
    else:
        print("Must be something, anything, but something!")

# setting first combination
attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))

generation = 0  # counting number of attempts

completed = False

while not completed:
    print(attemptThis)
    attemptNext = ''
    completed = True
    for i in range(len(target)):
        if attemptThis[i] != target[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += target[i]
    generation += 1
    attemptThis = attemptNext
    time.sleep(0.01)  # to make it look cool

print("Target matched! It took {} generation/s!".format(generation))
