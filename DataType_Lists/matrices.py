# Lists can be nested, that is called matrix
nested_list = [[0, 1], [10, 11], [100, 111]]
print(nested_list)
print(nested_list[0], nested_list[1][1])  # Use multiple index to refer a specific item

# Create matrix
matrix = []
n = 3

# Method 1
for i in range(n):
    matrix += [[0] * n]

print(matrix)

# Method 2
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    matrix.append(row)

print(matrix)

# Method 3
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(0)

print(matrix)
