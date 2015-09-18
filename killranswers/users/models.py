from uuid import uuid1

from cassandra.cqlengine import Model
from cassandra.cqlengine.types import *


class User(Model):
    """
    users are created with UUIDs, managed internally
    you'll want to map this in your application's user database
    create a user in killranswers for every user in your system
    """
    user_id = TimeUUID(primary_key=True, default=uuid1)
    name = Text()

class UserCategorySubscription(Model):
    user_id = TimeUUID(primary_key=True)
    category_id = TimeUUID(primary_key=True)
