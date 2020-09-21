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

# Reading csv to dictionary-like
with open('example.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = []

    for row in csv_reader:
        # First iteration will directly take the values of the second row
        data.append(row)

    # If a value is missing for one row, the corresponding value will be `None`
    print(data)

# Writing csv files - newline='' is to avoid double spacing between rows, in some OS default newline is '\n'
with open('example2.csv', 'w', newline='') as csv_file:
    # writer() method for writing file
    # @lineterminator is the character between rows - default is '\n'
    write_csv = csv.writer(csv_file, delimiter=';', lineterminator='\n\n')  # A different delimiter
    for row in data:
        write_csv.writerow(row)

# Dictionary to csv
my_objects = [
    {'label': 'alpha', 'value': 1},
    {'label': 'beta', 'value': 2},
]
with open('example2.csv', 'a', newline='') as csv_file:
    # DictWriter makes the conversion from dict to csv easy
    w = csv.DictWriter(csv_file, fieldnames=list(my_objects[0].keys()))
    w.writeheader()

    for object_ in my_objects:
        w.writerow(object_)
