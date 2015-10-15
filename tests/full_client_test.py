import sys
sys.path.append("")

import capnp
import killranswers_capnp
import socket
from uuid import uuid4
from time import time

if __name__  == "__main__":
    client = capnp.TwoPartyClient("127.0.0.1:6000")
    cap = client.bootstrap()
    cap = cap.cast_as(killranswers_capnp.KillrAnswers)

    # create users

    x = 1000
    start = time()
    for i in range(x):
        # print "Registering user", i
        cap.registerUser(str(uuid4())).wait()

        if i % 50 == 1:
            total = time() - start
            print "Time: {}, {} per user, {} per second".format(total, total / i, i / total)

    user_id = str(uuid4())
    user = cap.registerUser(user_id)

    sys.exit()


    # get root category
    root = cap.getRootCategory().wait()
    cat = root.category.id
    print 'root cat: ', cat

    new_cat = cap.createCategory(text="api provided name",
                                 parent=cat).wait()
    print new_cat
    # create a sub category of the new category

    # get child categories of the root
    children = cap.getChildCategories(cat).wait()
    print "children ", children

    # the oldest question in the universe
    result = cap.ask(text="Dr. Who?",
                     category=new_cat.category,
                     user=user_id).wait()
    print "api question: ", result

    q = result.question

    user_id2 = str(uuid4())
    user2 = cap.registerUser(user_id2).wait()
    print "Question rating: ", cap.voteQuestion(q, user_id2, 1).wait()

    # answer the question...
    answer = cap.answer(question=q, user=user_id, text="Silence will fall.").wait()
    print answer

    # rate the answer
    print "Answer rating: ", cap.voteAnswer(q, answer.answer, user_id2, 1).wait()

    # add a few more
    answer = cap.answer(question=q, user=user_id, text="Open the pandorica.").wait()
    answer = cap.answer(question=q, user=user_id, text="Reboot the universe.").wait()

    # get the answers
    answers = cap.getAnswers(q).wait()
    print answers

    answer = cap.answer(question=q, user=user_id, text="Open the pandorica.  Again.")
    answer = cap.answer(question=q, user=user_id, text="Reboot the universe. Again")
    answers = cap.getAnswers(q).wait()
    print answers

    # simple load test
    start = time()
    i = 10
    for x in range(i):
        p = cap.answer(question=q, user=user_id, text="Test {}".format(x))
    answer = p.wait()
    taken = time() - start
    # answers = cap.getAnswers(q.id).wait()
    print answers
    print "time taken: {}, {} per sec".format(taken, float(i) / taken)

    answer.answer
