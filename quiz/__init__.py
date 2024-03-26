import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from .app import app
import quiz.views
import quiz.commande
import quiz.models