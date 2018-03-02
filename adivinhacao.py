print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 5
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

    if(acertou):
        print("Parabéns! Você acertou!")
        break;
    elif(maior):
        print("O seu chute foi maior do que o número secreto!")
    else:
        print("O seu chute foi menor do que o número secreto!")

print("*********************************")
print("Fim do jogo")
print("*********************************")