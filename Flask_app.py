from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e0fff506caeff08d660240ee10e953e9'

blog_posts = [
    {'title': 'Test Post 1',
    'content': 'Dit is een erste test post',
    'date': '05/06/2020'},
    {'title': 'Test Post 2',
    'content': 'Dit is een tweede test post',
    'date': '05/06/2020'}
]



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form, title='Login')

@app.route('/blog')
def blog():
    posts = blog_posts
    return render_template('blog.html', title='Blog', blog_posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
