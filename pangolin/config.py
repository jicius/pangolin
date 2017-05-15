#!/usr/bin env python 
# -*- coding: UTF-8 -*-

"""
@version: python2.7
@author: jicius
@software: PyCharm Community Edition
@file: config.py
@time: 2017-03-07 
"""

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
