
from flask import render_template, url_for, flash, redirect
from index import app
from index.forms import RegistratitonForm, LoginForm
from index.models import User, Post

post = [
    {
        'author' : 'javier',
        'title' : 'First post',
        'content' : 'new york',
        'date_posted' : 'april 22 2019'


    },
    {
        'author' : 'jean',
        'title' : 'Second post',
        'content' : 'france',
        'date_posted' : 'april 22 2019'


    }
]

@app.route('/')
def home():
    return render_template('home.html', post=post)

@app.route('/about')
def about():
    return render_template('about.html', title='about')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistratitonForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') #concatenacion
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
