from flask import Flask, request, render_template, url_for
from markupsafe import escape
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '24fe825fc80a9203826c5a7f54023867'

posts=[
    {
        "author":"Shubham Nair",
        "title": "Blog post 1",
        "content": "First Post",
        "date_posted": "Jan 30, 2024"
    },
{
        "author":"Jane Doe",
        "title": "Blog post 2",
        "content": "Second Post",
        "date_posted": "Jan 31, 2024"
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts )

@app.route('/about')
def about():
    return render_template("about.html",title="About")

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form= form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form= form)

if __name__ == "__main__":
    app.run(debug=True)

