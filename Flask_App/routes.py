from flask import render_template, url_for, flash, redirect
from Flask_App.forms import RegistrationForm, LoginForm
from Flask_App.models import User, Post
from Flask_App import app

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'goed')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':
            flash('You have been logged in!', 'goed')
            return redirect(url_for('home'))
        else:
            flash('Log in gefaald, probeer opnieuw!', 'failed')
    return render_template('login.html', form=form, title='Login')


@app.route('/blog')
def blog():
    posts = blog_posts
    return render_template('blog.html', title='Blog', blog_posts=posts)

# Route for service worker
@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')

