from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e0fff506caeff08d660240ee10e953e9'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}"

blog_posts = [
    {'title': 'Test Post 1',
     'content': '''Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis illo delectus saepe, error quisquam pariatur laudantium at ab repellendus nihil. Similique dolor vero soluta adipisci doloribus repellendus exercitationem voluptatum qui.
    Deze tekst moet lang zijn vandaar al deze zever, hierna zal deze zever nog eens voorkomen gewoon voor de tekst te vullen Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis illo delectus saepe, error quisquam pariatur laudantium at ab repellendus nihil. Similique dolor vero soluta adipisci doloribus repellendus exercitationem voluptatum qui. 
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis illo delectus saepe, error quisquam pariatur laudantium at ab repellendus nihil. Similique dolor vero soluta adipisci doloribus repellendus exercitationem voluptatum qui.
    Deze tekst moet lang zijn vandaar al deze zever, hierna zal deze zever nog eens voorkomen gewoon voor de tekst te vullen Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis illo delectus saepe, error quisquam pariatur laudantium at ab repellendus nihil. Similique dolor vero soluta adipisci doloribus repellendus exercitationem voluptatum qui.
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis illo delectus saepe, error quisquam pariatur laudantium at ab repellendus nihil. Similique dolor vero soluta adipisci doloribus repellendus exercitationem voluptatum qui.
    Deze tekst moet lang zijn vandaar al deze zever, hierna zal deze zever nog eens voorkomen gewoon voor de tekst te vullen Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis illo delectus saepe, error quisquam pariatur laudantium at ab repellendus nihil. Similique dolor vero soluta adipisci doloribus repellendus exercitationem voluptatum qui.
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis illo delectus saepe, error quisquam pariatur laudantium at ab repellendus nihil. Similique dolor vero soluta adipisci doloribus repellendus exercitationem voluptatum qui.
    Deze tekst moet lang zijn vandaar al deze zever, hierna zal deze zever nog eens voorkomen gewoon voor de tekst te vullen Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis illo delectus saepe, error quisquam pariatur laudantium at ab repellendus nihil. Similique dolor vero soluta adipisci doloribus repellendus exercitationem voluptatum qui.
    ''',
     'date': '05/06/2020', 'photo': 'images/test.png'},
    {'title': 'Test Post 2',
     'content': 'Dit is een tweede test post',
     'date': '05/06/2020',
     'photo': False
     }
]

photo_galery = [
    {'preview': '/images/galeryTest/daylight-forest-preview.jpg',
     'full': '/images/galeryTest/daylight-forest-full.jpg',
     'alt': 'Forest in daylight',
     },
    {
        'preview': '/images/galeryTest/gray-bridge-and-trees-preview.jpg',
        'full': '/images/galeryTest/gray-bridge-and-trees-full.jpg',
        'alt': 'Bridge with trees'
    },
    {
        'preview': '/images/galeryTest/scenic-view-of-mountain-preview.jpg',
        'full': '/images/galeryTest/scenic-view-of-mountain-full.jpg',
        'alt': 'Mountains'
    },
    {
        'preview': '/images/galeryTest/view-of-elephant-in-water-preview.jpg',
        'full': '/images/galeryTest/view-of-elephant-in-water-full.jpg',
        'alt': 'Olifanten in het water'
    },
    {
        'preview': '/images/galeryTest/nature-red-forest-leaves-preview.jpg',
        'full': '/images/galeryTest/nature-red-forest-leaves-full.jpg',
        'alt': 'Herfst'
    },
    {
        'preview': '/images/galeryTest/nature-red-forest-leaves-preview.jpg',
        'full': '/images/galeryTest/nature-red-forest-leaves-full.jpg',
        'alt': 'Herfst'
    },
    {
        'preview': '/images/galeryTest/nature-red-forest-leaves-preview.jpg',
        'full': '/images/galeryTest/nature-red-forest-leaves-full.jpg',
        'alt': 'Herfst'
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/photos')
def photos():
    photos = photo_galery
    return render_template('photos.html', title="Foto's", photos=photos)


@app.route('/register') #methods=['GET', 'POST']
def register():
    form = RegistrationForm()
    # if form.validate_on_submit():
    #     flash(f'Account created for {form.username.data}!', 'goed')
    #     return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login') # methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if form.validate_on_submit():
    #     if form.username.data == 'admin' and form.password.data == 'password':
    #         flash('You have been logged in!', 'goed')
    #         return redirect(url_for('home'))
    #     else:
    #         flash('Log in gefaald, probeer opnieuw!', 'failed')
    return render_template('login.html', form=form, title='Login')


@app.route('/blog')
def blog():
    posts = blog_posts
    return render_template('blog.html', title='Blog', blog_posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
