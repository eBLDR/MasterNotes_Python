"""
logging module, for controlled print() and more
5 levels, from lowest to highest:
    - logging.debug() - small debugging details
    - logging.info() - to record information or confirming
    - logging.warning() - potential problem that doesn't prevent the program from working
    - logging.error() - causes the program to fail
    - logging.critical() - fatal error that causes the program to stop entirely
"""
import logging

# Setting configuration, @filename is usually by convention filename.log
# @level can set the levels we want to enable (itself and above)
# i.e.: level=logging.ERROR will only show error and critical
# @format can be anything we wish, using existing attributes
logging.basicConfig(filename='my_log.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s - %(process)d - %(processName)s - ' \
                           '%(threadName)s - %(levelname)s - %(message)s')

# logging can also be print onto the screen instead of writing to file,
# just don't pass any argument for @filename

# debug(msg) will print the msg
logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial({})'.format(n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is {}, total is {}'.format(i, total))
    logging.debug('End of factorial({})'.format(n))
    return total


print(factorial(5))
logging.debug('End of program')

print('=' * 40)

# to disable the logging, will disable from level to below
# i.e.: the next example wil disable info and debug
logging.disable(logging.INFO)

logging.debug('Debugging details')
logging.info('Module is working')
logging.warning('An error msg is about to be logged')
logging.error('An error has occurred')
logging.critical('Program unable to recover')
