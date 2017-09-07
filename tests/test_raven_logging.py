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

import logging
import time
import random


from raven.handlers.logging import SentryHandler
from raven.conf import setup_logging

# Configure the default client
handler = SentryHandler('http://ed7a4cdc507f47968ebd88072e3dae44:f62964da28c34a7d9906111f490a9d6f@192.168.1.211:9000/10')
setup_logging(handler)


logger = logging.getLogger(__name__)


if __name__ == '__main__':
    while True:
        logger.critical('There was an error, with a stacktrace!', extra={
            'stack': True,
        })
        time.sleep(random.randrange(1,3))
