from flask import Flask, render_template, url_for
from form import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ffd79c9998ddd0390606eedfada4a806'

posts = [
    {
        'author': 'Ossama Akram',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'data_posted': 'Feb 21, 2019'
    },
    {
        'author': 'Mercedes Benz',
        'title': 'Blog Post 2',
        'content': 'w124 rocks',
        'data_posted': 'Feb 21, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='about')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)