# -*- coding: utf-8 -*-

from celeryapp import celery


@celery.task()
def add_together(a, b):
    return a + b

