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

from flask import (request, jsonify, render_template)
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
    db.session.add(hs_obj)
    db.session.commit()
    return jsonify(dict(datetime=hs_obj.datetime))


@app.route('/emails', methods=['GET'])
def emails():
    """ Send email

    Sending email.
    """
    msg = Message(
        subject=u"数据统计",
        body=render_template('email.html'),
        sender=(u"征信运维", "2644148694@qq.com"),            # sender是一个二元组, 将会被分分为姓名和邮件地址
        recipients=["bq_ji@yahoo.com"]
    )
    try:
        mail.send(msg)
    except Exception as e:
        return jsonify(dict(Code=-1, state=e))
    return jsonify(dict(Code=0, state="Ok"))

