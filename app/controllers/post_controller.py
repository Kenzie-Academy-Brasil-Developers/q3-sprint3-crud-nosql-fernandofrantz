from app.models.post_model import Post
from flask import jsonify, request
from http import HTTPStatus
from app import db


def create_post():
    post = request.get_json()
    id = (len(list(db.posts.find()))) +1
    title = post.get('title')
    author = post.get('author')
    tag = post.get('tag')
    content = post.get('content')
    if (
    title == None or
    author == None or
    tag == None or
    content == None
    ):
        return {'Message': 'Wrong keys'}
    return post, 200
    
