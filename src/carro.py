class Carro:
    #FIXME O carro nao precisa de id para nada?
    def __init__(self, id, coord , vel=(0,0), ac=(0,0)):
        self.id  = id
        self.pos = coord
        self.vel = vel
        self.ac  = ac

    def nextPosicao(self):
        #Acelaração = {-1, 0, +1}
        #a = (ax,ay)   ax,ay ∈ Acelaração
        #Posição
        #p = (px,py)
        #Velocidade
        #v = (vx,vy)
        #p = p + v + a
        #v = v + a
        px, py = self.pos
        vx, vy = self.vel
        ax, ay = self.ac
        
        px = px + vx + ax
        py = py + vy + ay

        vx = vx + ax
        vy = vy + ay

        self.pos = px,py
        self.vel = vx,vy
    
    def __str__(self):
        out = 'Carro ' + str(self.id) + ': \n Posicao :' + str(self.pos) + '\n Velocidade:' + str(self.vel) + '\n Aceleracao: ' + str(self.ac) + '\n'
        return out
    
    def getID(self):
        return self.id
    
    def setID(self,id):
        self.id=id
    
    def getCord(self):
        return (self.x,self.y)
    
    def setCord(self, cordn):
        self.pos = cordn
    
    def getVel(self):
        return self.vel
    
    def setVel(self,veln):
        self.vel = veln
    
    def getAc(self):
        return self.ac
    
    def setAc(self,acn):
        self.ac = acn
    
    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
