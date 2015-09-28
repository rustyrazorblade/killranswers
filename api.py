import os
import socket
import capnp
import killranswers_capnp
from killranswers.categories import Category

class KillrAnswersServer(killranswers_capnp.KillrAnswers.Server):
    def ask(self, text, **kwargs):
        print "incoming"
        print str(text)
        q = killranswers_capnp.Question.new_message(id="test",
                                        text="blah")
        return q

    def createCategory(self, text, parent, **kwargs):
        cat = killranswers_capnp.Category.new_message()
        cat.id = "test"
        cat.name = "test"
        return cat

    def getRootCategory(self, **kwargs):
        root = Category.get_root()
        cat = killranswers_capnp.Category.new_message()
        cat.id = str(root.category_id)
        cat.name = root.name
        return cat


def get_server():
    server = capnp.TwoPartyServer('*:6000', bootstrap=KillrAnswersServer())
    return server

if __name__ == "__main__":
    from killranswers.connections import cassandra
    cassandra()
    server = get_server()
    print "Starting server.  To kill:\n\nkill %d" % os.getpid()
    server.run_forever()
