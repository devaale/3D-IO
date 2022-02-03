import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SCHEMA = "http://"
    HOST = "localhost"
    PORT = 5050
    SECRET_KEY = "123456790"
