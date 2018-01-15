# 命名的元组
import collections

Person = collections.namedtuple("Person", "name age gender")
print(type(Person))
Bob = Person(name="Bob", age="23", gender="male")
print(Bob)
Jane = Person(name="Jane", age="28", gender="female")
print(Jane)
for people in [Bob, Jane]:
    print(people.name, people.age, people.gender)
