#!/usr/bin/python

from bottle import route, run
from pydantic import BaseModel


class Human(BaseModel):
    name: str
    age: int


@route("/human")
def display_human():

    jan = Human(name="jan", age=7)

    return jan.dict()


run(host="localhost", port=8080, debug=True)
