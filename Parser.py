import sys
import Forest
import Person

def listoverlap(a, b):   # function to find if two lists share any elements
    s = set(b)
    return any(n in s for n in a)

class Parser(object):
    def __init__(self, forest):
        self.forest = forest

    def r(self, name1, name2):
    # Finds the closest relation of 2 people
        if name1 in self.w('spouse', name2):
            return 'Spouse'
        elif name1 in self.w('parent', name2) or name2 in self.w('parent', name1):
            return 'Parent'
        elif name1 in self.w('sibling', name2):
            return 'Sibling'
        elif name1 in self.w('ancestor', name2) or name2 in self.w('ancestor', name1):
            return 'Ancestor'
        elif name1 in self.w('relative', name2) or name2 in self.w('relative', name1):
            return 'Relative'
        elif name1 in self.w('unrelated', name2):
            return 'Unrelated'
        else:
            return 'Cousins'

    def x(self, name1, r, name2):
    # Finds if name1 is r relation to name2
        ll=self.w(r,name2)
        if name1 in ll:
            return True
        else:
            return False

    def w(self, rel, name1):
    # Prints a list of all people relation (rel) related to name1
        if rel == 'spouse':
            return self.forest.members[name1].spouse

        elif rel == 'parent':
            return self.forest.members[name1].parents

        elif rel == 'sibling':
            if self.forest.members[name1].parents[0] is not None:
                p1 = self.forest.members[self.forest.members[name1].parents[0]]
                p2 = self.forest.members[self.forest.members[name1].parents[1]]
                c1 = p1.children
                c2 = p2.children
                return list(set(c1) & set(c2))
                # from what I found this is the best way to find the intersection
                # of two lists, but there is probably other ways
        elif rel == 'ancestor':
            ancestors = self.forest.members[name1].parents
            for p in ancestors:    # this should work to find the list of ancestors but I haven't been able to test it
                if self.forest.members[p].parents[0] is not None:
                    ancestors.extend(self.forest.members[p].parents)
            return ancestors

        elif rel == 'relative':
            ancestors = self.w('ancestor', name1)
            relatives = []

            for a in ancestors:
                relatives.extend(self.w('siblings', a))
                
            return relatives

        elif rel == 'cousins': # (TODO) Implement
            print('cousins')

        elif rel == 'unrelated': # probably needs improvement
            ancestors = self.w('ancestor', name1)
            everyone  = self.forest.debug()
            unrelated = []

            for p in everyone:
                pa = self.w('ancestors', p)
                if not listoverlap(ancestors, pa):
                    unrelated.append(p)
            return unrelated

    def e(self, name1, name2, child=None):
        print('E', name1, name2, child)

        # creates parent 1 if they do not exist yet
        if name1 not in self.forest.members: 
            p = Person.Person(name1)
            self.forest.add(p)

        # creates parent 2 if they do not exist
        if name2 not in self.forest.members: 
            p = Person.Person(name2)
            self.forest.add(p)

        self.forest.members[name1].setSpouse(name2)
        self.forest.members[name2].setSpouse(name1)

        if child != None:
            p = Person.Person(child,name1,name2)
            self.forest.add(p)
            self.forest.members[name1].setChildren(name1)
            self.forest.members[name2].setChildren(name2)

        self.forest.debug()

f = Forest.Forest()
p = Parser(f)

for line in sys.stdin:
    newline = line.split()

    if newline[0] == 'E' and len(newline) >= 4:
        p.e(newline[1], newline[2], newline[3])
    elif newline[0] == 'E' and len(newline) < 4:
        p.e(newline[1], newline[2])
    elif newline[0] == 'R':
        p.r(newline[1], newline[2])
    elif newline[0] == 'X':
        p.x(newline[1], newline[2],newline[3])
    elif newline[0] == 'W':
        p.w(newline[1], newline[2])
        