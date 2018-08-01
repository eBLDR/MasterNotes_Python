# an assertion is a sanity check, assert is used to detect programmers
# errors, while exceptions are for user errors (such as non existing files, etc.)
# assertions can be disable by passing the -O (upper 'o') option when running Python

doorStatus = 'open'

# assert verifies that the variable has the expected value
# assert VARIABLE == expected_value, error_msg if condition is False
assert doorStatus == 'open', 'The door must be open'

doorStatus = 'close'

# assert should never be in a try/except block, assert is intended to crash the program
# if condition fails - it raises an AssertionError
# assert doorStatus == 'open', 'The door must be open'

traffic_lights = {'ns': 'green', 'sw': 'red', 'nwse': 'orange'}
assert 'red' in traffic_lights.values(), 'No light is red!'
