class Node:
    def __init__(self,carro,id=-1):
        self.id = id
        self.carro = carro

    def __str__(self):
        return str(self.carro)

    def __hash__(self):
        return hash(str(self.id))

    def __eq__(self,other):
        return (self.id == other.id)

    def getId(self):
        return self.id

    def getMapa(self):
        return self.mapa

    def setMapa(self,m):
        self.mapa = m

    def setId(self,id):
        self.id = id
