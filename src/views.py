"""
Routes and views for the flask application.
"""
from flask import render_template, g, current_app, Response, url_for

@app.route('/')
def summary():
    """Renders the home page."""
    current_app.logger.debug('idx=%s', url_for("summary"))
    return render_template(
        'index.html',
        title='Home Page'
    )
