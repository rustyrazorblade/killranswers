import socket
import capnp
import killranswers_capnp

class KillrAnswersServer(killranswers_capnp.KillrAnswers.Server):
    pass

server = capnp.TwoPartyServer('*:6000', bootstrap=KillrAnswersServer())
server.run_forever()
