from bottle import Bottle, route, run, post

app = Bottle()

@app.post("/questions")
def create_question():
    print "OH JOY"

run(app, host="localhost", port=8099)
