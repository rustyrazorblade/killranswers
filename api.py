from bottle import Bottle, route, run, post
import uuid

app = Bottle()
def uuid_filter(config):
    regexp = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    return regexp, lambda x: uuid.UUID(x), lambda x: str(x)

app.router.add_filter("uuid", uuid_filter)

@app.post("/questions")
def create_question():
    print "OH JOY"

@app.get("/questions/<question_id:uuid>")
def get_question(question_id):
    print "question %s" % question_id

run(app, host="localhost", port=8099)
