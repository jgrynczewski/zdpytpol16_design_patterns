# DIP - Dependency Inversion Principle (Zasada odwrócenia zależności)
# D w SOLID
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )


# Łamiemy zasadę DIP
class Research:
    def find_all_children_of(self, relationships, name):
        relations = relationships.relations
        for r in relations:
            if r[0].name==name and r[1]==Relationship.PARENT:
                print(F"{name} has a child called {r[2].name}")


parent = Person("John")
parent2 = Person("Peter")
child1 = Person("Chris")
child2 = Person("Matt")
child3 = Person("Helen")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)
relationships.add_parent_and_child(parent2, child3)

# research = Research()
# research.find_all_children_of(relationships, "John")

import abc

class AbstractNewRelationhips(abc.ABC):

    @abc.abstractmethod
    def find_all_children_of(self, name):
        pass

class NewRelationships(AbstractNewRelationhips):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    def __init__(self, browser: AbstractNewRelationhips, name):
        for item in browser.find_all_children_of(name):
            print(f"{name} has a child called {item}")


relationships = NewRelationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)
relationships.add_parent_and_child(parent2, child3)

Research(relationships, "John")