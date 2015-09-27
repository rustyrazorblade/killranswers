import sys
sys.path.append("")

import capnp
import killranswers_capnp
import socket

client = capnp.TwoPartyClient("localhost:6000")
cap = client.bootstrap()
cap = cap.cast_as(killranswers_capnp.KillrAnswers)

results = []
def add_result(x, n):
    results.append(x)
    n()
    
result = cap.ask(text="test")
result = result.then(lambda x: cap.ask(text="who"))
print result.wait()
