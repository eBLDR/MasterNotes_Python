# mode 'a' is going to create the file if it doesn't exists
# is going to append more text every time we run the program
with open('tables.txt', 'a') as tablesFile:
    for i in range(2, 5):
        for j in range(1, 11):
            print('{1:>2} times {0} is {2}'.format(i, j, i * j), file=tablesFile)
        print("-" * 20, file=tablesFile)
