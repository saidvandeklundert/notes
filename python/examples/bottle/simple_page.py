#!/usr/bin/python
from bottle import route, run


@route("/message")
def hello():
    return "So minimal this bottle is"


run(host="127.0.0.1", port=8080, debug=True)

# now you can open http://127.0.0.1:8080/message and see the message
