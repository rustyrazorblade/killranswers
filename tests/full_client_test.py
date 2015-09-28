import sys
sys.path.append("")

import capnp
import killranswers_capnp
import socket
from uuid import uuid4
from time import time

if __name__  == "__main__":
    client = capnp.TwoPartyClient("localhost:6000")
    cap = client.bootstrap()
    cap = cap.cast_as(killranswers_capnp.KillrAnswers)

    # create users

    x = 5
    start = time()
    for i in range(x):
        print "Registering user", i
        cap.registerUser(str(uuid4())).wait()
    total = time() - start
    print "Time: {}, {} per user".format(total, total / x)

    user_id = str(uuid4())
    user = cap.registerUser(user_id)


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
                     category=new_cat.category.id,
                     user=user_id).wait()
    print "api question: ", result

    q = result.question
    # answer the question...
    answer = cap.answer(question=q.id, user=user_id, text="Silence will fall.").wait()
    print answer
