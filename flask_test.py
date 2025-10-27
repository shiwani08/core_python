from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from forms.input import LoginForm
from dotenv import load_dotenv
import os
import json
from pymongo.errors import ConnectionFailure

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'supersecretkey')

# MongoDB connection setup
app.config['MONGO_URI'] = os.getenv('MONGODB_URL')
mongo = PyMongo(app)

try:
    mongo.cx.server_info()
    print("✅ Connected to MongoDB successfully.")

    users_collection = mongo.db.users_data
    # Import users.json data if empty
    if users_collection.count_documents({}) == 0:
        with open('users.json', 'r') as f:
            users_data = json.load(f)
            if isinstance(users_data, list):
                users_collection.insert_many(users_data)
            else:
                users_collection.insert_one(users_data)
        print("📁 Imported users.json into MongoDB successfully.")
except ConnectionFailure as e:
    print(f"❌ Could not connect to MongoDB: {e}")

@app.route('/', methods=['GET', 'POST'])
def signup():
    form = LoginForm()
    users_collection = mongo.db.users

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Check if user already exists
        if users_collection.find_one({"username": username}):
            flash("Username already exists! Please log in instead.")
            return redirect(url_for('login'))

        new_user = {
            "first_name": "Guest",
            "last_name": "User",
            "username": username,
            "password": password
        }

        users_collection.insert_one(new_user)
        flash("Signup successful! You can now log in.", "success")
        return redirect(url_for('login'))

    return render_template('index.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    users_collection = mongo.db.users

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = users_collection.find_one({"username": username, "password": password})
        if user:
            flash(f"Welcome back, {user['first_name']}!", "success")
            return redirect(url_for('home'))

        flash("Invalid credentials. Please sign up first.", "error")
        return redirect(url_for('signup'))

    return render_template('login.html', form=form)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
