# Truth table generation - cartesian product
import itertools

values = [0, 1]
dimensions = 3

# product(A, B) is equivalent to the generator ((x,y) for x in A for y in B)
# repeat=n is equivalent to product(A, A, ... An)
truth_table = [i for i in itertools.product(values, repeat=dimensions)]
print(truth_table)

# Base n truth table
n = 3
values = [i for i in range(n)]
dimensions = 2

truth_table = [i for i in itertools.product(values, repeat=dimensions)]
print(truth_table)
