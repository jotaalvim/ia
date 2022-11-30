class Interface:
    def mainMenu():
        print("+----------------------------------------------------------------+")
        print("|                            MAIN MENU                           |")
        print("+----------------------------------------------------------------+")
        print("|                             1-JOGAR                            |")
        print("|                             0-SAIR                             |")
        print("+----------------------------------------------------------------+")
        
        
    def jogarMenu():
        print("+----------------------------------------------------------------+")
        print("|                             PISTAS                             |")
        print("+----------------------------------------------------------------+")      
        print("|                            1-PISTA 1                           |")
        print("|                            2-PISTA 2                           |")
        print("|                            3-PISTA 3                           |")
        print("|                            4-PISTA 4                           |")
        print("|                            0-VOLTAR ATRÁS                      |")
        print("+----------------------------------------------------------------+") 
        
    def pistaMenu(numPista):
        print("+----------------------------------------------------------------+")
        print("|                           PISTA " + numPista + "                   |")
        print("+----------------------------------------------------------------+")      
        print("|                          1-PRINT PISTA                         |")
        print("|                          2-BFS                                 |")
        print("|                          3-DFS                                 |")
        print("|                          0-VOLTAR ATRÁS                        |")
        print("+----------------------------------------------------------------+") 
    
    def entradaInvalida():
        print("+----------------------------------------------------------------+")
        print("|                        ENTRADA INVÁLIDA                        |")
        print("+----------------------------------------------------------------+")
        
    def pedeInput():
        return int(input("INTRODUZA A SUA OPÇÃO --> "))
    
    def sair():
        print("+----------------------------------------------------------------+")
        print("|                             A SAIR...                          |")
        print("+----------------------------------------------------------------+")
        
    def voltarMenuPrincipal():
        print("+----------------------------------------------------------------+")
        print("|                  VOLTANDO AO MENU PRINCIPAL...                 |")
        print("+----------------------------------------------------------------+")
