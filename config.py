from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
if os.environ['FLASK_ENV'] == 'test':
    database_url = os.getenv('TEST_DATABASE_URL')
else:
    database_url = os.getenv('DATABASE_URL')


SQLALCHEMY_DATABASE_URI = database_url
SQLALCHEMY_TRACK_MODIFICATIONS = False
