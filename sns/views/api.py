# -*- coding: utf-8 -*-
__author__ = 'jinming'

from flask import Module, request, g, jsonify

api = Module(__name__)


@api.route('/')
def index():
    return "ok"