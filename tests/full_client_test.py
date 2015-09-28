import sys
sys.path.append("")

import capnp
import killranswers_capnp
import socket

if __name__  == "__main__":
    client = capnp.TwoPartyClient("localhost:6000")
    cap = client.bootstrap()
    cap = cap.cast_as(killranswers_capnp.KillrAnswers)

    # get root category
    root = cap.getRootCategory().wait()
    cat = root.category.id
    print 'root cat: ', cat

    cap.createCategory(text="api provided name", parent="test")

    # create a category


    result = cap.ask(text="test")
    print result.wait()
