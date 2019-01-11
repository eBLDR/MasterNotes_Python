"""
CSV - Comma-Separated Values
.csv files are plain text files, used to store a large number of variables - or data.
They are arranged in lines, each line is called a 'record' and contain
multiple 'fields' separated by a comma ','.
We can think of it as an spreadsheet.
"""

import csv

# Reading csv files
with open('example.csv', 'r') as csv_file:
    # reader() method for reading file
    # @delimiter allows us to set any specific field delimiter - character between cells - default is ','
    read_csv = csv.reader(csv_file, delimiter=',')
    data = []
    for row in read_csv:  # Each row is delimited by newline character '\n'
        # Attribute line_num - tracks current reading line
        print('Line #: {}'.format(read_csv.line_num))
        print(row)
        data.append(row)

print('=' * 20)
print(data)
print('=' * 20)

# Writing csv files - newline='' is to avoid double spacing between rows, in some OS default newline is '\n'
with open('example2.csv', 'w', newline='') as csv_file:
    # writer() method for writing file
    # @lineterminator is the character between rows - default is '\n'
    write_csv = csv.writer(csv_file, delimiter=';', lineterminator='\n\n')  # A different delimiter
    for row in data:
        write_csv.writerow(row)

# Dictionary to csv
my_dict = {'alfa': 1, 'beta': 2}
with open('example2.csv', 'a', newline='') as csv_file:
    # DictWriter makes the conversion from dict to csv easy
    w = csv.DictWriter(csv_file, my_dict.keys())
    w.writeheader()
    w.writerow(my_dict)

# Use DictReader for reading csv to dict-like
