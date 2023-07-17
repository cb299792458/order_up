import os
from os import environ


class Configuration:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=environ.get("DATABASE_URL") or "postgresql://order_up:9uCxydbt@localhost/order_up_dev"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
