i = 0
while i < 10:  # while needs a condition
    print('i is now {}'.format(i))
    i += 1
    
    # continue statements is executed here at the background, condition is reassessed
# when the condition is not satisfied anymore, the while ends

available_exits = ['north', 'east', 'south']
chosen_exit = ''

while chosen_exit not in available_exits:  # while can work whit lists
    chosen_exit = input('Choose a direction: ')
    if chosen_exit == 'quit':
        print('Coward')
        break  # break command exits the while, regardless of the condition

# will be executed if the condition wasn't True
else:  # else is also executed when the while loop is finished due to not satisfying
    # the condition anymore once started, not because the while is been broken by a break
    # will also be executed if the while is never happening because of the condition being False from he beginning
    print('Escaped!')

while True:  # this will always execute
    x = input('Quit?').lower()
    if x == 'quit':
        break
