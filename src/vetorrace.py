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
    f.close()
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
#def geraEstadoFinal(pista):
#    pos = getPosition (pista,"F")
#    xi,yi = getPosition (pista,"P")[0]
#    pista[yi][xi] = "-"
#    l = []
#    for x,y in pos:
#        pista[y][x] = "P"
#        l.append(pista)
#        pista[y][x] = "-"
#    return l


#todas as acelarações possíveis
def acel():
    return [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

#próximas posiçoes possiveis para um carro! 
#devolve uma lista de novos carros
def nextestado(pista,carro):
    l = []

    posi = carro.pos
    veli = carro.vel

    largura = len(pista[0]) 
    altura  = len(pista)

    for acele in acel():
        novoCarro = Carro(posi,veli)
        novoCarro.nextPosicao(acele)

        x,y = novoCarro.pos
        
        if not (x < 0 or y < 0 or x > largura or y > altura):
            print(x,y)
            if (pista [y][x] == 'X'):
                novoCarro.setPos(posi)
                novoCarro.setVel((0,0))
                if not (novoCarro in l):
                    l.append(novoCarro)
            else:
                l.append(novoCarro)

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

#def geraEstados(pista):
#    #só há uma posição de início
#    l = getPosition(pista,'P')
#    if (l == []):
#        return []
#    x,y = l[0]
#     
#    v = vizinhos(pista,(x,y))
#
#    pista[y][x] = '-'
#
#    l = []
#    for xs,ys in v:
#        k = p[ys][xs]
#        if k != 'X' and k != 'F':
#            pista[ys][xs] = 'P'
#            l.append(pista)
#            pista[ys][xs] = '-'
#
#    return l


def geraGrafo(pista,carro):
    # grafo é direcionado
    g = Grafo(True)
    i = carro
    v = set() #visited
    q = Queue()

    q.put(i)

    while not q.empty():
        #estado
        e = q.get()

        for car in nextestados(pista,e):
            g.add_edge(e ,car) 

            if (car not in v ):
                q.put(car)
        v.add(e)
    return g

p = pista("../pistas/pista.txt")
c = Carro(getPosition(p,"P")[0])

g = geraGrafo(p,c)

end = getPosition (pista,"F")

#print("BFS")
#print(g.procuraBFS(p,end))
#
#print("DFS")
#print(g.procuraDFS(p,end))
#
