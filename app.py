''' Simple flask application '''
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    ''' Prints Hello World to the home page. '''
    return "<h1>Hello world</h1>"

@app.route("/hello")
def greetings():
    ''' Renders hello.html template. '''
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True, port='8001')
    