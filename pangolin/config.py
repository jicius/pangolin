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

import os


class Config(object):
    """ Basic Config

    """
    project_name = 'Pangolin'

    qq_mail_username = '2644148694'
    qq_mail_password = 'rrkwvmhjukahdjai'


class DevelopmentConfig(Config):
    mysql_account = 'mysql://root:123456@192.168.1.214/test'


class TestingConfig(Config):
    mysql_account = 'mysql://root:123456@192.168.1.214/test'


class ProductionConfig(Config):
    mysql_account = ''


config_setting = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

config = config_setting.get(os.getenv('ENVIRONMENT'), DevelopmentConfig)
