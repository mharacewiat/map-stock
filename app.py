from flask import Flask
from flask_jwt_extended import JWTManager
from injector import inject, noninjectable
from source.container import Container
from source.blueprint.auth import bp as auth_bp
from source.blueprint.maps import bp as maps_bp
from flask_injector import FlaskInjector
from click import argument
from bcrypt import hashpw, checkpw, gensalt
from source.gateway.message import MessageGateway
from source.model.user import User
from source.repository.map import MapRepository

from source.repository.user import UserRepository


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_envvar("CONFIG")

    app.register_blueprint(auth_bp)
    app.register_blueprint(maps_bp)

    JWTManager(app)
    flask_injector = FlaskInjector(app=app, modules=[Container])

    @app.cli.command("user")
    @argument("username")
    @argument("password")
    @argument("is_active", type=int)
    def user_cli(username: str, password: str, is_active: int):
        user_repository = flask_injector.injector.get(UserRepository)
        try:
            user = user_repository.get_user(username)
            user.password = password
            user.is_active = is_active
        except Exception:
            user = User(username=username, password=password, is_active=is_active)

        user.password = hashpw(password.encode(), gensalt()).decode()

        user_repository.save_user(user)

    @app.cli.command("queue")
    def queue_cli():
        message_gateway = flask_injector.injector.get(MessageGateway)
        map_repository = flask_injector.injector.get(MapRepository)
        
        try:
            map = message_gateway.receive()
            map.is_processed = 1
        except Exception:
            return

        map_repository.save_map(map)


    app.cli.add_command(user_cli)
    app.cli.add_command(queue_cli)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
