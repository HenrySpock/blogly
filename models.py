"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
# The above line was moved over from app.py.

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/img/1671"

def connect_db(app):
    db.app = app
    db.init_app(app)

# Models go below this point. This is where we define our schema:
class User(db.Model):
    """User."""

    __tablename__ = "users"

    @classmethod    
    def get_by_first_namee(cls, first_name):
        return cls.query.filter_by(first_name=first_name).all()

    @classmethod    
    def get_by_last_namee(cls, last_name):
        return cls.query.filter_by(last_name=last_name).all()
  

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable = False)
    last_name = db.Column(db.Text, nullable = False)
    image_url = db.Column(db.Text, nullable = False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"

def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)