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
