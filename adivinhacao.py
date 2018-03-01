print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentavias = 3
rodada = 1

while(rodada <= total_tentavias):

    print("Tentativa:",rodada, "de", total_tentavias)
    chute_str = input("Digite o seu número: ")
    print("Você digitou :" ,chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto


    if(acertou):
        print("Parabéns! Você acertou!")
    elif(maior):
        print("O seu chute foi maior do que o número secreto!")
    else:
        print("O seu chute foi menor do que o número secreto!")

    rodada = rodada + 1

print("*********************************")
print("Fim do jogo")
print("*********************************")