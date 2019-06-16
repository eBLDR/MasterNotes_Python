"""
JSON format is plain text, it was developed as a standard for web servers data - commonly used
when providing web Application Programming Interface (API).
It stores data in a dictionary-like file. It specifies a way to serialize
(turn into a string) a dictionary or list, which then can be written to disk.
A JSON file is both compact and human readable.
JSON files are interchangeable between different languages.
JSON can’t store every kind of Python value. It can contain values of only the following data types:
strings, integers, floats, Booleans, lists, dictionaries, and NoneType.
JSON strings MUST use ""

JSON Data Types

Number - double precision floating-point format in JavaScript
String - double-quoted Unicode with backslash escaping
Boolean - true or false
Array - an ordered sequence of values
Value - it can be a string, a number, true or false, null etc
Object - an unordered collection of key:value pairs
Whitespace - can be used between any pair of tokens
null - empty
"""

import json

# load string method - translates json string to a python value
string_of_json_data = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
json_data_as_python_value = json.loads(string_of_json_data)

print(json_data_as_python_value)
print(type(json_data_as_python_value))

print('=' * 20)

# dump string method - translates a python value into a string of json-formatted data
python_value = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
                'felineIQ': None}
string_of_json_data2 = json.dumps(python_value)

print(string_of_json_data2)
print(type(string_of_json_data2))
