import os

def mainMenu():
    os.system("clear")
    print("┌────────────────────────────────────────────────────────────────┐")
    print("│                            MAIN MENU                           │")
    print("├────────────────────────────────────────────────────────────────┤")
    print("│                             1─JOGAR                            │")
    print("│                             0─SAIR                             │")
    print("└────────────────────────────────────────────────────────────────┘")
    
def playerMode():
    os.system("clear")
    print("┌────────────────────────────────────────────────────────────────┐")
    print("│                            PLAYER MODE                         │")
    print("├────────────────────────────────────────────────────────────────┤")
    print("│                           1-SINGLEPLAYER                       │")
    print("│                           2-MULTIPLAYER                        │")
    print("│                           0-VOLTAR                             │")
    print("└────────────────────────────────────────────────────────────────┘")

# Caso selecione Multiplayer -> "Introduza o número de jogadores"

def selecionapistasMenu():
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
    os.system("clear")
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


def sair():
    os.system("clear")
    print("┌────────────────────────────────────────────────────────────────┐")
    print("│                             A SAIR...                          │")
    print("└────────────────────────────────────────────────────────────────┘")

def voltarMenu():
    os.system("clear")
    print("┌────────────────────────────────────────────────────────────────┐")
    print("│                            VOLTANDO...                         │")
    print("└────────────────────────────────────────────────────────────────┘")

def numCarros():
    os.system("clear")
    print("┌────────────────────────────────────────────────────────────────┐")
    print("│                   INSIRA O NÚMERO DE JOGADORES                 │")
    print("└────────────────────────────────────────────────────────────────┘")
    

def mudarPartida():
    os.system("clear")
    print("┌────────────────────────────────────────────────────────────────┐")
    print("│                 DESEJA ESCOLHER PONTO DE PARTIDA               │")
    print("├────────────────────────────────────────────────────────────────┤")
    print("│                         1 ─ SIM                                │")
    print("│                         2 ─ NÃO                                │") 
    print("└────────────────────────────────────────────────────────────────┘")
    
         
def pedeCoord():
    os.system("clear")
    print("┌────────────────────────────────────────────────────────────────┐")
    print("│                     INTRODUZA AS COORDENADAS                   │")
    print("└────────────────────────────────────────────────────────────────┘")
    
    
def entrada():
    return int(input("ENTRADA ──> "))

def coords():
    return input("COORDENADAS ──> ")