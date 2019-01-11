from timeit import timeit

reps = 10000000

print('Performing {} repetitions...\n'.format(reps))

set_function = timeit('s = set([0, 1, 2])', number=reps)
set_literal = timeit('s = {0, 1, 2}', number=reps)

print('Set built-in function construction took {} seconds.'.format(set_function))
print('Set literal syntax construction took {} seconds.'.format(set_literal))

print('=' * 30)

dict_function = timeit("s = dict([('zero', 0), ('one', 1), ('two', 2)])", number=reps)
dict_literal = timeit("s = {'zero': 0, 'one': 1, 'two': 2}", number=reps)

print('Dict built-in function construction took {} seconds.'.format(dict_function))
print('Dict literal syntax construction took {} seconds.'.format(dict_literal))

print('=' * 30)

list_function = timeit('s = list((0, 1, 2))', number=reps)
list_literal = timeit('s = [0, 1, 2]', number=reps)

print('List built-in function construction took {} seconds.'.format(list_function))
print('List literal syntax construction took {} seconds.'.format(list_literal))
