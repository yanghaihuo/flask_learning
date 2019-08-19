#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/7/23 14:57
# @author: Paulson●Wier
# @file: config.py
# @desc:

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False   # 设置数据发生变更之后是否发送信号给应用
    POSTS_PER_PAGE = 25

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['ybsdeyx@foxmail.com']
    LANGUAGES = ['en', 'es']
