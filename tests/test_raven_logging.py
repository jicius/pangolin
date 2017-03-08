#!/usr/bin env python 
# -*- coding: UTF-8 -*-

"""
@version: python2.7
@author: jicius
@software: PyCharm Community Edition
@file: test_raven_logging.py
@time: 2017-03-08 
"""
import logging
import time
import random


from raven.handlers.logging import SentryHandler
from raven.conf import setup_logging

# Configure the default client
handler = SentryHandler('http://83a85dae93814c55b3f4421cdf543442:42d0dce506d145b39a06290b53e850c9@192.168.101.105:9000/1')
setup_logging(handler)


logger = logging.getLogger(__name__)


if __name__ == '__main__':
    while True:
        logger.error('There was an error, with a stacktrace!', extra={
            'stack': True,
        })
        time.sleep(random.randrange(1,3))