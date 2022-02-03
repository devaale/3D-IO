from flask import Flask
from flask_socketio import SocketIO
from config import BaseConfig

sio = SocketIO(cors_allowed_origins="*")


def create_app(debug=False):
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    app.debug = debug
    sio.init_app(app)

    return app
