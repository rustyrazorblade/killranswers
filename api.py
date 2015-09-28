import os
import socket
import capnp
import killranswers_capnp as api
from killranswers import User, Category, Question

class KillrAnswersServer(api.KillrAnswers.Server):
    def ask(self, text, category, user, **kwargs):
        print "incoming"
        print str(text)
        cat = Category.get(category)
        u = User.get(user)
        question = Question.create(cat, text, u)

        q = api.Question.new_message(id=str(question.question_id),
                                     text=question.text,
                                     category=str(cat.category_id))
        return q

    def createCategory(self, text, parent, **kwargs):
        p = Category.get(category_id=parent)
        cat = p.create_sub(text)
        c = api.Category.new_message()
        c.id = str(cat.category_id)
        c.name = cat.name
        return c

    def getRootCategory(self, **kwargs):
        root = Category.get_root()
        cat = api.Category.new_message()
        cat.id = str(root.category_id)
        cat.name = root.name
        return cat

    def registerUser(self, user_id, **kwargs):
        User.create(user_id)

    def getChildCategories(self, parent, **kwargs):
        cat = Category.get(parent)
        children = cat.get_children()

        response = api.CategoryList.new_message()
        cats = response.init("categories", len(children))
        i = 0
        for x in children:
            cats[i].id = str(x.category_id)
            cats[i].name = x.child_category_name
            i += 1
        return response




def get_server():
    server = capnp.TwoPartyServer('*:6000', bootstrap=KillrAnswersServer())
    return server

if __name__ == "__main__":
    from killranswers.connections import cassandra
    cassandra()
    server = get_server()
    print "Starting server.  To kill:\n\nkill %d" % os.getpid()
    server.run_forever()
