a_list = [6, -1, 12, 3]
b_list = [1, 6, 4]

# append(item) - appends item to end of list
a_list.append(0)
print(a_list)

# extend(seq) - appends a whole sequence at the end
a_list.extend(b_list)
print(a_list)

# insert(index, x) - insert an item x at a given index
a_list.insert(1, 31)
print(a_list)

# remove(x) - remove the first item whose value is x
a_list.remove(31)
print(a_list)

# pop(index) - remove and return the item at index, if index is not
# specified default value is the last item
give = a_list.pop(0)
print(give)
print(a_list)

# clear() - removes all items
b_list.clear()
print(b_list)

# reverse() - reverses the order of the items
a_list.reverse()
print(a_list)

# sort(key=function, reverse=False) - sorts alphanumerically, see sorted() in built-in
a_list.sort()
print(a_list)

# copy() - makes a shallow (independent) copy with different id
a_copy = a_list.copy()
