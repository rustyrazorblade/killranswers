import socket
import capnp
import killranswers_capnp

class KillrAnswersServer(killranswers_capnp.KillrAnswers.Server):
    pass

def get_server():
    server = capnp.TwoPartyServer('*:6000', bootstrap=KillrAnswersServer())
    return server

if __name__ == "__main__":
    server = get_server()
    server.run_forever()
