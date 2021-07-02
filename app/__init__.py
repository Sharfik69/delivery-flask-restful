from flask import Flask

import config
from .database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    import app.views as delivery
    app.register_blueprint(delivery.module)

    return app
