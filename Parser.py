import sys
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
