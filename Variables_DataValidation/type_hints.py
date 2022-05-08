# From Python 3.6+ variable annotations can be typed, this will show warnings
# on some IDE and provide autocompletion
# var_name: type = value
user: str = 'BLDR'

print(user, type(user))

# Multiple types can be specified
age: (int, None) = None

# Variable declaration without initial value
# The variable is still undefined
empty: str

print('=' * 20)

# Type list of int
# numbers: list[int] = []

print('=' * 20)

# Declaring sequences and their internal types
# Import of typing only necessary for python <3.9
from typing import Dict, List

numbers = List[int]

# Python 3.9+
# numbers = list[int]

# [@key type, @value type]
items = Dict[str, float]

print(items)

print('=' * 20)


# Function annotations (type hints) can also be used on function's parameters
def get_name(first_name: str, second_name: str) -> str:  # -> hint about the type returned
    return f'{first_name.title()} {second_name.title()}'


print(get_name('simon', 'will'))
print(f"__annotations__: {get_name.__annotations__}")


# Function annotations can also be placed in named arguments
def some_calculation(init: float, step: int = 1) -> float:
    return init + step


print(some_calculation(5, 7))

print('=' * 20)

# Multiple types
from typing import Optional, Union


# Optional defines the type as declared or None
def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f'Hey {name}!')
    else:
        print('Hello World')


say_hi()


# Union makes a list of possible types
# Only for python <3.10 (3.10 adds operator |)
def add_one(number: Union[int, float]):
    print(number + 1)


add_one(3)

print('=' * 20)


# Type hints can also be a customized class (besides generic types)
class Mock:
    def work(self):
        return


def work_mock(mock: Mock):
    mock.work()


print('=' * 20)


# Type aliases
Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


# A list of floats qualifies as a Vector
new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector)

# Simplifying complex type signatures
VectorSet = List[Vector]
print(VectorSet)

# Equivalent to
VectorSet = List[List[float]]
