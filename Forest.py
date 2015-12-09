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
        p = self.members[person]
        # Check to see if person exists
        if p is None:
            return None

        if p.parents is not None:
            # Regular Case
            return p.parents
        else:
            # Adam/Eve generation
            return p
    
    def getSiblingsOf(self, person):
        p = self.members[person]
        # Check to see if person exists
        if p is None:
            return None

        if p.parents is not None:
            # Maybe replace with list comprehension for intersection
            parent1 = self.members[p.parents[0]]
            parent2 = self.members[p.parents[1]]
            children1 = set([parent1.children])
            children2 = set([parent2.children])

            return list(children1 & children2)
        else:
            # You are your own sibling (A&E)
            return [p.name]


    def getAncestorsOf(self, person):
        curr, p = self.members[person], self.members[person]
        ancestors = set([])
        # Check to see if person exists
        if p is None:
            return None