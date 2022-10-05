import os

from flask import Flask


# initialising a application factory
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # __name__ is the name of the current Python module to tell the app where to set up paths
    # i_r_c = Ture means that configuration files hold local data not committed to version control

    # sets default config
    app.config.from_mapping(
        SECRET_KEY='dev',  # keep data safe
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),  # path to database
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
