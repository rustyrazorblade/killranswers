from uuid import uuid1

from cassandra.cqlengine.models import Model
from cassandra.cqlengine.columns import *
from killranswers.answers.models import Answer
from killranswers.ratings.models import QuestionRating, vote

class Question(Model):
    __table_name__ = "question"
    question_id = TimeUUID(primary_key=True, default=uuid1)
    user_id = Text()
    title = Text()
    text = Text() # body of question
    #category_id = UUID(required=True)

    @classmethod
    def create(cls, category, text, user):
        user_id = user.user_id

        # text cleanup?
        question = super(cls, Question).\
                    create(category_id=category.category_id,
                           text=text,
                           user_id=str(user_id))

        QuestionByCategory.create(category_id=question.category_id,
                                  question_id=question.question_id,
                                  user_id=user.user_id,
                                  text=text)
        # update category statistics
        return question

    @classmethod
    def get(cls, question_id):
        return super(cls, Question).get(question_id=question_id)

    def answer(self, user, text):
        answer = Answer.create(user, self, text)
        return answer

    def get_answers(self, offset_answer=None, limit=None):
        answers = Answer.objects(question_id=self.question_id)
        return answers

    @property
    def id(self):
        return self.question_id


Question.vote = vote(QuestionRating)


class QuestionByCategory(Model):
    # sorted by newest first
    category_id = UUID(primary_key=True, partition_key=True)
    # day = DateTime(primary_key=True, partition_key=True)
    question_id = TimeUUID(primary_key=True, clustering_order="DESC")
    user_id = Text()
    text = Text(required=True)


class QuestionByCategorySorted(Model):
    """
    using day to limit the tombstone effect for paginating way back
    """
    category_id = UUID(primary_key=True, partition_key=True)
    day = DateTime(primary_key=True, partition_key=True)
    sort_key = TimeUUID(primary_key=True, clustering_order="DESC")
    question_id = TimeUUID()
