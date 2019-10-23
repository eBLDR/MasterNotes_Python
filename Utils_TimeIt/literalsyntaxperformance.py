from timeit import timeit

reps = 10000000

print('Performing {} repetitions...\n'.format(reps))

set_constructor = timeit('s = set([0, 1, 2])', number=reps)
set_literal = timeit('s = {0, 1, 2}', number=reps)

print('Set built-in constructor took {:.3} seconds.'.format(set_constructor))
print('Set literal syntax took {:.3} seconds.'.format(set_literal))

print('=' * 30)

dict_constructor = timeit('s = dict(zero=0, one=1, two=2)', number=reps)
dict_literal = timeit("s = {'zero': 0, 'one': 1, 'two': 2}", number=reps)

print('Dict built-in syntax took {:.3} seconds.'.format(dict_constructor))
print('Dict literal syntax took {:.3} seconds.'.format(dict_literal))

print('=' * 30)

list_constructor = timeit('s = list((0, 1, 2))', number=reps)
list_literal = timeit('s = [0, 1, 2]', number=reps)

print('List built-in syntax took {:.3} seconds.'.format(list_constructor))
print('List literal syntax took {:.3} seconds.'.format(list_literal))
