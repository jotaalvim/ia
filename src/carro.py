class Carro:
    def __init__(self,id,cord,vel=0,ac=0):
        self.id=id
        self.x=cord[0]
        self.y=cord[1]
        self.vel=vel
        self.ac=ac
    
    def __str__(self):
        out = "Carro " + str(self.id) + ": \n Posicao : ("+str(self.x)+","+str(self.y)+") \n Velocidade: " + str(self.vel) + "\n Aceleracao: " + str(self.ac) + "\n"
        return out
    
    def getID(self):
        return self.id
    
    def setID(self,id):
        self.id=id
    
    def getCord(self):
        return (self.x,self.y)
    
    def setCord(self, *cord):
        self.x=cord[0]
        self.y=cord[1]
    
    def getVel(self):
        return self.vel
    
    def setVel(self,vel):
        self.vel=vel
    
    def getAc(self):
        return self.ac
    
    def setAc(self,ac):
        self.ac=ac
    
    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
