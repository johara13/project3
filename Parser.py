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
        p1 = self.forest.exists(name1)
        p2 = self.forest.exists(name2) 
        
        if not p1 or not p2:
            # One Case: R FakePerson FakePerson ?
            return 'Unrelated'


        if name1 in self.w('spouse', name2):
            return 'Spouse'

        elif name1 in self.w('parent', name2):
            return 'Parent'

        elif name1 in self.w('sibling', name2):
            return 'Sibling'

        elif name1 in self.w('ancestor', name2):
            return 'Ancestor'

        elif name1 in self.w('relative', name2):
            return 'Relative'

        elif name1 in self.w('unrelated', name2):
            return 'Unrelated'

        else:
            return 'Cousins'

    def x(self, name1, r, name2):
        # Finds if name1 is r relation to name2
        p1 = self.forest.members.get(name1, None)
        p2 = self.forest.members.get(name2, None)
        ll = self.w(r, name2)

        if (not p1 or not p2) and (r == 'unrelated'):
            return True

        elif ll is None:
            return False

        else:
            if name1 in ll:
                return True
            else:
                return False

    def w(self, rel, name1):
        # Prints a list of all people relation (rel) related to name1
        p = self.forest.members.get(name1, None)

        if rel == 'spouse':
            return self.forest.getSpousesOf(name1)
            
        elif rel == 'parent':
            return self.forest.getParentsOf(name1)

        elif rel == 'sibling':
            if p and p.parents is not None:
                # Person and parents exist
                return self.forest.getSiblingsOf(name1)
            else:
                # Adam & Eve or unrelated person
                return [name1]
                
        elif rel == 'ancestor':
            return self.forest.getAncestorsOf(name1)

        elif rel == 'relative':
            return self.forest.getRelativesOf(name1)

        elif rel[0] == 'cousin': # (TODO) Implement
            return self.forest.getCousinsOf(name1, rel[1], rel[2])

        elif rel == 'unrelated': # probably needs improvement
            return self.forest.getUnrelatedOf(name1)

    def e(self, name1, name2, child=None):
        # creates parent 1 if they do not exist yet
        if name1 not in self.forest.members: 
            p = Person.Person(name1)
            self.forest.add(p)

        # creates parent 2 if they do not exist
        if name2 not in self.forest.members: 
            p = Person.Person(name2)
            self.forest.add(p)

        par1, par2 = self.forest.members[name1], self.forest.members[name2]
        
        if par1.name not in par2.spouse:
            par1.setSpouse(name2)
            par2.setSpouse(name1)        
        
        if child is not None:
            c = Person.Person(child, name1, name2)
            self.forest.add(c)
            par1.setChildren(child)
            par2.setChildren(child)
