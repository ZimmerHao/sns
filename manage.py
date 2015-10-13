# -*- coding: utf-8 -*-
__author__ = 'jinming'

from flask.ext.script import Server, Manager, prompt_bool
from application import setup_app

"""
usage: provide a command for izppy.
python manage.py runserver: use to run a flask development server.
"""

app = setup_app()
manager = Manager(app)
manager.add_command("runserver", Server('0.0.0.0', port=5000))


if __name__ == "__main__":
    manager.run()