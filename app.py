from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def load_posts():
    try:
        with open("posts.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_post(title, content):
    posts = load_posts()
    posts.append({"title": title, "content": content})
    with open("posts.json", "w") as f:
        json.dump(posts, f)

@app.route("/")
def home():
    posts = load_posts()
    return render_template("home.html", posts=posts)

@app.route("/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        save_post(title, content)
        return redirect("/")
    return render_template("new_post.html")

app.run(host="0.0.0.0", port=5000)