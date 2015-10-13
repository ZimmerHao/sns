#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'jinming'


class Default(object):
    # debug mole
    DEBUG = True

    # configuration mysql--- for prodict
    SQLALCHEMY_DATABASE_URI = None

    # the secret key
    SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    # SECRET_KEY = "secret"


    # celery configuration
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_IMPORTS = ['tasks']