# mode 'a' - appending - is going to create the file if it doesn't exists
# is going to append more text every time we run the program
with open('appending_tables.txt', 'a') as tablesFile:
    for i in range(2, 5):
        for j in range(1, 11):
            # Redirecting the output of print() to the file
            print('{1:>2} times {0} is {2}'.format(i, j, i * j), file=tablesFile)
        print("-" * 20, file=tablesFile)

print('Done.')
