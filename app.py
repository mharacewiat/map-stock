from flask import Flask
from source.auth import bp as auth_bp
from source.maps import bp as maps_bp


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(auth_bp)
    app.register_blueprint(maps_bp)

    @app.route('/')
    def hello_geek():
        return '<h1>Hello world!</h1>'

    return app


if __name__ == "__main__":
    create_app.run(debug=True)
