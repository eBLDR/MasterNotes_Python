class Numbers(list):
    def add(self, number):
        if not isinstance(number, (int, float)):
            raise TypeError('Only <int> or <float> please!')

        self.append(number)


# Exceptions can be raised anytime
# Objects raised must be <BaseException> type (or subclass)
# raise EOFError
# raise EOFError()  # Equivalent

# Personalized error message can be passed
# raise EOFError('Trolling you!')

my_numbers = Numbers()

data = [9, 8, 'A', 7]

try:
    # Testing the error handling by forcefully raising an exception
    # raise Exception('Testing exception handler!')

    for value in data:
        my_numbers.add(value)

except TypeError as error:
    # Calling `raise` here will re-raise the same exception that was just caught
    raise
