# -*- coding: utf-8 -*-
__author__ = 'jinming'

from flask import Flask, request, g, render_template
from config import Default
from extensions import db
from sns.views import api

__all__ = ["setup_app"]
DEFAULT_NAME = "sns"
DEFAULT_MODULES = [
    (api, '/api')
]


def setup_app(config=None, app_name=None, modules=None):
    if app_name is None:
        app_name = DEFAULT_NAME
    if modules is None:
        modules = DEFAULT_MODULES
    app = Flask(app_name)
    init_configure_app(app, config)
    init_extensions(app)
    init_register_views(app, modules)

    return app


def init_configure_app(app, config):
    if config is not None:
        app.config.from_object(config)
    else:
        app.config.from_object(Default())

    # app.config.from_envvar('IZPPY_SET', silent=True)


def init_extensions(app):
    db.init_app(app)


def init_register_views(app, modules):
    for module, prefix in modules:
        app.register_module(module, url_prefix=prefix)

