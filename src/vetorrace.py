import time
import os
import copy
import math
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
def charPosition(pista,char):
    pos = []
    largura = len(pista[0])
    altura  = len(pista)

    for x in range(largura):
        for y in range(altura):
            if pista[y][x] == char:
                pos.append((x,y))
    return pos

#todas as acelarações possíveis
def acel():
    return [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

#próximas posiçoes possiveis para um carro! 
#devolve uma lista de novos carros
def nextestado(pista,carro,end):
    l = []

    posi = carro.pos
    veli = carro.vel

    largura = len(pista[0]) -1
    altura  = len(pista) -1

    #end variavel global
    if (posi in end):
        l.append((carro,1))

    for acele in acel():
        novoCarro = Carro(posi,veli)
        novoCarro.nextPosicao(acele)

        x,y = novoCarro.pos
        
        if not (x < 0 or x > largura or y < 0 or y > altura):
            #f = temParede(carro,novoCarro)
            f = intersetaParede(pista,carro,novoCarro)

            if f == False: # or (getChar(pista,(x,y)) == 'X'):
                novoCarro.setPos(posi)
                novoCarro.setVel((0,0))
                if not ((novoCarro,25) in l):
                    l.append((novoCarro,25))
            else:
                l.append((novoCarro,1))
    return l

def getChar(pista, coord):
    x,y = coord
    return pista[y][x]

def geraGrafo(pista,carro,end):
    # grafo é direcionado
    g = Grafo(True)
    v = set() #visited
    q = Queue()
    q.put(carro)

    while not q.empty():
        #estado
        e = q.get()
        le = nextestado(pista,e,end)

        for car,w in le:
            g.add_edge(e ,car,w) 
            g.add_heuristica(car, melhorDistance(carro,end)) 

            if (car not in v):
                q.put(car)
        v.add(e)

    return g


def endcarro(end):
    l = []
    for pos in end:
        novoCarro = Carro(pos)
        l.append(novoCarro)
    return l

def pp(pista,solve):
    pista2 = copy.deepcopy(pista)
    
    # Δ tempo 
    delta = 2

    os.system('clear')

    for linha in pista2:
        print("".join(linha))

    for carros in solve:
        os.system('clear')
        x,y = carros.getPos()
        pista2[y][x] = '•'
        for linha in pista2:
            print("".join(linha))
        time.sleep( delta / len(solve) )


def intersetaParede(pista,c1,c2):
    c1x,c1y = c1.getPos()    
    c2x,c2y = c2.getPos()    

    if (pista[c2y] [c2x] == "X"):
        return False

    if (c1x > c2x):
        aux = Carro((c1x,c1y))
        c1 = c2
        c2 = aux

    c1x,c1y = c1.getPos()    
    c11x,c11y = c1.getPos()    
    c2x,c2y = c2.getPos()    
    c22x,c22y = c2.getPos()    
    
    ts = [(c1x,c1y)]
    ti = [(c2x,c2y)]
    #ts = []
    #ti = []

    if (c1x <= c2x):
        if (c2y >= c1y):
            while c1x != c2x:
                c1x += 1
                ts.append((c1x,c1y))
            while c1y != c2y:
                c1y += 1
                ts.append((c1x,c1y))
            while c11y != c22y:
                c11y += 1
                ti.append((c11x,c11y))
            while c11x != c22x:
                c11x += 1
                ti.append((c11x,c11y))
        else:
            while c1x != c2x:
                c1x += 1
                ti.append((c1x,c1y))
            while c1y != c2y:
                c1y -= 1
                ti.append((c1x,c1y))
            while c11y != c22y:
                c11y -= 1
                ts.append((c11x,c11y))
            while c11x != c22x:
                c11x += 1
                ts.append((c11x,c11y))

    f  = False
    f2 = False
    for x,y in ts:
        if (pista[y][x] == 'X'):
            f = True
            break
        
    for x,y in ti:
        if (pista[y][x] == 'X'):
            f2 = True
            break

    # posso passar?
    return (not f) or (not f2)

#
#def corre (path):
#    p = pista(path)
#    start = charPosition (p,"P") [0]
#    c = Carro(start)
#    end = charPosition (p,"F")
#    print("Gerando grafo")
#    g = geraGrafo(p,c,end)
#    print("Grafo gerado")
#    print(
#"""
#Escolhe um algoritmo de procura
#1 - BFS
#2 - DFS
#""")
#    x = int(input())
#    if x == 1:
#        print("BFS")
#        solve,w = g.procuraBFS(c,end)
#    if x == 2:
#        print("DFS")
#        solve,w = g.procuraDFS(c,end)
#        #[print(str(u)) for u in solve]
#    pp(p,solve)
#    print("custo =",w)


def distance (pos1,pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    return math.sqrt( math.pow(x1-x2,2) + math.pow(y1-y2,2))

def melhorDistance (carro, end):
    pos = carro.getPos()
    # m = menor dist até ao momento
    m = 0
    for pos2 in end:
        k = distance(pos,pos2)
        if m > k:
            m = k
    return m


"""
ter N carros na corrida
    ⚠ lidar com as colisões
    
    algoritmo para gerar o caminho para os n carros
        • gerar o grafo normalmente
        1. Calcular o caminho do primeiro carro
            gardar o nº da iteração
            casa de cada carro
        2. Para o carro seguinte
"""

def carros(listaCarros, end, grafo, algoritmo):
    solution = []
    #lista de posiçoes usadas
    usadas = []
    #guarda soluções temporárias
    aux = []
    # nº carros
    n = len(listaCarros)

    for c in listaCarros:
        solve,w = grafo.procuraBFS(c,end)
        aux.append((solve,w))

    for sol,w in aux:
        solution.append(sol[0])

    usadas = [carro.getPos() for carro in solution]
    # devia guardar com um identificador 

    for carro in solution:
        pos = carro.getPos()
        if (usadas.count(pos) > 1):
            #colidir
        else:
            #passo ao próximo carro



# LISTA que cada carro vai percorrer 
    return solution
