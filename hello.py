from flask import Flask, render_template

app = Flask(__name__)
posts=[
    {
        "author":"joy",
        "title":"run",
        "content":"post1"

    },
      {
        "author":"joy",
        "title":"run",
        "content":"post1"

    }
]
@app.route("/home")
def home():
    return render_template ("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template ("about.html",titel="about page")
