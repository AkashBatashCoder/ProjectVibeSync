from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager


class base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=base)


login_manager = LoginManager()
