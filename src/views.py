"""
Routes and views for the flask application.
"""
from flask import render_template, g, current_app, Response, url_for
from app import app


@app.route('/')
def parseFile():
    current_app.logger.debug('idx=%s', url_for("parseFile"))
    return render_template(
        'index.html',
        title='Parse File'
    )
