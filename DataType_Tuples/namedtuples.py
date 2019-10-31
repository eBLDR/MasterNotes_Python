import json

# From collections module
from collections import namedtuple

# Generate the tuple structure - (@type, @[name1, name2, ..., nameN])
plant = namedtuple(
    'Plant',
    ['name', 'scientific_name', 'lifecycle', 'plant_type']
)

# Identifiers can also be specified as a comma-separated
# i.e.: namedtuple('Plant', 'name, scientific_name, lifecycle, plant_type')

# Create the named tuple by specifying the arguments to be put in the
# corresponding names, by order
my_plant = plant('Andro', 'OndraScience', 'Green', 'Fire')
print(my_plant)

# Access using indexes
print(my_plant[1])

# Or access members using dot notation
print(my_plant.scientific_name)

print('#' * 30)

plants_list = [
    plant('Andre', 'EndraScience', 'Green', 'Water'),
    plant('Andra', 'AndraScience', 'NotGreen', 'Fire'),
    plant('Andri', 'IndraScience', 'Green', 'Air'),
    plant('Andrw', 'WndraScience', 'Unknown', 'Earth'),
    plant('Andrs', 'RsndraScience', 'Green', 'Air')
]

print(plants_list[0].lifecycle)
# Using _replace to replace the value of a specific identifier
plants_list[0] = plants_list[0]._replace(lifecycle='Yellow')
print(plants_list[0].lifecycle)

for p in plants_list:
    if p.lifecycle == 'Green':
        print(p.name, p.scientific_name)

print('#' * 30)

# Dictionary to named tuple
data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

# Parse JSON into an object with attributes corresponding to dict keys.
data_object = json.loads(data, object_hook=lambda d: namedtuple('DataObject', d.keys())(*d.values()))
print(type(data_object))
print(data_object.name, data_object.hometown.name, data_object.hometown.id)

data_object_as_dict = data_object._asdict()

print(type(data_object_as_dict))
print(data_object_as_dict)
