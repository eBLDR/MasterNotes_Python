# assigning multiple variables
a2 = b2 = c2 = d2 = 12  # number type
print(a2, b2, c2, d2)

a2, b2 = 13, 14
print("a2 is {}".format(a2))
print("b2 is {}".format(b2))

w1, w2 = 'OK'  # str type, the number of variables must match the number of characters
print("w1 is {}".format(w1))
print("w2 is {}".format(w2))

l1, l2 = [0, 'L']  # list type, the number of variables must match the number of items
print("l1 is {}".format(l1))
print("l2 is {}".format(l2))

# swapping variables - notice that Python evaluates first the right side of the equal
a2, b2 = b2, a2
print("a2 is {}".format(a2))
print("b2 is {}".format(b2))
