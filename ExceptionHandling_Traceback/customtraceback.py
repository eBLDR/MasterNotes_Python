import sys

try:
    b = 'one' + 2

except TypeError:
    error_type, error_value, traceback_object = sys.exc_info()
    print(error_type)
    print(error_value)
    print(traceback_object)

    input('Raise me! <enter>')

    # with_traceback(@tb) is optional - it will add to the exception being
    # raised the traceback object
    raise TypeError('Custom msg').with_traceback(traceback_object)
