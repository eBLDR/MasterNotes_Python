alpha_list = ['alpha', 'beta', 'gamma', 'delta']
for item in alpha_list:
    if item == 'gamma':
        print('I am ignoring ' + item)
        continue
        # keyword continue skips the code for that item and jumps to the
        # next item in the iteration

    print('I am ' + item)

for item in alpha_list:
    if item == 'gamma':
        print('I am ' + item + ' and I am breaking the loop')
        break
        # keyword break cuts and finishes the for iteration loop

    print('I am ' + item)

for item in alpha_list:
    if item == 'gamma':
        nasty_letter = item
        break
        # in this case break is good for stopping the iteration once
        # we've found what we were looking for

for item in alpha_list:
    if item == 'gamma':
        nasty_letter = item
        # break
else:
    # else block is only executed if the previous for loop hasn't
    # finished due to a break
    print('Gimme a word')
