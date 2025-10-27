from flask import Flask
from piglatin import pig_latin
app = Flask(__name__)

@app.route('/')
def hello_world():
    # print("Hello, World!")
    return 'Hello, World! from flask1111'

@app.route('/about')
def about():
    return 'About Page'

# dynamic routing example
@app.route('/user/<username>')
def show_user_profile(username):
    return f'pig_latin: {dynamic_piglatin(username)}'

def dynamic_piglatin(name):
    return pig_latin(name)

if __name__ == '__main__':
    app.run(debug=True)