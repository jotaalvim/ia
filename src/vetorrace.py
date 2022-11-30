import time
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
def nextestado(pista,carro):
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


def geraGrafo(pista,carro):
    # grafo é direcionado
    g = Grafo(True)
    v = set() #visited
    q = Queue()

    q.put(carro)

    while not q.empty():
        #estado
        e = q.get()

        for car,w in nextestado(pista,e):
            g.add_edge(e ,car,w) 
            if (car not in v ):
                q.put(car)
        v.add(e)

    return g


def endcarro(end):
    l = []
    for pos in end:
        novoCarro = Carro(pos)
        l.append(novoCarro)
    return l

#NÂO USAMOS ISTO
def getDeclive(CarroEstadoAtual, CarroEstadoSeguinte):

    x_CarroAtual, y_CarroAtual = CarroEstadoAtual.getPos()
    x_CarroSeguinte, y_CarroSeguinte = CarroEstadoSeguinte.getPos()
    
    if (x_CarroSeguinte - x_CarroAtual) == 0:
        return 0
    declive = (y_CarroSeguinte - y_CarroAtual) / (x_CarroSeguinte - x_CarroAtual)
    
    return declive
    
def getOrdenadaOrigem(CarroEstadoAtual, declive):
    x_CarroAtual,y_CarroAtual = CarroEstadoAtual.getPos()
    ordenadaOrigem = y_CarroAtual-declive*x_CarroAtual
    return ordenadaOrigem
    
def verifica_parede_no_meio(lista_de_paredes, declive, ordenadaOrigem,carro1,carro2):
    tem_parede = False # se devolver falso, é porque nao tem parede no meio
    for coordx,coordy in lista_de_paredes:
        cx,cy   = carro1.getPos()
        cx2,cy2 = carro2.getPos()

        if ((cx > cx2 and coordx > cx2 and coordx < cx) or (cx2 > cx and coordx > cx  and coordx < cx2)) and ((cy > cy2 and coordy > cy2 and coordy < cy) or (cy2 > cy and coordy > cy  and coordy < cy2)):
            if coordy == int(declive*coordx + ordenadaOrigem):
                tem_parede = True

                #print("o = ",ordenadaOrigem)
                #print("d = ",declive)
                #print("f = ",tem_parede)
                return tem_parede


def temParede (carro,novoCarro):
    #declive
    d = getDeclive(carro,novoCarro)
    #ordnada na origem
    o = getOrdenadaOrigem(novoCarro, d)

    f = verifica_parede_no_meio(lp ,d,o,carro,novoCarro )
    return f

def intersetaParede(pista,c1,c2):
    c1x,c1y = c1.getPos()    
    c2x,c2y = c2.getPos()    

    if (c1x > c2x):
        aux = Carro((c1x,c1y))
        c1 = c2
        c2 = aux

    c1x,c1y = c1.getPos()    
    c11x,c11y = c1.getPos()    
    c2x,c2y = c2.getPos()    
    c22x,c22y = c2.getPos()    
    
    ts = []
    ti = []

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

def pp(pista,solve):
    for carros in solve:
        x,y = carros.getPos()
        pista[y][x] = '•'
        for linha in pista:
            print("".join(linha))
        print('\n\n\n\n\n\n\n\n')
        time.sleep(0.3)


p = pista("../pistas/pista4.txt")

start = charPosition (p,"P") [0]
c = Carro(start)

#Lista de paredes
#VAR GLOBAL 
lp = charPosition(p,'X')

#end = endcarro(charPosition (p,"F"))
#VARIAVEL GLOBAL 
end = charPosition (p,"F")

lista_de_paredes = charPosition(p,"#")


g = geraGrafo(p,c)
print("grafo gerado")

#novoCarro = Carro((17,1),(5,0))
#print(len(g.dic))


print("BFS")
solve,w = g.procuraBFS(c,end)
[print(str(u)) for u in solve]
print("custo =",w)
pp(p,solve)



#print("DFS")
#solve,w = g.procuraDFS(c,end)
#[print(str(u)) for u in solve]
#print("custo =",w)
#pp(p,solve)
