#!/usr/bin/env python
#   -*- coding: utf-8 -*-
#
#   Copyright (C) 2017 Jicius
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time
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
        subject=u"Data Statistics",
        sender=(u"jicius", "2644148694@qq.com"),                  # sender是一个二元组, 分别为姓名和邮件地址
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
