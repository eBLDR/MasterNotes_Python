# Create customized exceptions
# Inherit from basic built-in Exception
class MyException(Exception):

    # Setting the custom message
    def __init__(self, msg):
        self.msg = msg


try:
    raise MyException('Calling custom exception')
except Exception as e:
    print(e.args)  # Attribute containing the message (tuple)
    raise

