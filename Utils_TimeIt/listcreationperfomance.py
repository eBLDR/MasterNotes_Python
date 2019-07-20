"""
The time it module can time profile the code - that is timing the execution time of specific blocks of code 
Other processes being executed at the same time can affect the results.
General consideration: do not include output in the snippets, print() is actually a very slow function.
"""
import timeit

# we're going to compare performance creating the same list using 2 different methods (append vs. comprehension)
# the code snippet must be converted into str, \ to avoid starting with a blank line

# setup variables, data that our code snippet needs
setup = """\
rng = 1000
"""

# the pass statement is added to fairly compared the generator performance
# snippet 1
list_append = """\
my_list = []
for i in range(rng):
    my_list.append(i)
for x in my_list:
    pass
"""

# snippet 2
list_comprehension = """\
my_list = [i for i in range(rng)]
for x in my_list:
    pass
"""

# snippet 3
list_generator = """\
my_list = (i for i in range(rng))
for x in my_list:
    pass
"""

# timeit function to measure the execution time of the code
# timeit('code_block', setup=variables_we_wish_to_use_also_as_str , timer=default_is_time.perf_counter,
# number=default_is_1000000, globals=namespace_scope)
# the function will automatically off garbage collection, if we wish to enable it,
# the first line of the snippet should be gc.enable()

repetitions = 30000

# we need to use a variable outside of the code block (rng), one option would be globals=globals()
# but this isn't recommended because was introduced after python 3.5, better option is to use setup

# Will return the execution time of the total number of repetitions (number=)
result_append = timeit.timeit(list_append, setup=setup, number=repetitions)

result_comprehension = timeit.timeit(list_comprehension, number=repetitions, setup=setup)

result_generator = timeit.timeit(list_generator, number=repetitions, setup=setup)

print('List append method:\t{} sec'.format(result_append))
print('List comprehension:\t{} sec'.format(result_comprehension))
print('List generator:\t\t{} sec'.format(result_generator))

print()
# repeat() - several runs, repeat=3 by default - returns a list of the times
repeat_generator = timeit.repeat(list_generator, setup=setup, number=repetitions, repeat=5)
print('Repeat generator:\t{}'.format(repeat_generator))
