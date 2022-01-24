from turtle import pos
from app.models.post_model import Post
from flask import jsonify
from http import HTTPStatus

def retrieve():
    posts_list = Post.get_all()

    posts_list = list(posts_list)

    for post in posts_list:
        post.update({"_id": str(post["_id"])})
    
    return jsonify(posts_list), HTTPStatus.OK


