from mylib import serializer

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("John doe", 37)


serializer.save_json(p, "person.json")
p2 = serializer.load_json("person.json", cls=Person)

serializer.save_binary(p, "person.bin")
p3 = serializer.load_binary("person.bin")