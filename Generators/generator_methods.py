def echo(maximum=10):
    print('Execution start with first next() call.')
    i = 0

    while i < maximum:
        val = (yield i)  # Save return value
        print('val is:', val)

        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1


generator = echo()

print('Calling next() - 1st time')
print(next(generator))

print('Calling next() - 2nd time')
print(next(generator))

# send(@arg) - resumes the execution and “sends” a value into the generator function.
# The value argument becomes the result of the current yield expression.
print('Calling send(@arg)')
print(generator.send(7))

print('Calling next() - 3rd time')
print(next(generator))

# throw(@type) - raises an exception of type @type at the point where the generator was paused
# and returns the next value yielded by the generator function.
print('Calling throw()')
print(generator.throw(ZeroDivisionError))

# close() - raises a GeneratorExit at the point where the generator function was paused.
generator.close()
