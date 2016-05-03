import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from todoapp.apps import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
