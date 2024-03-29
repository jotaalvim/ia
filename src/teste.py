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
                    pista = entrada() 
                    flag3=True
                    
                    while flag3:
                        if pista == 0:
                            voltarMenu()
                            flag3=False
                        
                        elif(pista == 1 or pista == 2 or pista == 3 or pista == 4):
                            flag4=True
                            
                            shutil.copy(f"../pistas/pista{pista}.txt","../pistasUser/pistaUser.txt")
                            while flag4:
                                mudarPartida()
                                mudarPartidaVar = entrada() 
                                
                                if mudarPartidaVar == 2:
                                    flag4=False
                                
                                elif mudarPartidaVar == 1:
                                    
                                    pedeCoord()
                                    coordenadas = coords() 
                                    mudaPartidas(coordenadas,"../pistasUser/pistaUser.txt")
                                
                                else:
                                    entradaInvalida()
                            
                            path=""
                            
                            if(mudarPartidaVar==2):
                                path = f"../pistas/pista{pista}.txt"
                            
                            if(mudarPartidaVar==1):
                                path = f"../pistasUser/pistaUser.txt"
                                
                            start = charPosition (p,"P") [0]
                            c = Carro(start)
                            end = charPosition (p,"F")
                            g = geraGrafo(p,c,end)
                            
                            flag5 = True
                            while flag5:
                                pistaMenu(str(pista))
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
                    pista = entrada() 
                    flag6= True
                    while flag6:
                        if pista == 0:
                            voltarMenu()
                            flag6=False
                        
                        elif(pista == 1 or pista == 2 or pista == 3 or pista == 4):
                            
                            flag7=True
                            mudarPartidaVar=-1
                            while flag7:
                                mudarPartida()
                                mudarPartidaVar = entrada() 
                                
                                if mudarPartidaVar == 2:
                                    flag7=False
                                elif mudarPartidaVar == 1:
                                    shutil.copy(f"../pistas/pista{pista}.txt","../pistasUser/pistaUser.txt")
                                    #for i in range(numCarros):
                                    pedeCoord()
                                    coordenadas = coords() 
                                    mudaPartidas(coordenadas,"../pistasUser/pistaUser.txt")
                                else:
                                    entradaInvalida()
                            
                            path=""
                            
                            if(mudarPartidaVar ==2):
                                path = f"../pistas/pista{pista}.txt"
                            
                            if(mudarPartidaVar ==1):
                                path = f"../pistasUser/pistaUser.txt"
                                
                            for i in range(numCarrosVar):
                                start = charPosition (p,"P") 
                                c = Carro(start)
                                end = charPosition (p,"F")
                                g = geraGrafo(p,c,end)
                            
                            flag8=True
                            while flag8:
                                pistaMenu(str(pista))
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