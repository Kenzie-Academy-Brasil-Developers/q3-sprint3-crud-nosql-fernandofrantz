import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["posts"]

class Post:
    def __init__(*args, **kwargs) -> None:
        ...

    @staticmethod
    def get_all():
        posts_list = db.find()
        return posts_list