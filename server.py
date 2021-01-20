#!/usr/bin/env python
import flask
# Create the application.
APP = flask.Flask(__name__)

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    pass


if __name__ == '__main__':
    APP.debug=True
    APP.run()
