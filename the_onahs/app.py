from flask import Flask
from .extensions import mail


ROOT_URL = '/'


def create_app(config_name):
    from the_onahs.config import app_config

    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    # app.config["APPLICATION_ROOT"] = ROOT_URL

    # app.register_blueprint(apidoc, url_prefix=ROOT_URL)

    with app.app_context():
        from the_onahs.api_v1 import blueprint as api
        from the_onahs.healthcheck import healthcheck

        app.register_blueprint(api, url_prefix=ROOT_URL)
        app.register_blueprint(healthcheck, url_prefix=ROOT_URL)

        extensions(app)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    mail.init_app(app)

    return None
