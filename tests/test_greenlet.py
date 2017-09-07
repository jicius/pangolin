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

"""
generator & greenlet diff:
    generator: 将yield的value返回个调用者
    greenlet: 可以切换到指定的协程然后yield value
"""

from greenlet import greenlet


def test1():
    print 12
    gr2.switch()
    print 34


def test2():
    print 56
    gr1.switch()
    print 78


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()

