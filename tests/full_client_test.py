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


    # get root category
    root = cap.getRootCategory().wait()
    cat = root.category.id
    print 'root cat: ', cat

    cap.createCategory(text="api provided name", parent="test")

    # create a category


    result = cap.ask(text="test")
    print result.wait()
