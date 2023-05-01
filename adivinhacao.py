import random

def jogar():
    numero_aleatorio = random.randint(1, 100)
    tentativas = 0
    limite_tentativas = 10
    
    print("Bem-vindo ao jogo de adivinhação! Eu escolhi um número entre 1 e 100. Tente adivinhar qual é!")

    while tentativas < limite_tentativas:
        tentativas += 1
        palpite = int(input("Tentativa {} - Qual é o seu palpite? ".format(tentativas)))

        if palpite == numero_aleatorio:
            print("Parabéns! Você acertou o número em {} tentativas!".format(tentativas))
            jogar_novamente()
        elif palpite < numero_aleatorio:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

    print("Você não conseguiu adivinhar o número em {} tentativas. O número era {}.".format(limite_tentativas, numero_aleatorio))
    jogar_novamente()

def jogar_novamente():
    jogar_denovo = input("Deseja jogar novamente? (S/N) ")
    if jogar_denovo.upper() == "S":
        jogar()
    else:
        print("Obrigado por jogar! Até a próxima!")
        exit()

jogar()
