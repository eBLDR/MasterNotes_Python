"""
An assertion is a sanity check, assert is used to detect programmers errors,
while exceptions are for user errors (such as non existing files, etc.)
Assertions can be disable by passing the -O (upper 'o') option when running
the Python script
"""
# assert verifies that the expression is satisfied
# assert <expression>, error_msg to be printed if expression is False
# if condition fails - it raises an AssertionError
assert isinstance('a', int), 'Not cool!'

door_status = 'open'

assert door_status == 'open', 'The door must be open'

door_status = 'close'

# assert should never be in a try/except block, assert is intended to crash
# the program
# assert door_status == 'open', 'The door must be open'

traffic_lights = {'ns': 'green', 'sw': 'red', 'nwse': 'orange'}
assert 'red' in traffic_lights.values(), 'No light is red!'
