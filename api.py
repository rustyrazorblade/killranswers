import os
import socket
import capnp
import killranswers_capnp
from killranswers import User, Category, Question

class KillrAnswersServer(killranswers_capnp.KillrAnswers.Server):
    def ask(self, text, category, user, **kwargs):
        print "incoming"
        print str(text)
        q = killranswers_capnp.Question.new_message(id="test",
                                        text="blah")
        return q

    def createCategory(self, text, parent, **kwargs):
        p = Category.get(category_id=parent)
        cat = p.create_sub(text)
        c = killranswers_capnp.Category.new_message()
        c.id = str(cat.category_id  )
        c.name = cat.name
        return c

    def getRootCategory(self, **kwargs):
        root = Category.get_root()
        cat = killranswers_capnp.Category.new_message()
        cat.id = str(root.category_id)
        cat.name = root.name
        return cat

    def registerUser(self, user_id, **kwargs):
        User.create(user_id)



def get_server():
    server = capnp.TwoPartyServer('*:6000', bootstrap=KillrAnswersServer())
    return server

if __name__ == "__main__":
    from killranswers.connections import cassandra
    cassandra()
    server = get_server()
    print "Starting server.  To kill:\n\nkill %d" % os.getpid()
    server.run_forever()
