from flask import Flask
from config import Config

app = Flask(__name__)
# load some configurations to the app instance
app.config.from_object(Config)

from app import routes