import random

vitorias = 0
derrotas = 0

def jogo_jokenpo():
    
    global vitorias, derrotas
    jogada = ['pedra', 'papel', 'tesoura']
    jogada_computador = random.choice(jogada)

    try:
        jogada_usuario = input("Escolha sua jogada (pedra, papel ou tesoura): ").lower()
        if jogada_usuario not in jogada:
            print("Por favor, escolha entre as opções válidas: pedra, papel e tesoura!")
            jogo_jokenpo()

        print(f"A jogada do computador foi: {jogada_computador}")

        if jogada_usuario == jogada_computador:
            print("Ops, deu empate!")

        elif (jogada_usuario == 'tesoura' and jogada_computador == 'papel') or (jogada_usuario == 'pedra' and jogada_computador == 'tesoura') or (jogada_usuario == 'papel' and jogada_computador == 'pedra'):
            print('Parabéns, você ganhou!')
            vitorias += 1
        else:
            print("Que pena, você perdeu!")
            derrotas += 1

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    print(f"Suas vitórias: {vitorias} || Suas derrotas: {derrotas}")

    jogar_denovo = input("Você gostaria de jogar novamente? Digite 1 para sim, e 2 para não: ")
    if jogar_denovo == '1':
        jogo_jokenpo()
    else:
        print("Jogo encerrado :(")
        return

