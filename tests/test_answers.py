from uuid import uuid4
from killranswers.answers.models import Answer
from killranswers.connections import cassandra
from killranswers import *

cassandra()

def test_answer_question():
    u = User.create(user_id=uuid4())
    root = Category.get_root()
    cat = root.create_sub("monkey")
    question = Question.create(category=cat,
                               text="test question",
                               user=u)
    answer = Answer.create(user=u, question=question, text="monkey")
