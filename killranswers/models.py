from uuid import uuid1

from cassandra.cqlengine import Model
from cassandra.cqlengine.types import *

class User(Model):
    """
    users are created with UUIDs, managed internally
    you'll want to map this in your application's user database
    create a user in killranswers for every user in your system
    """
    user_id = TimeUUID(primary_key=True)
    name = Text()

class Category(Model):
    category_id = TimeUUID(primary_key=True)
    name = Text()
    parent_categories = List(TimeUUID)
    # parent_category_id = TimeUUID(primary_key=True)

    @property
    def parent(self):
        # returns a single Category object

    @property
    def parents(self):
        # returns a list of category objects

    # track the full category list


    def move(self, new_parent):
        """
        moves to a new parent category
        updates the category children
        """
        pass


class CategoryStats(Model):
    pass

class CategoryChildren(Model):
    """
    maintaining the list of children of a given category
    """
    category_id = TimeUUID(primary_key=True)
    child_category_id = TimeUUID(primary_key=True)
    child_category_name = Text()

class Question(Model):
    question_id = TimeUUID(primary_key=True)
    user_id = TimeUUID()
    text = Text()
    user = Text() # user's name

    @classmethod
    def create(cls, user, text):
        pass



class Answer(Model):
    question_id = TimeUUID(primary_key=True)
    answer_id = TimeUUID(primary_key=True)
    user_id = TimeUUID()
    text = Text()
    user = Text() # user's name

    @classmethod
    def create(cls, user, question, text):
        pass
