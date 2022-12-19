import time
import pickle
import os
import copy
import math
import ast
from grafo import Grafo
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

        for car,w in nextestado(pista,e,end):
            g.add_edge(e ,car,w)
            g.add_heuristica(car, distance(car.getPos(),end[0]))#melhorDistance(carro,end))

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
    time.sleep( delta / len(solve) )
    for carros in solve:
        os.system('clear')
        x,y = carros.getPos()
        pista2[y][x] = '•'
        for linha in pista2:
            print("".join(linha))
        time.sleep( delta / len(solve) )

def ppCarros(pista,dicionario,grafo):
    l = "•⊙⊚⊛⊗"
    pista2 = copy.deepcopy(pista)
    dic = copy.deepcopy(dicionario)
    maxi = max([len(dic[k])for k in dic ])
    done = set()
    delta = 4
    os.system('clear')
    for linha in pista2:
        print("".join(linha))
    time.sleep( delta / maxi )
    n  = len(dic)
    while (len(done) != n ):
        time.sleep( delta / maxi )
        os.system('clear')
        for i in range(n):
            if (len(dic[i]) != 0):
                x,y = dic[i].pop(0).getPos()
                pista2[y][x] = l[i]
            else:
                done.add(i)
        for linha in pista2:
            print("".join(linha))
    for i in range(n):
        print("custo", l[i]," = ", grafo.calculaCusto(dicionario[i]))


def intersetaParede(pista,c1,c2):
    c1x,c1y = c1.getPos()
    c2x,c2y = c2.getPos()

    if (pista[c2y][c2x] == "X"):
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

def carros(listaCarros, end, grafo, algoritmo):
    alg = {1: grafo.procuraBFS, 2: grafo.procuraDFS, 3:grafo.greedy, 4: grafo.aEstrela }

    #f = alg[algoritmo]
    f = alg.get(algoritmo)

    solution = []
    #lista de posiçoes usadas
    usadas = []
    done = set()
    #nº carros
    dic = {}
    n = 0
    #inicializar 
    for c in listaCarros:
        solve,w = f(c,end)
        #aux.append((solve,w))
        if solve != []:
            dic[n] = [solve[0]]
            n += 1
    
    n = len(listaCarros)

    while len(done) != n:
        for key in range(n):
            # ultimo carro da solução
            last = dic[key][-1]
            solve,w = grafo.aEstrela(last, end)

            usadas = [dic[car][-1].getPos() for car in range(key)]

            if (len(solve) == 1):
                done.add(key)
                dic[key].append(solve[0])
            elif (solve[1].getPos() in end ): #cheguei ao fim
                done.add(key)
                dic[key].append(solve[1])
            else:
                ncarro = copy.deepcopy(solve[1])
                pos = ncarro.getPos()

                if (pos in usadas):
                    ncarro.setPos( solve[0].getPos() )
                    ncarro.setVel((0,0))
                dic[key].append(ncarro)
    return dic

# LISTA que cada carro vai percorrer 
    return solution

def pedePos():
    inputUtilizador = input('Insere as coordenadas onde queres que começe o carro: ')
    tokens = inputUtilizador.split(",")
    for token in tokens:
        token = token.strip()

    # print(f"Tokens: {tokens}")
    return tuple(map(int, tokens))

def insertInitPos (pista, n):
    number_of_cars = n
    while number_of_cars != 0:
        posDesejada = pedePos()
        # pos1 = getCharPosition(pista, posDesejada)
        # x = getChar(pista, posDesejada)
        # x = x.replace(char, "P")
        pista[posDesejada[1]][posDesejada[0]] = "P"
        number_of_cars -= 1
    return pista

def teste():
    path = f"../pistas/pista2.txt"
    p = pista(path)
    print(p)
    n = 2
    insertInitPos(p, n)
    print(p)

np = 3
path  = f"../pistas/pista{np}.txt"
p     = pista(path)
start = charPosition(p,"P")
end   = charPosition(p,"F")
c     = Carro(start[0])
c2    = Carro((1,1))
c3    = Carro((4,1))
c4    = Carro((2,2))
c5    = Carro((3,3))
#c2    = Carro((10,1))
#c3    = Carro((18,1))
#c2    = Carro((36,43))
#c3    = Carro((34,34))

pathFile = f"grafo{np}.pkl"
if os.path.exists(pathFile):
    with open(pathFile, "rb") as file:
        print("loading data from "+pathFile)
        g = pickle.load(file)
        print("done")
else:
    g = geraGrafo(p,c,end)
    with open(pathFile, "wb") as f:
        print("dumping data to "+pathFile)
        pickle.dump(g, f)
        print("done")
lista = [c,c2,c3]
#lista = [c]

#ç     = carros(lista,end,g,4)

#ppCarros(p,ç,g)

