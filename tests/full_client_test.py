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
    cat_id = root.categoryId
    # cat = cap.createCategory(name="test", parent=root.categoryId).wait()

    # print "new category: ",
    # print cat

    # create a category


    result = cap.ask(text="test")
    print result.wait()
