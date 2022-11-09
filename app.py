"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bloglydb' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "thekey"
app.config['DEBUG_TB_INTERCEPT_REDIERECTS'] = False 
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def list_users():
    """Shows list of all users in db."""
    users = User.query.all()
    return render_template('index.html', users=users)

# @app.route("/users/new_user", methods=["POST"])
@app.route("/users/new_user", methods=["POST"]) 
def add_user():
    """Create new user from form submission."""

    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None)

    db.session.add(new_user)
    db.session.commit()

    return render_template("/")
    # return redirect(f"/{new_user.id}")

# @app.route("/<int:user_id>")
# def show_user(user_id):
#     """Show details about a single user.""" 
#     user = User.query.get_or_404(user_id)
#     return render_template("user_details.html", user=user)