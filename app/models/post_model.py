from datetime import datetime
from venv import create


class Post:
    def __init__(self, id, title, author, tags, content) -> None:
        self.id = id
        self.created_at = datetime.utcnow().strftime('%d/%m/%Y %H:%M:%S')
        self.updated_at = datetime.utcnow().strftime('%d/%m/%Y %H:%M:%S')
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content

    # @staticmethod
    # def get_all():
    #     posts_list = db.find()
    #     return posts_list