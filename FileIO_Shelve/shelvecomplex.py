import shelve

blt = ['bacon', 'lettuce', 'tomato', 'bread']
beansOnToast = ['beans', 'bread']
scrambledEggs = ['eggs', 'butter', 'milk']
soup = ['tin of soup']
pasta = ['pasta', 'cheese']

with shelve.open('recipes', writeback=True) as recipes:
    recipes['blt'] = blt
    recipes['beans on toast'] = beansOnToast
    recipes['scrambled eggs'] = scrambledEggs
    recipes['soup'] = soup
    recipes['pasta'] = pasta
    """
    # the next item won't be added to the file (unless writeback=True)
    recipes['blt'].append('butter')
    # if we wish to, we need to reassign the variable:
    temporary = recipes['blt']
    temporary.append('butter')
    recipes['blt'] = temporary
    
    OR
    
    passing writeback=True as a parameter will cause that items can be updated (once closed)
    this will take more disk usage and reduce the speed
    
    OR
    
    using .sync() method, that flushes the cache. Not recommended
    """
    recipes['soup'].append('croutons')

    for snack in recipes:
        print(snack, recipes[snack])
