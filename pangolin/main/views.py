#!/usr/bin env python 
# -*- coding: UTF-8 -*-

"""
@version: python2.7
@author: jicius
@software: PyCharm Community Edition
@file: views.py
@time: 2017-03-07 
"""
import time
from functools import wraps

from flask import (request, jsonify)
from flask_mail import Message

from pangolin import (app, mail)
# from pangolin import sentry
from pangolin.models import (Hosts, db)


def timer_handle(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        global c
        c = time.time()
        return f(*args, **kwargs)
    return wrapper


@app.route('/', methods=['GET'])
@timer_handle
def index():
    """ App index

    Index of the program.
    """
    hs_obj = Hosts(
        query=request.url,
        host=request.host
    )
    print c
    db.session.add(hs_obj)
    db.session.commit()
    return jsonify(dict(datetime=hs_obj.datetime))


@app.route('/emails', methods=['GET'])
def emails():
    """ Send email

    Sending email.
    """
    msg = Message(
        subject="Hello, world!",
        body="This is my first email sent by Flask Mail.",
        sender="bq_ji@yahoo.com",
        recipients=["487834315@qq.com"]
    )
    if mail.send(msg):
        return jsonify(dict(status="Success"))
    else:
        return jsonify(dict(status="Failed"))

