from flask import Flask, render_template 

app = Flask(__name__)

post = [
    {
        'author' : 'javier',
        'title' : 'Python tutorial',
        'content' : 'new york',
        'date_posted' : 'april 22 2019'    


    },
    {
        'author' : 'jean',
        'title' : 'Flask framework',
        'content' : 'france',
        'date_posted' : 'april 22 2019'


    }


]


@app.route('/')
def home(): 
    return render_template('home.html', post=post)

@app.route('/about')
def about(): 
    return render_template('about.html')


if __name__ == '__main__': 
    app.run(debug=True)