def jogar ():

    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "palavra"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra?")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrou a letra '{}' na posição {}".format(letra, index))
            index = index + 1

    print("***********")
    print("Fim do jogo")
    print("***********")

if (__name__ == "__main__"):
    jogar()