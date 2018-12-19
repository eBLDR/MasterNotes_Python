"""
Context managers are used when working with external resources like
files, databases, sockets...
Removes the need of closing the resource each time and also handles errors.
It's a good alternative to try/except/finally
"""

# WITH keyword
# 'with' can call anything that returns a context manager (like the built-in open() function)
with open('example.txt', 'a') as myResource:
    # myResource variable can only be used in this context, outside this
    # indentation it will be closed
    print(type(myResource))
    
    myResource.write('one more line\n')
    # No need to close the resource, it's done automatically
    # If we force an error during the execution, the resource will be closed before calling raise


# Multiple resource usage
# with A() as a, B() as b, ...:


# Customized managers
class File:
    # Redundant class, does exactly the same as the example above, but we can
    # add here extra functionality
    
    def __init__(self, filename, mode):
        
        print('I am __init__')
        
        self.filename = filename
        self.mode = mode
        
        self.success = False  # Extra functionality
    
    def __enter__(self):
        # Special method name
        
        print('I am __enter__')
        
        # Method called when resource is opened
        self.connection = open(self.filename, self.mode)
        
        print('File opened')
        
        # The value returned from this method will be assigned to the 'as' variable
        return self
    
    def __exit__(self, *args):
        # Special method name
        
        print('I am __exit__')
        
        # Extra functionality
        if self.success:
            print('Do A, I succeeded.')
        else:
            print('Do B, I failed.')
        
        # Method called when the 'with' block is finished or when an exception is raised
        self.connection.close()
        
        print('File closed')


with File('example2.txt', 'a') as file:
    # file is now whatever is returned from the __enter__() method
    file.connection.write('more and more and more\n')
    
    # Forcing error
    # raise NameError  # Comment/Uncomment this line to see different behaviour
    
    # Extra functionality - if no errors were raised
    file.success = True  # Last line
