# NumPy arrays of n-dimensions
# by default, the items are float
# elements inside the arrays are mutable, but not the dimension of the array

import numpy as np

# creating zero vector - @length of vector
zero_vector = np.zeros(5)
print(zero_vector)
print(type(zero_vector))
print(len(zero_vector))

# creating a zero matrix - (@rows, @columns)
zero_matrix = np.zeros((3, 4))
print(zero_matrix)
print(type(zero_matrix))

# similarly, create vectors/matrices of 1
one_vector = np.ones(4)
print(one_vector)

one_matrix = np.ones((3, 3))
print(one_matrix)

print("=" * 30)

# personalized arrays
x = np.array([1, 2, 3])
y = np.array([[0, 0, 1], [4, 5, 6], [7, 8, 9]])
print(x)
print(y)

print("=" * 20)

# indexing arrays and slicing arrays
# slices return a view object (shallow copy), index return a new object (deep copy)
print(y[1][1])
print(y[1][0:2])
print(y[1:])
print(y[:, 0])  # return the column at index
print(y[1, :])  # return the row at index

ind = [0, 2]
print(x[ind])  # return the items corresponding to the indexes

print("=" * 20)

# adding arrays - must have the same length
z = x + np.ones(len(x))
print(z)

print(z + 10)  # add 10 to each element

print(y[:, 0] + y[:, 2])  # adding the row 0 + row 2 - NOT CONCATENATING

print("=" * 20)

# boolean array (aka logical array)
b_array = x > 1
print(b_array)

print(x[x > 1])  # returns an array with the elements that satisfy the condition

print("=" * 20)

# transposing
y_T = y.transpose()
print(y_T)

print("=" * 20)
