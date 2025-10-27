from flask import Flask, render_template
from piglatin import pig_latin
app = Flask(__name__)

@app.route('/')
def hello_world():
    # print("Hello, World!")
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# dynamic routing example
@app.route('/user/<username>')
def show_user_profile(username):
    return f'pig_latin: {dynamic_piglatin(username)}'

def dynamic_piglatin(name):
    return pig_latin(name)

if __name__ == '__main__':
    app.run(debug=True)