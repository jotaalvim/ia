from interface import *
from vetorrace import *

def main():
    saida = -1

    while saida != 0:
        mainMenu()
        saida = pedeInput()
        if saida == 0:
            sair()
        elif saida == 1:
            i = -1
            while i != 0:
                jogarMenu()
                i = pedeInput()
                if i == 0:
                    voltarMenuPrincipal()
                elif(i == 1 or i == 2 or i == 3 or i == 4): 
                    e = -1
                    path = f"../pistas/pista{i}.txt"
                    p = pista(path)
                    start = charPosition (p,"P") [0]
                    c = Carro(start)
                    end = charPosition (p,"F")
                    g = geraGrafo(p,c,end)
                    while e!=0:
                        pistaMenu(str(i))
                        e=pedeInput()
                        
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
                        elif e == 4:
                            solve3,w3 = g.greedy(c,end)
                            pp(p,solve3)
                            print("custo =",w3)

                        elif e == 5:
                            solve4,w4 = g.aEstrela(c,end)
                            pp(p,solve4)
                            print("custo =",w4)

                        else:
                            entradaInvalida()
                else:
                    entradaInvalida()
        else: 
            entradaInvalida()
        
if __name__ == "__main__":
    main()
