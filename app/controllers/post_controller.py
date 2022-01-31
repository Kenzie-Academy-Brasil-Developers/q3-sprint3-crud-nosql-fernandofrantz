from app.models.post_model import Post
from flask import jsonify, request
from http import HTTPStatus
from app import db
from datetime import datetime


def create_post():
    post = request.get_json()
    id = (len(list(db.posts.find()))) +1
    title = post.get('title')
    author = post.get('author')
    tag = post.get('tags')
    content = post.get('content')

    if (
    title == None or
    author == None or
    tag == None or
    content == None
    ):
        return {'Message': 'Wrong keys'}

    db.posts.insert_one(Post(id, title, author, tag, content).__dict__)
    return post, HTTPStatus.CREATED

def get_posts():
    posts_list = list(db.posts.find())
    for post in posts_list:
        post.update({'_id': str(post['_id'])})
    return jsonify(posts_list), HTTPStatus.OK
    
def get_post_by_id(id):
    posts_list = list(db.posts.find())
    for post in posts_list:
        post.update({'_id': str(post['_id'])})
    for post in posts_list:
        if(post['id'] == id):
            return jsonify(post), HTTPStatus.OK
    return {'message': "post with this id doesn't exist"}, HTTPStatus.NOT_FOUND

def update_post(id):
    posts_list = list(db.posts.find())
    post_to_edit = ''
    changes = request.get_json()
    post = request.get_json()

    title = post.get('title')
    author = post.get('author')
    tag = post.get('tags')
    content = post.get('content')

    if (
    title == None or
    author == None or
    tag == None or
    content == None
    ):
        return {'Message': 'Wrong keys'}

    for post in posts_list:
        if(post['id'] == id):
            title_change = changes.get('title')
            if(title_change != None): 
                db.posts.update_one({'id': id}, {"$set": {'title': title_change}})

            author_change = changes.get('author')
            if(author_change != None): 
                db.posts.update_one({'id': id}, {"$set": {'author': author_change}})

            tag_change = changes.get('tag')
            if(tag_change != None): 
                db.posts.update_one({'id': id}, {"$set": {'tags': tag_change}})

            content_change = changes.get('content')
            if(content_change != None): 
                db.posts.update_one({'id': id}, {"$set": {'content': content_change}})
                    
            db.posts.update_one({'id': id}, {"$set": {'updated_at': datetime.utcnow().strftime('%d/%m/%Y %H:%M:%S')}})

            for post in posts_list:
                post.update({'_id': str(post['_id'])})
            for post in posts_list:
                if(post['id'] == id):
                    post_to_edit = post
                    jsonify(post_to_edit)

            return {'msg': f'Post with id: {id} edited'}, HTTPStatus.OK
    return {'message': "post with this id doesn't exist"}, HTTPStatus.NOT_FOUND


def delete_post(id):
    db.posts.delete_one({'id': id})
    return '', HTTPStatus.OK