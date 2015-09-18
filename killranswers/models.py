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

class Category(Model):
    category_id = TimeUUID(primary_key=True, default=uuid1)
    name = Text()
    parent_categories = List(TimeUUID) # first parent on the left, root at the end
    # parent_category_id = TimeUUID(primary_key=True)

    @classmethod
    def create(self, parent, name):
        pass

    @classmethod
    def create_root(self, name):
        # creating a root category has slightly different rules
        pass

    @property
    def parent(self):
        # returns a single Category object or None

    @property
    def parents(self):
        # returns a list of category objects

    # track the full category list


    def move(self, new_parent):
        """
        moves to a new parent category
        updates the category children
        updates the category counts
        """
        pass


class CategoryCounters(Model):
    category_id = TimeUUID()
    questions = Counter()
    answers = Counter()

class CategoryChildren(Model):
    """
    maintaining the list of children of a given category
    """
    category_id = TimeUUID(primary_key=True)
    child_category_id = TimeUUID(primary_key=True)
    child_category_name = Text()

class Question(Model):
    question_id = TimeUUID(primary_key=True, default=uuid1)
    user_id = TimeUUID()
    text = Text()
    user = Text() # user's name
    category_id = TimeUUID()

    @classmethod
    def create(cls, user, text):
        pass

class QuestionByCategory(Model):
    # sorted by newest first
    category_id = TimeUUID(primary_key=True)
    question_id = TimeUUID(primary_key=True, clustering_order="DESC")

class Answer(Model):
    question_id = TimeUUID(primary_key=True)
    answer_id = TimeUUID(primary_key=True)
    user_id = TimeUUID()
    text = Text()
    user = Text() # user's name

    @classmethod
    def create(cls, user, question, text):
        pass

class UserCategorySubscription(Model):
    user_id = TimeUUID(primary_key=True)
    category_id = TimeUUID(primary_key=True)

class QuestionRating(Model):
    # probably just an upvote 1 / downvote 0 thing
    question_id = TimeUUID(primary_key=True)
    user_id = TimeUUID(primary_key=True)
    rating = Int()
