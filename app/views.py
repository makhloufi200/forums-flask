from flask import render_template, request, redirect, url_for, jsonify
from app import models
from app import app, member_store, post_store

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = post_store.get_all())


@app.route("/topic_add", methods = ["GET", "POST"])
def topic_add():
    if request.method == "POST":
        new_post = models.Post(request.form["title"], request.form["content"])
        post_store.add(new_post)
        return redirect(url_for("home"))

    else:
        return render_template("topic_add.html")

@app.route("/topic_delete/<int:id>")
def topic_delete(id):
    post_store.delete(id)
    return redirect(url_for("home"))

@app.route("/topic_edit/<int:id>", methods = ["GET", "POST"])
def topic_edit(id):
    posts = post_store.get_all()
    found_post = [post for post in  posts if post.id == id][0]
    if request.method == "POST":
        updated_post = post_store.get_by_id(id)
        updated_post.title = request.form["title"]
        updated_post.content = request.form["content"]
        post_store.update(updated_post)
        return redirect(url_for("home"))

    else:
        return render_template("topic_edit.html", post=found_post)

@app.route('/topic_show/<int:id>', methods = ["GET", "POST"])
def topic_show(id):
    posts = post_store.get_all()
    found_post = [post for post in  posts if post.id == id][0]
    if request.method == "POST":
        return redirect(url_for("home"))
    else:
        return render_template("topic_show.html", post=found_post)
