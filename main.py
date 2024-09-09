
from adivinhacao_numero import jogo
from jokenpo import jogo_jokenpo
from quiz import quiz
print("Bem vindo ao console de jogos em Python!")

menu = '''

Escolha o número referente ao jogo que deseja jogar:
1 - Adivinhação de números
2 - Jokenpo(Pedra, Papel ou Tesoura)
3 - Perguntas e respostas


'''

entrada_usuario = input(menu)

if entrada_usuario == "1":
    jogo()
elif entrada_usuario == "2":
    jogo_jokenpo()
elif entrada_usuario == "3":
    quiz()