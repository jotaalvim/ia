class Node:
    def __init__(self,name,id=-1):
        self.id = id
        self.name = name

    def __str__(self):
        return str(self.name)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self,other):
        return (self.name == other.name)

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setIf(self,id):
        self.id = id
