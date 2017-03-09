#!/usr/bin env python 
# -*- coding: UTF-8 -*-

"""
@version: python2.7
@author: jicius
@software: PyCharm Community Edition
@file: __init__.py.py
@time: 2017-03-07 
"""

import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from raven import Client
from raven.contrib.flask import Sentry


app = Flask(__name__)
sentry = Sentry(dsn='http://6a50e29553ba4890adbb68ba386a3ab2:85ff4c4ba8b04350b45f8d5b6c4192bb@127.0.0.1:9000/4')


def create_app():
    sentry.init_app(app, logging=True, level=logging.INFO)
    return app

app = create_app()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@192.168.1.214/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


from main import views