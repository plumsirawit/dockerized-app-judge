from flask import Flask
app = Flask(__name__)

from cloner import clone
from builder import build
from runner import run
from grader import grade

@app.route('/')
def index():
    return 'Hi'