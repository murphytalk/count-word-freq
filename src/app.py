"""
The flask application package.
"""
from os import environ
from platform import node
from flask import Flask
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.exceptions import NotFound

deployed_in_production = node() == "anchor"
DEBUG = not deployed_in_production

# deployed behind ngix
URL_ROOT = "/word" if deployed_in_production else None

UPLOAD_DIR = environ.get('UPLOAD_DIR')
FREQ = environ.get('FREQ')

app = Flask(__name__)
# load all uppercase variables ad configuration
app.config.from_object(__name__)
app.debug = DEBUG

if URL_ROOT is not None:
    app.config["APPLICATION_ROOT"] = URL_ROOT
    application = DispatcherMiddleware(NotFound, {URL_ROOT: app})
else:
    application = app

import views
