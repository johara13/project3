class Person:
    def __init__(self, name, par1=None, par2=None):
        self.name     = name
        self.children = []
        self.spouse   = []

        if par1 == None:
            self.parents = None
        else:
            self.parents = [par1, par2]

    def setChildren(self, child):
        self.children.append(child)

    def setSpouse(self, spouse):
        self.spouse.append(spouse)