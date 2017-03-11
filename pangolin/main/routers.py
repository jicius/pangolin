#!/usr/bin env python 
# -*- coding: UTF-8 -*-

"""
@version: python2.7
@author: jicius
@software: PyCharm Community Edition
@file: routers.py
@time: 2017-03-11 
"""

from pangolin import app


if __name__ == '__main__':
    its = app.view_functions.viewitems()
    for it in its:
        print it[1].__name__, it[1].func_name, it[1].func_doc