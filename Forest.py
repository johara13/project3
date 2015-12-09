class Forest():
    def __init__(self):
        self.members = {}

    def debug(self):
        pass
        #print(self.members)

    def add(self, person):
        self.members[person.name] = person

    def getMembers(self):
        return self.members.keys()