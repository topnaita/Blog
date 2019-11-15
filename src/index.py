from flask import Flask, render_template, url_for, flash, redirect 
from forms import RegistratitonForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = 'kfjmdo771e0fcod55e48e789w5d2c'
app.config['SLQALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)




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

if __name__ == '__main__': 
    app.run(debug=True) 