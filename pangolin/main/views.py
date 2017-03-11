#!/usr/bin env python 
# -*- coding: UTF-8 -*-

"""
@version: python2.7
@author: jicius
@software: PyCharm Community Edition
@file: views.py
@time: 2017-03-07 
"""

from flask import (request, jsonify)

from pangolin import app
from pangolin.models import (Hosts, db)


@app.route('/', methods=['GET'])
def index():
    """ 入口地址
    """
    hs_obj = Hosts(
        query=request.url,
        host=request.host
    )
    db.session.add(hs_obj)
    db.session.commit()
    return jsonify(dict(datetime=hs_obj.datetime))


@app.route('/news', methods=['GET'])
def news():
    """ 新闻
    """
    return jsonify(dict(news="???"))