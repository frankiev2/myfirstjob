## note the default port is 5000 FYI
import os
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


#@app.route('/<name>')
@app.route('/o-dogg')
def hello_name(name):
    return "Hello {}!".format("name")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
