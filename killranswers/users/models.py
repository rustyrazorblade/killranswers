from uuid import uuid1

from cassandra.cqlengine.models import Model
from cassandra.cqlengine.columns import *


class User(Model):
    """
    users are created with UUIDs, managed internally
    create a user in killranswers for every user in your system
    we'll keep the mapping in killranswers
    """
    user_id = Text(primary_key=True)
    @classmethod
    def create(cls, user_id):
        return super(cls, User).create(user_id=str(user_id))

    @classmethod
    def get(cls, user_id):
        return super(cls, User).get(user_id=str(user_id))

class UserCategorySubscription(Model):
    user_id = Text(primary_key=True)
    category_id = TimeUUID(primary_key=True)
