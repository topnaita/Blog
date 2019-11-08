from flask import Flask, render_template, url_for 

app = Flask(__name__)

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


if __name__ == '__main__': 
    app.run(debug=True) 