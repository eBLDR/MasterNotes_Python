# mode 'a' - appending - is going to create the file if it doesn't exists
# is going to append more text every time we run the program
with open('appending_tables.txt', 'a') as tables_file:
    for i in range(2, 5):
        for j in range(1, 11):
            # Redirecting the output of print() to a file, write() is also possible
            print('{1:>2} times {0} is {2}'.format(i, j, i * j), file=tables_file)
        print('-' * 20, file=tables_file)

    more_text = input('What else would you life to append to file?\n>')
    tables_file.write(more_text)

print('Done.')
