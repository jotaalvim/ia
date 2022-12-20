from interface import *
from vetorrace import *

def main():
    saida = -1

    while saida != 0:
    #menu inicial
        mainMenu()
        saida = pedeInput()
    #sai do jogo
        if saida == 0:
            sair()
    #jogar
        elif saida == 1:
            i = -1
            while i != 0:
    #menu numjogadores
                playerNumber()
                numjogadores = pedeInput()
                while numjogadores != 0:
    #single player
                    if numjogadores == 1:
                        PistasMenu()
                        i = pedeInput()
    #volta ao menu do num de jogadaores                    
                        if i == 0:
                            voltarMenu()
    #escolhe a pista
                        elif(i == 1 or i == 2 or i == 3 or i == 4): 
                            e = -1
                            path = f"../pistas/pista{i}.txt"
                            p = pista(path)
                            start = charPosition (p,"P") [0]
                            c = Carro(start)
                            end = charPosition (p,"F")
                            g = geraGrafo(p,c,end)
    
                            while e!=0:
    #menu da pista, escolher a opção                            
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
                                #elif e == 3:         
    #MULTIPLAYER                     
                    elif numjogadores == 2:
                        numCarros()
                        ncarros=pedeInput()
                        PistasMenu()
                        i = pedeInput()
    #volta ao menu do num de jogadaores                    
                        if i == 0:
                            voltarMenu()
    #escolhe a pista
                        elif(i == 1 or i == 2 or i == 3 or i == 4): 
                            e = -1
                            path = f"../pistas/pista{i}.txt"
                            p = pista(path)
                            start = charPosition (p,"P") [0]
                            c = Carro(start)
                            end = charPosition (p,"F")
                            g = geraGrafo(p,c,end)
    
                            while e!=0:
    #menu da pista, escolher a opção                            
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
                                #elif e == 3: )
            else:
                entradaInvalida()

if __name__ == "__main__":
    main()
