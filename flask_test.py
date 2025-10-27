from flask import Flask, render_template, request, redirect, url_for, flash
import json
from forms.input import LoginForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

with open('users.json', 'r') as f:
    users = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def signup():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        for user in users:
            if user['username'] == username:
                flash("Username already exists! Please log in instead.")
                return redirect(url_for('login'))

        # Otherwise register new user
        new_user = {
            "first_name": "Guest",
            "last_name": "User",
            "username": username,
            "password": password
        }
        users.append(new_user)

        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)

        flash("Signup successful! You can now log in.", "success")
        return redirect(url_for('login'))

    return render_template('index.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        for user in users:
            if user['username'] == username and user['password'] == password:
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
