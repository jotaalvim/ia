from queue import Queue

class Grafo:
    def __init__(self,directed=False):
        self.nodes = set() #conjunto
        self.dic = dict()
        self.directed = directed
        self.heuristica = dict()

    def __str__(self): 
        s = ''
        for k in self.dic.keys():
            s += str(k) +' -> '+ str(self.dic[k]) + '\n'
        return s

    #default weight = 0
    def add_edge (self,nome1,nome2,weight=0):
        #removi porque achei que nao fazemos nada com isto
        #n1 = Node(nome1)
        #n2 = Node(nome2)
        #self.nodes.add(nome1)
        #self.nodes.add(nome2)
        if (nome1 in self.dic):
            self.dic[nome1].add((nome2,weight))
        else:
            self.dic[nome1] = {(nome2,weight)}
            
        if not self.directed:
            if (nome2 in self.dic):
                self.dic[nome2].add((nome1,weight))
            else:
                self.dic[nome2] = {(nome1,weight)}

    #imprime aresta
    #get Nodo by name

    #def getNodobyName(self,name):

    #def getArcConst(self,n1,n2):

    def retorna(self,name,listaNodos):
        for n,p in listaNodos:
            if n == name:
                return n,p
        return name,1

    def calculaCusto (self,listaNodos):
        if len(listaNodos) == 0:
            return 0

        if len(listaNodos) == 1:
            return 1

        _, b = self.retorna(listaNodos[1], self.dic[listaNodos[0]])
        if len(listaNodos) == 2:
            return b
        return  b + self.calculaCusto(listaNodos[1:])


    def procuraDFS(self,start,end,path=[],visited=set()):
        path.append(start)
        visited.add(start)

        if start.getPos() in end:
            custoT = self.calculaCusto(path)
            return (path,custoT)

        #FIXME nao ta bem
        if (start in self.dic):
            for adjacente, peso in self.dic[start]:
                if adjacente not in visited:
                    resultado = self.procuraDFS(adjacente, end, path, visited)
                    if resultado is not None:
                        return resultado

        path.pop()
        #return None
        return ([],0)
    
    def procuraBFS(self, start, end):
        q = Queue()
        q.put(start)
        visited = set()
        pais = dict()
        pais[start] = None
        visited.add(start)
        #nodo atual
        u = start
        while not q.empty() and (not (u.pos in end)):
            u = q.get()  
            #FIXME u in self.dic
            if u in self.dic:
                for no,peso in self.dic[u]:
                    if no not in visited:
                        visited.add(no)
                        pais[no] = u
                        q.put(no)

        #recontruir caminho
        path = []
        if u.pos in end:
            while pais[u] != None:
                path.append(u)
                u = pais[u]
            path.append(u)

        path.reverse()

        #return (path, 0)
        return (path, self.calculaCusto(path))
        
    def add_heuristica(self,nodo,x):
        self.heuristica[nodo] = x
    
    def getNeighbours(self,n):
        return self.dic[n]


    def greedy(self, start, end):
        # open_list é uma lista de nodos visitados, mas com vizinhos
        # que ainda não foram todos visitados, começa com o  start
        # closed_list é uma lista de nodos visitados
        # e todos os seus vizinhos também já o foram
        open_list = set([start])
        closed_list = set([])

        # parents é um dicionário que mantém o antecessor de um nodo
        # começa com start
        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            # encontraf nodo com a menor heuristica
            for v in open_list:
                if n == None or self.heuristica[v] < self.heuristica[n]:
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # se o nodo corrente é o destino
            # reconstruir o caminho a partir desse nodo até ao start
            # seguindo o antecessor
            pos = n.getPos()
            if pos in end:
                reconst_path = []
    
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start)
                reconst_path.reverse()
                return (reconst_path, self.calculaCusto(reconst_path))
    
            # para todos os vizinhos  do nodo corrente
            if (n in self.dic):
                for m,weight in self.getNeighbours(n):
                    # Se o nodo corrente nao esta na open nem na closed list
                    # adiciona-lo à open_list e marcar o antecessor
                    if m not in open_list and m not in closed_list:
                        open_list.add(m)
                        parents[m] = n
    
            # remover n da open_list e adiciona-lo à closed_list
            # porque todos os seus vizinhos foram inspecionados
            open_list.remove(n)
            closed_list.add(n)
        print('Path does not exist!')
        return None

    def aEstrela(self, start, end):
        # open_list é uma lista de nodos visitados, mas com vizinhos
        # que ainda não foram todos visitados, começa com o  start
        # closed_list é uma lista de nodos visitados
        # e todos os seus vizinhos também já o foram
        open_list = set([start])
        closed_list = set([])

        # parents é um dicionário que mantém o antecessor de um nodo
        # começa com start
        parents = {}
        parents[start] = start

        g = {}
        g[start] = 0
        while len(open_list) > 0:
            n = None

            # encontraf nodo com a menor heuristica
            # + custo da aresta 
            for v in open_list:
                if n == None or g[v] + self.heuristica[v] < g[n] + self.heuristica[n]:
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # se o nodo corrente é o destino
            # reconstruir o caminho a partir desse nodo até ao start
            # seguindo o antecessor
            pos = n.getPos()
            if pos in end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start)
                reconst_path.reverse()
                return (reconst_path, self.calculaCusto(reconst_path))
            # para todos os vizinhos  do nodo corrente
            if n in self.dic:
                for m,weight in self.getNeighbours(n):
                    # Se o nodo corrente nao esta na open nem na closed list
                    # adiciona-lo à open_list e marcar o antecessor
                    if m not in open_list and m not in closed_list:
                        open_list.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight 
            # remover n da open_list e adiciona-lo à closed_list
            # porque todos os seus vizinhos foram inspecionados
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
