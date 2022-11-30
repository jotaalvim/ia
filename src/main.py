from interface import Interface
from vetorrace  import *

def main():
    saida = -1

    while saida != 0:
        Interface.mainMenu()
        saida = Interface.pedeInput()
        if saida == 0:
            Interface.sair()
        elif saida == 1:
            i = -1
            while i != 0:
                Interface.jogarMenu()
                i = Interface.pedeInput()
                if i == 0:
                    Interface.voltarMenuPrincipal()
                elif(i == 1 or i == 2 or i == 3 or i == 4): 
                    e = -1
                    path = f"../pistas/pista{i}.txt"
                    p = pista(path)
                    start = charPosition (p,"P") [0]
                    c = Carro(start)
                    end = charPosition (p,"F")
                    g = geraGrafo(p,c,end)
                    while e!=0:
                        Interface.pistaMenu(str(i))
                        e=Interface.pedeInput()
                        
                        # depos é implementar as merdas
                        #printpista
                        if e == 1:
                            pp(p,[])
                        elif e == 2:
                            solve2,w2 = g.procuraBFS(c,end)
                            pp(p,solve2)
                            print("custo =",w2)
                        elif e == 3:
                            solve,w = g.procuraDFS(c,end)
                            pp(p,solve)
                            print("custo =",w)
                        else:
                            Interface.entradaInvalida()
                else:
                    Interface.entradaInvalida()
        else: 
            Interface.entradaInvalida()
        
if __name__ == "__main__":
    main()
