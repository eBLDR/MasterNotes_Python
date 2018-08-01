"""
JSON format is plain text, it was developed as a standard for web servers data - commonly used
when providing web Application Programming Interface (API).
It stores data in a dictionary-like file. It specifies a way to serialize
(turn into a string) a dictionary or list, which then can be written to disk.
A JSON file is both compact and human readable.
JSON files are interchangeable between different languages.
JSON can’t store every kind of Python value. It can contain values of only the following data types:
strings, integers, floats, Booleans, lists, dictionaries, and NoneType.
"""

import json

# load string method - translates json string to a python value
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)

print(jsonDataAsPythonValue)
print(type(jsonDataAsPythonValue))

print("=" * 20)

# dump string method - translates a python value into a string of json-formatted data
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
               'felineIQ': None}
stringOfJsonData2 = json.dumps(pythonValue)

print(stringOfJsonData2)
print(type(stringOfJsonData2))
