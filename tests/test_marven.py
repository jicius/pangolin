#!/usr/bin env python 
# -*- coding: UTF-8 -*-

"""
@version: python2.7
@author: jicius
@software: PyCharm Community Edition
@file: test_marven.py
@time: 2017-03-08 
"""

from raven import Client


client = Client('http://83a85dae93814c55b3f4421cdf543442:42d0dce506d145b39a06290b53e850c9@127.0.0.1:9000/1')

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()


