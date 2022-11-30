from interface import Interface

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
                    while e!=0:
                        Interface.pistaMenu(str(i))
                        e=Interface.pedeInput()
                        
                        # depos é implementar as merdas
                        if e == 1:
                            print("ola")
                else:
                    Interface.entradaInvalida()
        else: 
            Interface.entradaInvalida()
        
if __name__ == "__main__":
    main()
