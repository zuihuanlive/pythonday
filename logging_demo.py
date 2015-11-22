# coding:utf-8
import logging


# print(sys.path)
# logging.info('nihao')

# logging to a file
# logging.basicConfig(filename='log.log', level=logging.DEBUG)
# logging.basicConfig(filename='log.log', level=logging.INFO)
# logging.debug('This is debug log.')
# logging.warning('This is warning log.')
# logging.error('This is error log.')
# logging.info('This is info log.')

# logging variable data
# logging.warning('%s before you %s', 'look', 'leap!')

# change the format of displayed messages
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG, filename='log.log')
# logging.debug('This message should appear on the console')
# logging.info('So should this')
# logging.warning('And this,too')

# display date/time in the messages
logging.basicConfig(format='%(asctime)s:%(message)s')
logging.warning('is when this event was logged.')
