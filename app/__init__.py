from flask import Flask

app = Flask(__name__)

from app.api import routes

app.run()