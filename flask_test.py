from flask import Flask, render_template, request, redirect, url_for, flash
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# In-memory 'database' just for demo
with open('users.json', 'r') as f:
    users = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if username already exists
        for user in users:
            if user['username'] == username:
                return redirect(url_for('login'))

        # Otherwise register new user
        new_user = {
            "first_name": request.form.get('first_name'),
            "last_name": request.form.get('last_name'),
            "username": request.form.get('username'),
            "password": request.form.get('password')
        }
        users.append(new_user)

        # Save to JSON file
        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)

        return redirect(url_for('login'))

    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if credentials are correct
        for user in users:
            if user['username'] == username and user['password'] == password:
                flash(f"Welcome back, {user['first_name']}!")
                return redirect(url_for('home'))

        flash("User not found, please sign up")
        return redirect(url_for('signup'))

    # If method is GET, just show the login page
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
