from flask import Flask
from source.container import Container
from source.blueprint.auth import bp as auth_bp
from source.blueprint.maps import bp as maps_bp
from flask_injector import FlaskInjector


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(maps_bp)

    FlaskInjector(app=app, modules=[Container])

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
