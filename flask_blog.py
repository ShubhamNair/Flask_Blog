from flask import Flask, request, render_template, url_for
from markupsafe import escape

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)

