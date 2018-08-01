"""
CSV - Comma-Separated Values
.csv files are plain text files, used to store a large number of variables - or data.
They are arranged in lines, each line is called a 'record' and contain
multiple 'fields' separated by a comma ','.
We can think of it as an spreadsheet.
"""

import csv

# reading csv files
with open('example.csv', 'r') as csvfile:
    # reader() method for reading file
    # delimiter allows us to set any specific field delimiter - character between cells - default is ','
    readCSV = csv.reader(csvfile, delimiter=',')
    data = []
    for row in readCSV:  # each row is delimited by newline character '\n'
        # attribute line_num - tracks current reading line
        print("Line #: {}".format(readCSV.line_num))
        print(row)
        data.append(row)

print("=" * 20)
print(data)
print("=" * 20)

# writing csv files - newline='' is to avoid double spacing between rows, in some OS default newline is '\n'
with open('example2.csv', 'w', newline='') as csvfile:
    # writer() method for writing file
    # lineterminator is the character between rows - default is '\n'
    writeCSV = csv.writer(csvfile, delimiter=';', lineterminator='\n\n')  # a different delimiter
    for row in data:
        writeCSV.writerow(row)
