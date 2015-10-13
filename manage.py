__author__ = 'jinming'

from flask.ext.script import Server, Manager, prompt_bool
from application import setup_app

"""
usage: provide a command for izppy.
python manager.py runserver: use to run a flask development server.
python manager.py createall: use to create all database tables. But MUST create databese first.
python manager.py dropall: use to drop all database tables.
python manager.py createuse: use to create a user.(use uuid module)
"""

app = setup_app()
manager = Manager(app)
manager.add_command("runserver", Server('0.0.0.0', port=5000))


if __name__ == "__main__":
    manager.run()