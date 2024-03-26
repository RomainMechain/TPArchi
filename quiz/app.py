import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

def mkpath(p):
    """
    This function takes a path and normalizes it relative to the current file's directory.
    """
    return os.path.normpath(os.path.join(os.path.dirname(__file__), p))

app = Flask(__name__)
cors = CORS(app, resources={r"/quiz/api/v1.0/*": {"origins" : "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + mkpath('../quiz.db')
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)