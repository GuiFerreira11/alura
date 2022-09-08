def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while not enforcou and not acertou:

        chute = input("Escolha uma letra: ")
        chute = chute.strip()

        index = 1

        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print("Encontrei a letra {} na posição {}.".format(letra, chute))
            index = index + 1

        print("Jogando ...")

    print("Fim do jogo.")


if __name__ == "__main__":
    jogar()
