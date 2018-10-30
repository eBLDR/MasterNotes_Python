#! /usr/bin/python3
"""
Reading a file and, if file is CSV, importing the data in
a relational database using SQLite3, in which the column's names
correspond to the first record (header) found in the CSV file.

Run from terminal - command line:

csv_to_db.py <absolute_path> - reads the file at <absolute_path> and extracts data if the file is CSV.
"""
import sys
import os
import csv
import sqlite3


def script_usage():
    """
    Displays program's usage from command line.
    
    """
    print('Usage:\n\tcsv_to_db.py <absolute_path> - reads the file and extracts data if the file is CSV')


def read_file(path):
    """
    Opens and reads a file, if the file has '.csv' format extension,
    data will be extracted.

    @path: absolute path of file.

    return: data -- a list type object containing the records extracted from the file,
    only if file is CSV format.
    """
    try:
        with open(path) as file:

            # Extracting the file name from the path
            file_name = os.path.split(file_path)[1]

            # If the file is CSV - extract and create database
            if file_name.endswith(".csv"):

            # Equivalent expression using indexes:
            # if path[-3:] == 'csv':
                
                readCSV = csv.reader(file, delimiter=',')

                print('Extracting records from {}...'.format(file_name))  # Control print
                
                # Extracting and storing the data from the file on a list
                data = [record for record in readCSV]

                # Control print
                print('Extraction completed.\n\t- Records extracted: {}'.format(readCSV.line_num - 1))

                return file_name, data

            # If the file is not CSV - read normally
            else:
                for line in file:
                    print(line.rstrip())  # Stripping newline at the end of line, just for aesthetics

    except FileNotFoundError:
        # In case the file doesn't exist
        print("File Not Found.")
        sys.exit(1)


def create_db(file_name, data):
    """
    Creates the database and fills it with the records from the data.

    @file_name: name of the database file.
    @data: list type storing the records.
    """
    # Stripping the extension to get the name only,
    # stripping of the '.' on its own to avoid accidentally stripping
    # possible matching characters with the sequence '.csv'
    db_name = file_name.rstrip('csv').rstrip('.')
    
    # Opening/creating database file object
    db = sqlite3.connect('{}.sqlite'.format(db_name))

    print('\nInserting records to {}.sqlite...'.format(db_name))

    # Counter of added records, control only
    r = 0

    header = True
    for record in data:

        # Creating table and columns - special treat to first record (header)
        if header:
            header = False
            
            # To clear the table every time, otherwise the INSERT will duplicate records
            # in case we run the script more than once
            db.execute("DROP TABLE IF EXISTS {}".format(db_name))
            
            # Creating table
            db.execute("CREATE TABLE {} (id INTEGER PRIMARY KEY, {})"
                       .format(db_name, ", ".join(["%s TEXT" % column for column in record])))

            # Storing the names of the fields for future insertions
            fields = ", ".join([field for field in record])

        # Inserting records into the database
        else:
            db.execute("INSERT INTO {} ({}) VALUES ({})"
                       .format(db_name, fields, ", ".join([repr(column) for column in record])))

            r += 1  # Updating the counter
            
    print('Insertion completed.\n\t- Records added: {}'.format(r))  # Control print

    # Committing changes and closing database file
    db.commit()
    db.close()


def main(path):
    # Read the file and extract data
    file_name, data = read_file(path)

    if data:
        # Creating a database using the records previously extracted
        create_db(file_name, data)

    
if __name__ == '__main__':
    # Type the path of the file here -- TESTING/DEBUGGING ONLY, leave blank otherwise
    PATH = ''

    # -- GETTING THE PATH --
    file_path = file_path = sys.argv[1] if len(sys.argv) == 2 else PATH if PATH else ''

    # -- RUNNING --
    if file_path:
        main(file_path)

    else:
        script_usage()
        print('No path provided.')
