from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login')
def contact():
    return render_template('login.html')

@app.route('/register')
def contact():
    return render_template('regoster.html')


@app.route('/blog')
def contact():
    return render_template('blog.html')