class Carro:
    def __init__(self, coord = (0,0) , vel = (0,0)):
        self.pos = coord
        self.vel = vel

    def nextPosicao(self,ac):
        #ac = (ax,ay),  ax,ay ∈ {-1, 0, +1}
        px, py = self.pos
        vx, vy = self.vel
        ax, ay = ac
        
        px = px + vx + ax
        py = py + vy + ay

        vx = vx + ax
        vy = vy + ay

        self.pos = px,py
        self.vel = vx,vy
    
    def __str__(self):
        out = 'Carro : \n Posicao :' + str(self.pos) + '\n Velocidade:' + str(self.vel)
        return out
    
    def getPos(self):
        return (self.pos)
    
    def setPos(self, npos):
        self.pos = npos
    
    def getVel(self):
        return self.vel
    
    def setVel(self,veln):
        self.vel = veln
    
    def __eq__(self, other):
        if other == None:
            return False 
        else:
            return self.pos == other.pos and self.vel == other.vel

    def __hash__(self):
        return hash(self.pos + self. vel)
