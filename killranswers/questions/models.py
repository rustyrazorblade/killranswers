from uuid import uuid1

from cassandra.cqlengine import Model
from cassandra.cqlengine.types import *



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


class QuestionRating(Model):
    # probably just an upvote 1 / downvote 0 thing
    question_id = TimeUUID(primary_key=True)
    user_id = TimeUUID(primary_key=True)
    rating = Int()
