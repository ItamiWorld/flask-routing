# Flask class import
from flask import Flask
from markupsafe import escape

# Create a instance of Flask class. The first argument is the name of the application's module or package.
# @__name__ argument is convenient shortcut. This is needed to look for resources as templates or static files.
app = Flask(__name__)

# Use route() decorator to tell Flask what URL should trigger the function.
@app.route('/')
def index():
    return 'Index Page'

@app.route('/string')
def string():
    return 'Hello, world'

@app.route('/html')
def html():
    return '<p>Hello, world</p>'

