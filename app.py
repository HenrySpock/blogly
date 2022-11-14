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
def red_users():
    """Shows list of all users in db.""" 
    return redirect('/users')

@app.route('/users')
def list_users():
    """Shows list of all users in db."""
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route("/users/new_user", methods=["GET"])
def new_user_form():
    """Display the new user form."""
    return render_template("users/new_user.html")
 
@app.route("/users/new_user", methods=["POST"]) 
def add_user():
    """Create new user from form submission."""

    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None)

    db.session.add(new_user)
    db.session.commit() 
    return redirect(f"/{new_user.id}")

@app.route("/<int:user_id>")
def show_user(user_id):
    """Show details about a single user.""" 
    user = User.query.get_or_404(user_id)
    return render_template("user_details.html", user=user)

# @app.route("/edit")
# def edit_user(user_id):
#     """Edit details about a single user."""
#     updated_user = User(

#     )
#     user = User.query.get_or_404(user_id)
#     return render_template("user_details.html", user=user)    
# @app.route('/users/<int:user_id>/edit')
# def users_edit(user_id):
#     """Show a form to edit an existing user"""

#     user = User.query.get_or_404(user_id)
#     return render_template('users/edit.html', user=user)

@app.route('/users/<int:user_id>/edit_user', methods=["GET"])
def users_edit(user_id):
    """Show a form to edit an existing user"""

    user = User.query.get_or_404(user_id)
    return render_template('users/edit_user.html', user=user)


@app.route('/users/<int:user_id>/edit_user', methods=["POST"])
def users_update(user_id):
    """Handle form submission for updating an existing user"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect(f"/{user.id}")

@app.route('/users/<int:user_id>/delete', methods=["GET"])
def delete(user_id):
    """Get route for form submission for deleting an existing user"""

    user = User.query.get_or_404(user_id)
    return redirect("/users")

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")