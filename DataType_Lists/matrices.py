# Lists can be nested, that is called matrix
nested_list = [[0, 1], [10, 11], [100, 111]]
print(nested_list)
print(nested_list[0], nested_list[1][1])  # Use multiple index to refer a specific item

# Create matrix
l = []
n = 3

# Method 1
for i in range(n):
    l += [[0] * n]

print(l)

# Method 2
l = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    l.append(row)

print(l)

# Method 3
l = []
for i in range(n):
    l.append([])
    for j in range(n):
        l[i].append(0)

print(l)
