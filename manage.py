from flask_script import Manager
from sqlalchemy import Column, String, Integer, create_engine
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from models import db, Movies, Actors

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


# custom seed command
@manager.command
def seed():
    Movie(title='Bojack Horseman', release_date='2018-12-12').insert()
    Movie(title='Witcher', release_date='2009-12-12').insert()

    Actor(name='Jennifer Lawrence', age=32, gender='female').insert()
    Actor(name='Chris Pratt', age=50, gender='male').insert()


if __name__ == '__main__':
    manager.run()
