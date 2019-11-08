# `while` loop represents an indefinite iteration

# i is the "iterator"
i = 0
while i < 10:  # while needs a expression - assessed as bool(expression)
    print('i is now {}'.format(i))
    i += 1

    # continue statement is executed here at the background,
    # expression is reassessed
# When the condition is not satisfied anymore, the loop ends

available_exits = ['north', 'east', 'south']
chosen_exit = ''

while chosen_exit not in available_exits:  # while can work whit lists
    chosen_exit = input('Choose a direction: ')
    if chosen_exit == 'quit':
        print('Coward')
        break  # break command exits the while, regardless of the condition

# else block will be executed if the condition was False
# or when the while loop is finished due to no longer satisfying the expression
# else block won't be run if the while is been broken by a break
else:
    print('Escaped!')

# This will always execute
while True:
    x = input('Quit?').lower()
    if x == 'quit':
        break
