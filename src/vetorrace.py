import time
import pickle
import os
import copy
import math
import ast
from grafo import Grafo
from queue import Queue
from carro import Carro
import shutil

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

    a = acel()
    for acele in a:
        novoCarro = Carro(posi,veli)
        novoCarro.nextPosicao(acele)

        x,y = novoCarro.pos

        if not (x < 0 or x > largura or y < 0 or y > altura):
            f = intersetaParede(pista,carro,novoCarro)

            if f:
                l.append((novoCarro,1))
            else:
                novoCarro.setPos(posi)
                novoCarro.setVel((0,0))
                if not ((novoCarro,25) in l):
                    l.append((novoCarro,25))
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

def printp(pista):
    pista2 = copy.deepcopy(pista)
    for linha in pista2:
        print("".join(linha))
    x = input()

def pp(pista,solve):
    pista2 = copy.deepcopy(pista)
    # Δ tempo
    delta = 4
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
    l = "•⊙⊚⊛⊗⊕⊖⊜⌀⌕⌽⍟"
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
        print("custo", l[i]," = ", grafo.calculaCusto(list(set(dicionario[i]))))
    x = input()

def intersetaParede(pista,c1,c2):
    c1x,c1y = c1.getPos()
    c2x,c2y = c2.getPos()

    if (pista[c2y][c2x] == "X"):
        return False
    ts = []
    ti = []

    if (c1x >= c2x):
        ix = c2x
        fx = c1x
    else:
        ix = c1x
        fx = c2x
    if (c1y >= c2y):
        iy = c2y
        fy = c1y
    else:
        iy = c1y
        fy = c2y

    ts.extend([(xx,iy) for xx in range(ix,fx)])
    ts.extend([(ix,yy) for yy in range(iy,fy)])
    ti.extend([(xx,fy) for xx in range(ix,fx)])
    ti.extend([(fx,yy) for yy in range(iy,fy)])


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

def carrosBFS(listaCarros, end, grafo):
    #lista de posiçoes usadas
    usadas = []
    done = set()
    #nº carros
    dic = {}
    n = 0
    #inicializar
    for c in listaCarros:
        solve,w = grafo.procuraBFS(c,end)
        #aux.append((solve,w))
        dic[n] = [solve[0]]
        n += 1
    n = len(listaCarros)
    
    while len(done) != n:
        for key in range(n):
            # ultimo carro da solução
            last = dic[key][-1]
            solve,w = grafo.procuraBFS(last, end)
    
            usadas = [dic[car][-1].getPos() for car in range(key)]
    
            #if (solve == []):
            #    done.add(key)

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





def carrosDFS(listaCarros, end, grafo):
    #lista de posiçoes usadas
    usadas = []
    done = set()
    #nº carros
    dic = {}
    n = 0
    #inicializar
    for c in listaCarros:
        solve,w = grafo.procuraDFS3(c,end)
        #aux.append((solve,w))
        dic[n] = [solve[0]]
        n += 1
    n = len(listaCarros)
    
    while len(done) != n:
        for key in range(n):
            # ultimo carro da solução
            last = dic[key][-1]
            solve,w = grafo.procuraDFS3(last, end)
    
            usadas = [dic[car][-1].getPos() for car in range(key)]
    
            #if (solve == []):
            #    done.add(key)

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










def carrosgreedy(listaCarros, end, grafo):
    #lista de posiçoes usadas
    usadas = []
    done = set()
    #nº carros
    dic = {}
    n = 0
    #inicializar
    for c in listaCarros:
        solve,w = grafo.greedy(c,end)
        #aux.append((solve,w))
        dic[n] = [solve[0]]
        n += 1
    n = len(listaCarros)
    
    while len(done) != n:
        for key in range(n):
            # ultimo carro da solução
            last = dic[key][-1]
            solve,w = grafo.greedy(last, end)
    
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

def carrosaEstrela(listaCarros, end, grafo):
    #lista de posiçoes usadas
    usadas = []
    done = set()
    #nº carros
    dic = {}
    n = 0
    #inicializar
    for c in listaCarros:
        solve,w = grafo.aEstrela(c,end)
        #aux.append((solve,w))
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

def fazCarros(l):
    q = []
    for pos in l:
        q.append(Carro(pos))
    return q

#np    = 5
#path  = f"../pistas/pista{np}.txt"
#p     = pista(path)
#start = charPosition(p,"P")
#end   = charPosition(p,"F")
#c     = Carro(start[0])
#c2    = Carro((4,4))
#c3    = Carro((4,5))
#c4    = Carro((2,2))
#c5    = Carro((3,3))
#c2   = Carro((10,1))
#c3   = Carro((18,1))
#c2   = Carro((36,43))
#c3   = Carro((34,34))

#pathFile = f"../pickle/grafo{np}.pkl"
#if os.path.exists(pathFile):
#    with open(pathFile, "rb") as file: #        print("loading data from "+pathFile)
#        g = pickle.load(file)
#        print("done")
#else:
#    g = geraGrafo(p,c,end)
#    with open(pathFile, "wb") as f:
#        print("dumping data to "+pathFile)
#        pickle.dump(g, f)
#        print("done")
#lista = [c,c2,c3]
#lista = [c]

#ç = carrosaEstrela(lista,end,g)
#ç = carrosaEstrela(lista,end,g)
#ç = carrosgreedy(lista,end,g)
#ç = carrosBFS(lista,end,g)

#ppCarros(p,ç,g)
#solve,w = g.procuraDFS(c,end)
#print(solve)
#pp(p,solve)
#print("custo =",w)
