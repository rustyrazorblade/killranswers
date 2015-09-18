from cassandra.cqlengine import Model
from cassandra.cqlengine.types import *

class User(Model):
    user_id = TimeUUID(primary_key=True)
    name = Text()

class Question(Model)
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
        
