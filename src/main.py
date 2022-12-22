from interface import *
from vetorrace import *

def main():
    
    flag1=True
    
    while flag1:
        
        mainMenu()
        mainMenuVar = entrada()
        
        if mainMenuVar == 0:
            sair()
            flag1 = False
        
        elif mainMenuVar == 1:
            flag2=True
            
            while flag2:
                selecionapistasMenu()
                npista = entrada() 


                if npista == 0:
                    voltarMenu()
                    flag3=False
                    
                elif(npista in [1,2,3,4,5]):    
                    pathFile = f"../pickle/grafo{npista}.pkl"
                    if os.path.exists(pathFile):
                        with open(pathFile, "rb") as file:
                            loading(pathFile)
                            g = pickle.load(file)
                            print("done")
                    else:
                        g = geraGrafo(p,c,end)
                        with open(pathFile, "wb") as f:
                            loading(pathFile)
                            pickle.dump(g, f)
                            print("done")

                        
                    flag5 = True
                    while flag5:
                        pistaMenu(str(npista))
                        pistaMenuVar = entrada() 
                        solve = None
                        path  = f"../pistas/pista{npista}.txt"
                        p     = pista(path)
                        start = fazCarros(charPosition
                                (p,"P"))
                        end   = charPosition (p,"F")

                        if pistaMenuVar == 0:
                            voltarMenu()
                            flag5=False
                        elif pistaMenuVar == 1:
                            printp(p)
                        elif pistaMenuVar == 2:
                            solve = carrosBFS(start,end,g)
                            ppCarros(p,solve,g)

                        elif pistaMenuVar == 3:
                            a = 4
                            #FIXME
                            #solve = carrosaDPS(start,end,g)
                        elif pistaMenuVar == 4:
                            solve = carrosgreedy(start,end,g)
                            ppCarros(p,solve,g)

                        elif pistaMenuVar == 5:
                            solve = carrosaEstrela(start,end,g)
                            ppCarros(p,solve,g)

                        else:
                            entradaInvalida()
                else:
                    entradaInvalida()

                #elif playerModeVar == 2:                       #multi player
                #    numCarros()
                #    numCarrosVar = entrada()
                #    selecionapistasMenu()
                #    npista = entrada() 
                #    flag6= True
                #    while flag6:
                #        if npista == 0:
                #            voltarMenu()
                #            flag6=False
                #        
                #        elif(npista == 1 or npista == 2 or npista == 3 or npista == 4):    
                #            
                #            path  = f"../pistas/pista{npista}.txt"    
                #            #for i in range(numCarrosVar):
                #            p=pista(path)
                #            start = charPosition (p,"P") 
                #            c = Carro(start)
                #            end = charPosition (p,"F")
                #            g = geraGrafo(p,c,end)
                #            
                #            flag8=True
                #            while flag8:
                #                pistaMenu(str(npista))
                #                pistaMenuVar = entrada() 
                #                
                #                if pistaMenuVar == 0:
                #                    voltarMenu()
                #                    flag8=False
                #                elif pistaMenuVar == 1:
                #                     pp(p,[])
                #                elif pistaMenu == 2:
                #                    solve2,w2 = g.procuraBFS(c,end)
                #                    pp(p,solve2)
                #                    print("custo =",w2)
                #                #fixme - falta para as outras operações                                
                #                else:
                #                    entradaInvalida()
                #        else:
                #            entradaInvalida()
                #    
                #else:
                #    entradaInvalida()

        else:
            entradaInvalida()
    
if __name__ == "__main__":
    main()
