# Create customized exceptions
# Inherit from basic built-in Exception


class MyException(Exception):

    # Setting the custom message
    def __init__(self, msg, error_code=None):
        self.msg = msg
        self.code = error_code


try:
    raise MyException('Calling custom exception', error_code=112)
except Exception as e:
    print(e.args)  # Attribute containing the message (tuple)
    # Named arguments will NOT appear in e.args
    raise
