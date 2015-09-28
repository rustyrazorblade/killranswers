from uuid import uuid1

from cassandra.cqlengine.models import Model
from cassandra.cqlengine.columns import *


class User(Model):
    """
    users are created with UUIDs, managed internally
    you'll want to map this in your application's user database
    create a user in killranswers for every user in your system
    """
    user_id = TimeUUID(primary_key=True, default=uuid1)

class UserCategorySubscription(Model):
    user_id = TimeUUID(primary_key=True)
    category_id = TimeUUID(primary_key=True)
