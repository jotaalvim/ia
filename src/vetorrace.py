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
from queue import Queue

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


def vizinhos(pista,coord):
    x,y = coord
    
    (x2,y2) = x+1,y
    (x3,y3) = x  ,y+1
    (x4,y4) = x+1,y+1
    (x5,y5) = x-1,y
    (x6,y6) = x  ,y-1
    (x7,y7) = x-1,y-1
    (x8,y8) = x-1,y+1
    (x9,y9) = x+1,y-1

    l = []
    for xs,ys in [ 
            (x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6),(x7,y7),(x8,y8),(x9,y9)]:
        if xs < 0 or ys < 0 or xs > len(pista[0]) or ys > len(pista):
            a = 2
        else:
            l.append((xs,ys))
    return l


#por faver ainda
#def geraGrafo(pista):
    # grafo é direcionado
    #g = Grafo(True)
    #i = pista
    #v = set() #visited
    #q = Queue()

    #q.put(i)
    #while not q.empty():
    #    #estado
    #    e = q.get()
    #    for estado in geraEstados(e):
    #        g.add_edge(e, estado)

    #        if (estado not in v ):
    #            q.put(estado)
    #    v.add(e)

    #return g
