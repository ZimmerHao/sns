#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'jinming'


class Config(object):
    @staticmethod
    def get_database_uri(**database):
        return 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(
            user=database['USER'],
            password=database['PASSWORD'],
            host=database['HOST'],
            port=database['PORT'],
            name=database['NAME'],
        )


class Default(object):
    # debug mole
    DEBUG = True

    # postgresql configuration
    DATABASE = {
        'NAME': 'testsns',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }

    SQLALCHEMY_DATABASE_URI = Config.get_database_uri(**DATABASE)
    SQLALCHEMY_BINDS = {

    }
    # the secret key
    SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    # SECRET_KEY = "secret"


    # celery configuration
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_IMPORTS = ['tasks']


