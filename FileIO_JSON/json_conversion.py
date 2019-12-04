"""
JSON files can’t store every kind of Python value. It can contain values of
only the following data types:
strings, integers, floats, Booleans, lists, dictionaries, and NoneType.
"""
import json

# load string method - translates json string to a python value
string_of_json_data = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
json_data_as_python_value = json.loads(string_of_json_data)

print(json_data_as_python_value)
print(type(json_data_as_python_value))

print('=' * 20)

# dump string method - translates a python value into a string of json-formatted data
python_value = {
    'isCat': True,
    'miceCaught': 0,
    'name': 'Zophie',
    'felineIQ': None,
}
string_of_json_data2 = json.dumps(python_value)

print(string_of_json_data2)
print(type(string_of_json_data2))
