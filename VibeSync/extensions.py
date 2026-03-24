from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=base)
