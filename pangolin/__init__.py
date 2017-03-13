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
from flask_mail import Mail
# from raven.contrib.flask import Sentry


app = Flask(__name__)
# sentry = Sentry(dsn='http://6a50e29553ba4890adbb68ba386a3ab2:85ff4c4ba8b04350b45f8d5b6c4192bb@127.0.0.1:9000/4')


# def create_app():
#     sentry.init_app(app, logging=True, level=logging.INFO)
#     return app

# app = create_app()


"""
In this case all emails are sent using the configuration values of the application that was passed to
the Mail class constructor.
    * MAIL_SERVER: default 'localhost'
    * MAIL PORT: default 25
    * MAL_USE_TLS: default False
    * MAIL_USE_SSL: default False
    * MAIL_DEBUG: default app.default
    * MAIL_USERNAME: default None
    * MAIL_PASSWORD: default None
    * MAIL_DEFAULT_SENDER: default None
    * MAIL_MAX_EMAILS: default None
    * MAIL_SUPPRESS_SEND: default app.testing
    * MAIL_ASCII_ATTACHMENTS: default False
"""
# email are managed through a Mail instance
mail = Mail(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@192.168.1.214/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


from main import views