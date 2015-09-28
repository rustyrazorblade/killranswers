from uuid import uuid1

from cassandra.cqlengine.models import Model
from cassandra.cqlengine.columns import *


class Answer(Model):
    question_id = TimeUUID(primary_key=True)
    answer_id = TimeUUID(primary_key=True)
    user_id = Text()
    text = Text()

    @classmethod
    def create(cls, user, question, text):
        pass
