from bson import ObjectId
from app.database.mongo import db

class UserRepository:

    collection = db.users

    @classmethod
    def create(cls, user):

        return cls.collection.insert_one(user)

    @classmethod
    def get_all(cls):

        return list(cls.collection.find())

    @classmethod
    def get_by_cedula(cls, cedula):

        return cls.collection.find_one({
            "cedula": cedula
        })

    @classmethod
    def delete(cls, user_id):

        return cls.collection.delete_one({
            "_id": ObjectId(user_id)
        })