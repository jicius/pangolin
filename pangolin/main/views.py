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
import datetime
from functools import wraps

from flask import (request, jsonify, render_template)
from flask_mail import Message

from pangolin import (app, mail)
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


@app.route('/email', methods=['GET'])
def email():
    """ Send email

    Sending email.
    """
    msg = Message(
        subject=u"数据统计",
        body="text body",
        html=render_template("email.html", datetime=time.ctime()),
        sender=(u"征信运维", "2644148694@qq.com"),                  # sender是一个二元组, 分别为姓名和邮件地址
        recipients=["bq_ji@yahoo.com"]
    )
    msg.html = render_template('email.html', title=123456)
    try:
        mail.send(msg)
    except Exception as e:
        return jsonify(dict(Code=-1, State=e))
    return jsonify(dict(Code=0, State="Ok"))


@app.route('/proxy_message')
def proxy():
    """ Proxy check

    Check proxy type.
    """
    return jsonify(dict(
        remote_addr=request.remote_addr,
        user_agent=str(request.user_agent),
        scheme=request.scheme
    ))


# @app.route('/email', methods=['GET'])
# def email():
#     return render_template("email.html", title=u"数据统计")

