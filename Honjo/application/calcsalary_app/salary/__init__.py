from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from .middleware.AuthMiddleware import AuthMiddleware
app = Flask(__name__)
app.config.from_object('salary.config')
# app.wsgi_app=AuthMiddleware(app.wsgi_app)
db = SQLAlchemy(app)

import salary.views