def mostra_pistas():
    print("PISTAS")
    print("\t1.Pista 1")
    print("\t2.Pista 2")
    print("\t3.Pista 3")


def menu():
    print("[1] - Escolher a pista")
    print("[0] - Sair")

def main():
    menu()
    option =  int(input("Escolha uma opereção: "))
    while(option !=0 ):
        if option == 1:
            mostra_pistas()
            ans = int(input("Escolha uma opereção: "))
            if ans == 1:
                print(ans)
            elif ans == 2:
                print(ans)
            elif ans == 3:
                print(ans)

            else:
                print("Escolha inválida")
                break
        else:
            print("Entrada inválda")


    print("A sair...")


if __name__ == "__main__":
    main()
