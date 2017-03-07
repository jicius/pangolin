#!/usr/bin env python 
# -*- coding: UTF-8 -*-

"""
@version: python2.7
@author: jicius
@software: PyCharm Community Edition
@file: models.py
@time: 2017-03-07 
"""

import uuid
import datetime

from pangolin import db


class Hosts(db.Model):
    # Records query
    __tablename__ = 'hosts'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(64), unique=True, default=str(uuid.uuid4()).replace('-', ''))
    query = db.Column(db.String(64))
    host = db.Column(db.String(64))
    datetime = db.Column(db.DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return '<Uid> %s' % self.uid
