class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


bob = Person("Bob", 35)
print(bob)  

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old"


bob = Person("Bob", 35)
print(bob) 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return (
            f"<Person({self.name!r}, {self.age})>"
        )  

bob = Person("Bob", 35)
print(bob) 