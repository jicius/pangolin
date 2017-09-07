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

