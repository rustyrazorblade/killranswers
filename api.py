import socket
import capnp
import killranswers_capnp

class KillrAnswersServer(killranswers_capnp.KillrAnswers.Server):
    def ask(self, text, **kwargs):
        print "incoming"
        print str(text)
        return str(text)

def get_server():
    server = capnp.TwoPartyServer('*:6000', bootstrap=KillrAnswersServer())
    return server

if __name__ == "__main__":
    server = get_server()
    print "Starting server"
    server.run_forever()
