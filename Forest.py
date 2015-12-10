class Forest():
    def __init__(self):
        self.members = {}

    def getMembers(self):
        return self.members.keys()

    def debug(self):
        for m in self.members:
            print(m)

    def exists(self, person):
        if self.members[person] is not None:
            return True

        return False

    def add(self, person):
        self.members[person.name] = person

    def getParentsOf(self, person):
        p = self.members.get(person, None)
        # Check to see if person exists
        if p is None:
            return None

        if p.parents is not None:
            # Regular Case
            return p.parents
        else:
            # Adam/Eve generation
            return [p.name]
    
    def getSiblingsOf(self, person):
        p = self.members[person]
        # Check to see if person exists
        if p is None:
            return [person]

        if p.parents is not None:
            # Maybe replace with list comprehension for intersection
            parent1   = self.members[p.parents[0]]
            parent2   = self.members[p.parents[1]]
            children1 = set(parent1.children)
            children2 = set(parent2.children)
            
            return list(children1 & children2)
        else:
            # You are your own sibling (A&E)
            return [p.name]


    def getAncestorsOf(self, person):
        p = self.members.get(person, None)
        
        # Check to see if person exists
        if p is None or p.parents is None:
            return [person] # If not they are their own ancestor... I think.

        ancestors = set(p.parents)
        newgen    = p.parents

        while (newgen):
            curr   = self.members[newgen[0]]
            newgen = newgen[1:]

            if curr.parents is not None:
                newgen.append(curr.parents[0])
                newgen.append(curr.parents[1])

            ancestors.add(curr.name)

        return list(ancestors)

    def getRelativesOf(self, person):
        p = self.members.get(person, None)
        
        # Check to see if person exists
        if p is None:
            return None
        else:
            relatives = []
            for person2 in self.members.keys():
                if self.isRelatedTo(person, person2):
                    relatives.append(person2)
            return relatives

    def isRelatedTo(self, person1, person2):
        p1ans = self.getAncestorsOf(person1)
        p2ans = self.getAncestorsOf(person2)
        
        if len(p1ans) <= len(p2ans):
            for i in p1ans:
                if i in p2ans:
                    return True
        else:
            for i in p2ans:
                if i in p1ans:
                    return True
        
        return False
