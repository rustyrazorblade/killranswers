from uuid import uuid1

from cassandra.cqlengine.models import Model
from cassandra.cqlengine.columns import *



class Question(Model):
    __table_name__ = "question"
    question_id = TimeUUID(primary_key=True, default=uuid1)
    user_id = Text()
    text = Text()
    category_id = UUID(required=True)

    @classmethod
    def create(cls, category, text, user):
        user_id = user.user_id
        question = super(cls, Question).\
                    create(category_id=category.category_id,
                           text=text,
                           user_id=str(user_id))

        # update category statistics
        return question

class QuestionByCategory(Model):
    # sorted by newest first
    category_id = TimeUUID(primary_key=True)
    question_id = TimeUUID(primary_key=True, clustering_order="DESC")


class QuestionRating(Model):
    # probably just an upvote 1 / downvote 0 thing
    question_id = TimeUUID(primary_key=True)
    user_id = Text(primary_key=True)
    rating = Integer()
