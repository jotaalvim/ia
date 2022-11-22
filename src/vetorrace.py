#sair da pista -> custo 25
#    • v = (0,0)
#movimento -> custo 1

from grafo import Grafo
from node import Node
from queue import Queue
from carro import Carro


#devolve uma lista de listas
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
    return pista



# devolde as posições de um carater na pista
def getPosition(pista,char):
    pos = []
    for y in range(len(pista)):
        for x in range(len(pista[0])):
            if pista[y][x] == char:
                pos.append((x,y))
    return pos


#gera o fim, o carro em cima da meta
def geraEstadoFinal(pista):
    pos = getPosition (pista,"F")
    xi,yi = getPosition (pista,"P")[0]
    pista[yi][xi] = "-"
    l = []
    for x,y in pos:
        pista[y][x] = "P"
        l.append(pista)
        pista[y][x] = "-"
    return l


#todas as acelarações possíveis
def acel():
    return [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

#FIXME INUTIL
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

def getChar(pista, coord):
    x,y = coord
    return pista[y][x]

#def pista2tuple(pista):
#    for i in range(len(pista)):
#        pista[i] = tuple(pista[i])
#    return (tuple(pista))
#
#def tuple2pista(pista):
#    pista = list(pista)
#    for i in range(len(pista)):
#        pista[i] = list(pista[i])
#    return pista

#[[Char]]-> [[Char]]
def geraEstados(pista):
    #só há uma posição de início
    l = getPosition(pista,'P')
    if (l == []):
        return []
    x,y = l[0]
     
    v = vizinhos(pista,(x,y))

    pista[y][x] = '-'

    l = []
    for xs,ys in v:
        k = p[ys][xs]
        if k != 'X' and k != 'F':
            pista[ys][xs] = 'P'
            l.append(pista)
            pista[ys][xs] = '-'

    return l


def geraGrafo(pista):
    # grafo é direcionado
    g = Grafo(True)
    i = pista
    v = set() #visited
    q = Queue()

    q.put(i)
    while not q.empty():
        #estado
        e = q.get()
        #te = pista2tuple(e)
        #e = tuple2pista(te)
        print(geraEstados(e))
        #for estado in geraEstados(tuple2pista(e)):
        for estado in geraEstados(e):
            #t = pista2tuple(estado)
            #g.add_edge(te ,t) 
            g.add_edge(e ,estado) 

            if (e not in v ):
                q.put(estado)
        v.add(e)
    return g

p = pista("../pistas/pista.txt")
c = Carro(0, getPosition (pista,"P")[0])
n = Node(c,p,0)

end = geraEstadoFinal(p)

g = geraGrafo(p)

print("BFS")
print(g.procuraBFS(p,end))

print("DFS")
print(g.procuraDFS(p,end))

