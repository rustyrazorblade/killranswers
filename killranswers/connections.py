from cassandra.cqlengine.connection import setup

def cassandra():
    # TODO move to use configuration
    setup(["localhost"], "killranswers")

def kafka():
    pass
