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
                playerMode()
                playerModeVar = entrada() 
            
                if playerModeVar == 0:
                    voltarMenu()
                    flag2=False
            
                elif playerModeVar == 1:                       #single player
                    selecionapistasMenu()
                    npista = entrada() 
                    flag3=True
                    
                    while flag3:
                        if npista == 0:
                            voltarMenu()
                            flag3=False
                        
                        elif(npista == 1 or npista == 2 or npista == 3 or npista == 4):    
                            
                            path  = f"../pistas/pista{npista}.txt"
                            p=pista(path)
                            start = charPosition (p,"P") [0]
                            c = Carro(start)
                            end = charPosition (p,"F")
                            g = geraGrafo(p,c,end)
                            
                            flag5 = True
                            while flag5:
                                pistaMenu(str(npista))
                                pistaMenuVar = entrada() 
                                
                                if pistaMenuVar == 0:
                                    voltarMenu()
                                    flag5=False
                                elif pistaMenuVar == 1:
                                     pp(p,[])
                                elif pistaMenuVar == 2:
                                    solve2,w2 = g.procuraBFS(c,end)
                                    pp(p,solve2)
                                    print("custo =",w2)
                                #fixme - falta para as outras operações                                
                                else:
                                    entradaInvalida()
                        else:
                            entradaInvalida()
                            
                elif playerModeVar == 2:                       #multi player
                    numCarros()
                    numCarrosVar = entrada()
                    selecionapistasMenu()
                    npista = entrada() 
                    flag6= True
                    while flag6:
                        if npista == 0:
                            voltarMenu()
                            flag6=False
                        
                        elif(npista == 1 or npista == 2 or npista == 3 or npista == 4):    
                            
                            path  = f"../pistas/pista{npista}.txt"    
                            #for i in range(numCarrosVar):
                            p=pista(path)
                            start = charPosition (p,"P") 
                            c = Carro(start)
                            end = charPosition (p,"F")
                            g = geraGrafo(p,c,end)
                            
                            flag8=True
                            while flag8:
                                pistaMenu(str(npista))
                                pistaMenuVar = entrada() 
                                
                                if pistaMenuVar == 0:
                                    voltarMenu()
                                    flag8=False
                                elif pistaMenuVar == 1:
                                     pp(p,[])
                                elif pistaMenu == 2:
                                    solve2,w2 = g.procuraBFS(c,end)
                                    pp(p,solve2)
                                    print("custo =",w2)
                                #fixme - falta para as outras operações                                
                                else:
                                    entradaInvalida()
                        else:
                            entradaInvalida()
                    
                else:
                    entradaInvalida()
                
        else:
            entradaInvalida()
    
if __name__ == "__main__":
    main()