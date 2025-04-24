from app import app
from flask import render_template # type: ignore

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')