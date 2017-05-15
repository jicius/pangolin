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




