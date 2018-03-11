from flask import render_template, request, redirect, url_for, jsonify
from app import models
from app import app, member_store, post_store


@app.route("/api/topic/all")
def topic_get_all():
    posts = [post.__dict__ for post in post_store.get_all()]
    return jsonify(posts)

@app.route("/api/topic/add", methods = ["POST"])
def topic_create():
    request_data = request.get_json()
    new_post = models.Post(request_data["title"], request_data["content"])
    post_store.add(new_post)
    return jsonify(new_post.__dict__)

@app.route("/")
@app.route("/api/index")
def topic_api_home():
    posts = [post.__dict__ for post in post_store.get_all()]
    return jsonify(posts)

@app.route("/api/delete/<int:id>")
def topic_api_delete(id):
    post = post_store.get_by_id(id)
    post_store.delete(id)
    return jsonify(post.__dict__)

@app.route("/api/show/<int:id>")
def api_topic_show(id):
    post = post_store.get_by_id(id)
    return jsonify(post.__dict__)

@app.route("/api/edit/<int:id>", methods = ["GET", "POST"])
def api_topic_edit(id):
    request_data = request.get_json()
    updated_post = post_store.get_by_id(id)
    updated_post.title = request_data["title"]
    updated_post.content = request_data["content"]
    post_store.update(updated_post)
    return jsonify(updated_post.__dict__)