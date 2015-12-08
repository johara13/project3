import sys
import Forest
import Person
# (TODO) Create class for parser (instantiated with Forest Object)

class Parser(object):
    def __init__(self, forest):
        self.forest = forest

    def r(self, name1, name2):
    # Finds the closest relation of 2 people
        print('R')

    def x(self, name1, r, name2):
    # Finds if 2 people are related with r relation
        print('X')

    def w(self, rel, name1):
    # Prints a list of all people relation (rel) related to name1
        print('W')

    def e(self, name1, name2, child=None):
        print('E', name1, name2, child)

        if name1 not in self.forest.members: #creates parent 1 if they do not exist yet
            p=Person.Person(name1)
            self.forest.add(p)

        if name2 not in self.forest.members: #creates parent 2 if they do not exist
            p=Person.Person(name2)
            self.forest.add(p)

        self.forest.members[name1].setSpouse(name2)
        self.forest.members[name2].setSpouse(name1)

        if child!=None:
            p=Person.Person(child,name1,name2)
            self.forest.add(p)
            self.forest.members[name1].setChildren(name1)
            self.forest.members[name2].setChildren(name2)

        self.forest.debug()
f=Forest.Forest()
p=Parser(f)

for line in sys.stdin:
    newline = line.split()

    if newline[0]   == 'E' and len(newline) >= 4:
        p.e(newline[1], newline[2], newline[3])
    elif newline[0]   == 'E' and len(newline) < 4:
        p.e(newline[1], newline[2])
    elif newline[0] == 'R':
        print('R')
    elif newline[0] == 'X':
        print('X')
    elif newline[0] == 'W':
        print('W')