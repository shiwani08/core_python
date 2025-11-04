from flask import Blueprint, render_template, redirect, url_for, flash
from forms.input import LoginForm
from models.users_model import UserModel
from flask import current_app

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def signup():
    form = LoginForm()
    mongo = current_app.extensions['pymongo']  
    users_collection = mongo.db.users

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if users_collection.find_one({"username": username}):
            flash("Username already exists! Please log in instead.")
            return redirect(url_for('auth.login'))

        new_user = UserModel(first_name="Guest", last_name="User", username=username, password=password)
        new_user.save(users_collection)

        flash("Signup successful! You can now log in.", "success")
        return redirect(url_for('auth.login'))

    return render_template('index.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    mongo = current_app.extensions['pymongo']  # ✅ Same here
    users_collection = mongo.db.users

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = users_collection.find_one({"username": username, "password": password})
        if user:
            flash(f"Welcome back, {user['first_name']}!", "success")
            return redirect(url_for('main.home'))

        flash("Invalid credentials. Please sign up first.", "error")
        return redirect(url_for('auth.signup'))

    return render_template('login.html', form=form)
