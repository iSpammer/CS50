from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index(username):
    # show the user profile for that user
    return 'Hello %s' % username
