#!/usr/bin env python 
# -*- coding: UTF-8 -*-

"""
@version: python2.7
@author: jicius
@software: PyCharm Community Edition
@file: run.py.py
@time: 2017-03-07 
"""

from pangolin import app

from raven import Client
from raven.middleware import Sentry

app = Sentry(
    app,
    Client('http://6a50e29553ba4890adbb68ba386a3ab2:85ff4c4ba8b04350b45f8d5b6c4192bb@127.0.0.1:9000/4')
)


if __name__ == '__main__':
    app.run()