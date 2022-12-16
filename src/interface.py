import os

def mainMenu():
    os.system("clear")
    print("┌────────────────────────────────────────────────────────────────┐")
    print("│                            MAIN MENU                           │")
    print("├────────────────────────────────────────────────────────────────┤")
    print("│                             1─JOGAR                            │")
    print("│                             0─SAIR                             │")
    print("└────────────────────────────────────────────────────────────────┘")

def playerNumber():
    print("┌────────────────────────────────────────────────────────────────┐")
    print("│                            MAIN MENU                           │")
    print("├────────────────────────────────────────────────────────────────┤")
    print("│                             1-Singleplayer                     │")
    print("│                             2-Multiplayer                      │")
    print("│                             0-Sair                             │")
    print("└────────────────────────────────────────────────────────────────┘")

# Caso selecione Multiplayer -> "Introduza o número de jogadores"

def jogarMenu():
    os.system("clear")
    print("┌────────────────────────────────────────────────────────────────┐")
    print("│                             PISTAS                             │")
    print("├────────────────────────────────────────────────────────────────┤")
    print("│                           1 ─ PISTA 1                          │")
    print("│                           2 ─ PISTA 2                          │")
    print("│                           3 ─ PISTA 3                          │")
    print("│                           4 ─ PISTA 4                          │")
    print("│                           0 ─ VOLTAR ATRÁS                     │")
    print("└────────────────────────────────────────────────────────────────┘")

def pistaMenu(numPista):
    #os.system("clear")
    print("┌────────────────────────────────────────────────────────────────┐")
    print("│                           PISTA " + numPista + "                              │")
    print("├────────────────────────────────────────────────────────────────┤")
    print("│                         1 ─ PRINT PISTA                        │")
    print("│                         2 ─ BFS                                │")
    print("│                         3 ─ DFS                                │")
    print("│                         4 ─ GREEDY                             │")
    print("│                         5 ─ A*                                 │")
    print("│                         0 ─ VOLTAR ATRÁS                       │")
    print("└────────────────────────────────────────────────────────────────┘")

def entradaInvalida():
    os.system("clear")
    print("┌────────────────────────────────────────────────────────────────┐")
    print("│                        ENTRADA INVÁLIDA                        │")
    print("└────────────────────────────────────────────────────────────────┘")

def pedeInput():
    return int(input("INTRODUZA A SUA OPÇÃO ──> "))

def sair():
    os.system("clear")
    print("┌────────────────────────────────────────────────────────────────┐")
    print("│                             A SAIR...                          │")
    print("└────────────────────────────────────────────────────────────────┘")

def voltarMenuPrincipal():
    os.system("clear")
    print("┌────────────────────────────────────────────────────────────────┐")
    print("│                  VOLTANDO AO MENU PRINCIPAL...                 │")
    print("└────────────────────────────────────────────────────────────────┘")
