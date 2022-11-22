class Node:
    def __init__(self,carro,mapa,id=-1):
        self.id = id
        self.carro = carro
        self.mapa = None

    def __str__(self):
        #FIXME pode ter o mapa também
        return str(self.carro)

    def __hash__(self):
        return hash(str(self.id))

    def __eq__(self,other):
        #FIXME comparar carro e o mapa?
        return (self.id == other.id)

    def getId(self):
        return self.id

    def getCarro(self):
        return self.carro
    
    def getMapa(self):
        return self.mapa

    def setMapa(self,m):
        self.mapa = m

    def setId(self,id):
        self.id = id
