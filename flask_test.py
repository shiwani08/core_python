from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory 'database' just for demo
users = {'username': 'password'}

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # if username already exists, go to login page
        if username in users:
            return redirect(url_for('login'))
        
        # otherwise register new user
        users[username] = password
        return redirect(url_for('login'))

    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if credentials are correct
        if username in users and users[username] == password:
            return redirect(url_for('home'))
        else:
            return "Invalid username or password. Try again!"

    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
