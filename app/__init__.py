"""

(c) 2019 - ModoUnreal

"""


import os

from flask import Flask


def create_app(test_config=None):
    """Create and configure the application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev', # The secret key will change, after development.
        DATABASE=os.path.join(app.instance_path, 'access.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing.
        app.config.from_pyfile('config.py', silent=True)

    else:
        # Load the test config if passed on.
        app.config.from_mapping(test_config)

    # Ensure that the instance folder exists.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Test with simple view.
    @app.route('/cheeky')
    def cheeky():
        return "Hey this is Alex Hurtado, I'm a cheeky boi."

    @app.route('/')
    def index():
        return "TESTING"

    return app

app = create_app()
