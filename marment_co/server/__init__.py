# -*- coding: utf-8 -*-

from __future__ import with_statement, print_function, absolute_import

import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

__version__ = '0.1.0'

# Define the WSGI application object
app = Flask(__name__,
            static_folder="../client/dist/static",
            template_folder="../client/dist")

# Load config for current environment (Development / Production)
app.config.from_object(os.environ['CONFIG_PROFILE'])

# enable CORS
CORS(app)

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

import server.view
import server.projects
