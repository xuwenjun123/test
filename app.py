from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/world')
def world():
    return 'hello world'

if __name__ == '__main__':
    app.debug = True
    app.run()
