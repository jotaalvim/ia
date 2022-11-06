#Acelaração = {-1, 0, +1}
#a = (ax,ay)   ax,ay ∈ Acelaração
#
#Posição
#p = (px,py)
#
#Velocidade
#v = (vx,vy)
#
#
#p = p + v + a
#v = v + a
#
#
#sair da pista -> custo 25
#    • v = (0,0)
#
#movimento -> custo 1
#
#parser de ficheiro -> pista
from grafo import Grafo
from grafo import Node



# type Pista = [[Char]]
def pista(path:str):
    pista = []
    f = open(path, "r")
    conteudo = f.read()
    #conteudo.split('\n')
    conteudo = conteudo.splitlines()
    
    for linha in conteudo:
        aux = []
        aux[:0] = linha
        pista.append(aux)
    #ys = len(pista)
    #xs = len(pista[0])
    return pista


# devolde as posições de um carater na pista
def getPosition(pista,char):
    pos = []
    for y in range(len(pista)):
        for x in range(len(pista[0])):
            if pista[y][x] == char:
                pos.append((x,y))
    return pos
