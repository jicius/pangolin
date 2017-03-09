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
handler = SentryHandler('http://ed7a4cdc507f47968ebd88072e3dae44:f62964da28c34a7d9906111f490a9d6f@192.168.1.211:9000/10')
setup_logging(handler)


logger = logging.getLogger(__name__)


if __name__ == '__main__':
    while True:
        logger.critical('There was an error, with a stacktrace!', extra={
            'stack': True,
        })
        time.sleep(random.randrange(1,3))
