from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e0fff506caeff08d660240ee10e953e9'

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
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/photos')
def photos():
    photos = photo_galery
    return render_template('photos.html', title="Foto's", photos=photos)


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
