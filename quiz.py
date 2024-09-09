perguntas = ['Qual é o elemento químico representado pelo símbolo ‘Fe’?', 'Qual a capital da frança?' , 'Qual é o esporte mais popular do Brasil?']
respostas = ['ferro','paris', 'futebol']
pontos = [10, 10, 10]

print('''Bem vindo ao nosso quiz.

''')

pontos_total = 0

for i, perguntas in enumerate(perguntas):
  resposta_usuario = input(f'{perguntas}').lower().replace("â", "a").replace("é", "e").replace("ú", "u").replace("í", "i").replace("ç", "c")
  if resposta_usuario == respostas[i]:
    print("Parábens, você acertou!")
    pontos_total += pontos[i]

  else:
    print("Que pena, você errou!")

print(f"Seus pontos são: {pontos_total}! Obrigado por participar.")