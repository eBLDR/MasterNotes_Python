"""
Adding customized attributes to the formatter msg.
"""
import logging

extra = {'my_attr': __name__}

# Instantiating a new logger object, name can be any
my_logger = logging.getLogger(__name__)

# Customizing the new format
formatter = logging.Formatter('%(asctime)s - %(my_attr)s: %(message)s')

# Format handler
syslog = logging.StreamHandler()
syslog.setFormatter(formatter)

# Adding the handler to our custom logger
my_logger.addHandler(syslog)

path = 'custom_log.log'  # In current working directory

# Adding file path where to log
file_handler = logging.FileHandler(path)
# If format is not set, it will just log the message
file_handler.setFormatter(formatter)

# Adding the handler
my_logger.addHandler(file_handler)

# logger.LoggerAdapter(@logger, @extra) updates the @logger with the new @extra parameters
my_logger = logging.LoggerAdapter(my_logger, extra=extra)

# It will ignore the ones which have less severity that the specified level
my_logger.setLevel(logging.INFO)

my_logger.info('Hello there')
