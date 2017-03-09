#!/usr/bin env python 
# -*- coding: UTF-8 -*-

"""
@version: python2.7
@author: jicius
@software: PyCharm Community Edition
@file: test_jinja2_api.py
@time: 2017-03-08 
"""

"""
Jinja2使用一个名为Environment的中心对象。这个类的实例用于存储配置、全局对象, 并用于
从文件系统或者其他位置加载模板
"""
from jinja2 import Environment, PackageLoader, Template

# 创建默认设定下的模板环境和一个在yourapplication python包中的templates文件夹中寻找模板的加载器
# 使用一个加载器, 而不是向Template或Environment.from_string()传递字符串有很多好处
# evn = Environment(loader=PackageLoader('yourapplication', 'templates'))

tmp_template = "{% set a, b = 'foo', '123'%}"
m = Template(tmp_template).module
print m.a
print m.b

# compile_expression(source, undefined_to_none=True)
evn = Environment()
expr = evn.compile_expression('foo == 42')
print expr(foo=23)
print expr(foo=42)

