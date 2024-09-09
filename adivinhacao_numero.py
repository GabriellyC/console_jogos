import random

def jogo():
    alvo = random.randint(0, 1000)
    tentativas = 5

    while tentativas > 0:
        try:
            chute = int(input("Digite um número inteiro entre 0 e 1000: "))
            if chute < 0 or chute > 1000:
                print("Digite um número dentro do intervalo solicitado")
                continue

            if chute == alvo:
                print("Parabéns, você acertou!!")
                break
            else:
                sugestao = "menor" if chute > alvo else "maior"
                print(f"Que pena, mais sorte da próxima vez! O número correto é {sugestao} que o número que você chutou!")

            tentativas -= 1

        except ValueError:
            print("Valor digitado deve ser um número inteiro")

    if tentativas == 0:
        print(f"Suas tentativas acabaram! O número correto era {alvo}.")

    jogar_denovo = input("Você gostaria de jogar novamente? Digite 1 para sim, e 2 para não: ")
    if jogar_denovo == '1':
        jogo()
    else:
      print("Jogo encerrado :(")
      return

jogo()