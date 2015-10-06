from uuid import uuid1

from cassandra.cqlengine.models import Model
from cassandra.cqlengine.columns import *

def vote(rating_table):
    def f(self, user, vote):
        fields = {
            rating_table._partition_keys.items()[0][0] : self.id,
            "vote":vote,
            "user_id":user.user_id
        }
        rating_table.create(**fields)
        # what's the new rating?
        return 0
    return f


class QuestionRating(Model):
    question_id = TimeUUID(primary_key=True)
    user_id = Text(primary_key=True, index=True)
    vote = Integer()

class QuestionRatingAggregate(Model):
    question_id = TimeUUID(primary_key=True)
    score = Counter()

class AnswerRating(Model):
    answer_id = TimeUUID(primary_key=True)
    user_id = Text(primary_key=True, index=True)
    vote = Integer()

class AnswerRatingAggregate(Model):
    question_id = TimeUUID(primary_key=True)
    answer_id = TimeUUID(primary_key=True)
    score = Counter()
