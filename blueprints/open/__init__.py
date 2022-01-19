from flask import Blueprint, render_template, redirect, url_for, request, flash

# Create a blueprint object that can be used as an app object for this blueprint
from werkzeug.security import generate_password_hash

from models import User

bp_open = Blueprint('bp_open', __name__)


@bp_open.get('/')
def index():
    return render_template("index.html")


@bp_open.get('/login')
def login_get():
    return render_template('login.html')


@bp_open.get('/signup')
def signup_get():
    return render_template('signup.html')


@bp_open.post('/signup')
def signup_post():
    name = request.form['name']
    email = request.form.get('email')
    password = request.form['password']
    hashed_password = generate_password_hash(password, method='sha256')

    # Check if user with this password exists in the database
    user = User.query.filter_by(email=email).first()  # First will give us object if user exist, or None if not
    if user:
        # If user is not none, then a user with this email exists in the database
        flash("Email address is already in use")
        return redirect(url_for('bp_open.signup_get'))

    new_user = User(name=name, email=email, password=hashed_password)

    from app import db
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('bp_open.login_get'))