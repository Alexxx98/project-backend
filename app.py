''' Simple flask application '''
from flask import Flask,render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    ''' Render from on main page. '''
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    ''' Redirect to hello, <name> page. '''
    name = request.form['name']
    return redirect(url_for('hello', name=name))

@app.route('/hello/<name>')
def hello(name):
    ''' Render gretings. '''
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, port=8001)
    