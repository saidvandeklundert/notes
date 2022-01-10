import pickle


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and my age is {self.age}."


someone = Human("Joe", 25)
# pickling the object:
pickle.dump(someone, open("someone.p", "wb"))
the_same_person = pickle.load(open("someone.p", "rb"))
print(type(the_same_person))
print(the_same_person.introduce())

# pickling something as bytes:

someone_as_bytes = pickle.dumps(someone)
someone_from_the_bytes = pickle.loads(someone_as_bytes)
print(someone_from_the_bytes.introduce())
