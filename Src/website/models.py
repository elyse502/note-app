from . import db  # Import the database instance created in __init__.py
from flask_login import UserMixin  # Import UserMixin for user authentication
from sqlalchemy.sql import func  # Import func for using database functions


# Define the Note class as a model for the 'note' table in the database
class Note(db.Model):
    """Model class for notes."""
    id = db.Column(db.Integer, primary_key=True)  # Define 'id' as the primary key
    data = db.Column(db.String(10000))  # Define 'data' as a string column with a length of 10000 characters
    date = db.Column(db.DateTime(timezone=True), default=func.now())  # Define 'date' as a datetime column with timezone, default value is current timestamp
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Define 'user_id' as a foreign key referencing the 'id' column in the 'user' table


# Define the User class as a model for the 'user' table in the database, inheriting from UserMixin for user authentication
class User(db.Model, UserMixin):
    """Model class for users."""
    id = db.Column(db.Integer, primary_key=True)  # Define 'id' as the primary key
    email = db.Column(db.String(150), unique=True)  # Define 'email' as a unique string column with a length of 150 characters
    password = db.Column(db.String(150))  # Define 'password' as a string column with a length of 150 characters
    first_name = db.Column(db.String(150))  # Define 'first_name' as a string column with a length of 150 characters
    notes = db.relationship('Note')  # Define a one-to-many relationship with the 'Note' model
