import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["turma7"]

class Dev:
    def __init__(*args, **kwargs) -> None:
        ...

    @staticmethod
    def get_all():
        devs_list = db.devs.find()

        return devs_list