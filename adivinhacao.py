import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,11)
    total_tentavias = 0
    pontos = 100

    print("Níveis:")
    print("(1) Fácil\n(2) Médio\n(3) Difícil")

    nivel = int(input("Defina o nível:"))

    if (nivel == 1):
        total_tentavias = 7
    elif (nivel == 2):
        total_tentavias = 5
    else:
        total_tentavias = 3

    for rodada in range(1, total_tentavias + 1):

        print("Tentativa {} de {}".format(rodada, total_tentavias))
        chute_str = input("Digite um número entre 1 e 10: ")
        print("Você digitou :" ,chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 10):
            print("Valor não aceito!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou!")
            print("Voce fez {} pontos:".format(pontos))
            break;
        else:
            if(maior):
                print("Voce errou! O seu chute foi maior que o número secreto")
            elif (menor):
                print("Voce errou! O seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("*********************************")
    print("***********Fim do jogo***********")
    print("*********************************")

if (__name__ == "__main__"):
    jogar()