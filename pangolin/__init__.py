#!/usr/bin env python 
# -*- coding: UTF-8 -*-

"""
@version: python2.7
@author: jicius
@software: PyCharm Community Edition
@file: __init__.py.py
@time: 2017-03-07 
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from pangolin.config import config


app = Flask(__name__)
# both the name and template_mode arguments as optionl
# ModelView all you to add a dedicated set of admin pages for managing any model in your database
admin = Admin(app, name=config.project_name, template_mode='bootstrap3')

# email are managed through a Mail instance
app.config.update(
    MAIL_SERVER='smtp.qq.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=config.qq_mail_username,
    MAIL_PASSWORD=config.qq_mail_password
)
mail = Mail(app)

secret_key = '3141592653589'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = config.mysql_account
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

"""
Straight out of the box, this gives you a set of fully featured CRUD views for your model:

    - A list view, with support for searching, sorting, filtering, and deleting records.
    - A create view for adding new records.
    - An edit view for updating existing records.
    - An optional, read-only details view.
"""
from pangolin.models import Users
# avoid loop revoking
# 初始化后台管理数据库中的表,
# 默认表中列全部显示
admin.add_view(ModelView(Users, db.session))
# 部分列显示, 自定义类, 并继承ModelView, 将需要使用的列写在column_list中
# class MyUsers(ModelView):
#     can_create = False
#     column_albels ={
#         'username': u'用户名',
#         'email': u'邮箱地址'
#     }
#     column_list = [
#         'username',
#         'email',
#     ]
#     def __init__(self, session, **kwargs):
#         super(MyUsers, self).__init__(Users, session, **kwargs)
# admin.add_view(MyUsers(db.session, nane=u'用户中心'))


from main import views