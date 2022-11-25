class Node:
    def __init__(self,carro,id=-1):
        self.id = id
        self.carro = carro

    def __str__(self):
        return str(self.carro)

    def __hash__(self):
        return hash(self.carro)

    def __eq__(self,other):
        return (self.carro == other.carro)

    def getId(self):
        return self.id

    def setId(self,id):
        self.id = id
