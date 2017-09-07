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
import random

from raven import Client


client = Client('http://ed7a4cdc507f47968ebd88072e3dae44:f62964da28c34a7d9906111f490a9d6f@127.0.0.1:9000/10')


if __name__ == '__main__':
    while True:
        try:
            1 / 0
        except ZeroDivisionError:
            client.captureException()
        time.sleep(random.randrange(1,3))