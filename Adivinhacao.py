print("*******************************")
print("bem-vindo no jogo de Advinhação")
print("*******************************")

numero_secreto = 42
total_de_tentativas = 3

while (total_de_tentativas > 0):
    print("Tentativa:" , total_de_tentativas)
    chute_str = input("Digite o seu numero: ")
    print("Você Digitou" , chute_str)
    chute = int (chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! O seu número foi maior que do que o número secreto!")
        elif(menor):
            print("Você errou! O seu número foi menor que do que o número secreto!")

    total_de_tentativas = total_de_tentativas - 1


print("Fim do Jogo.")