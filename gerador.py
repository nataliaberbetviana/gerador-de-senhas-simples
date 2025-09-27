# Importa as bibliotecas necessárias para o projeto
# 'string' contém constantes úteis como letras e números
# 'random' é usado para escolher um caractere de forma aleatória
import string
import random

# Define uma string com todos os caracteres que a senha pode ter.
# Isso inclui letras (maiúsculas e minúsculas), números e pontuação.
cartacteres_disponiveis = string.ascii_letters + string.digits + string.punctuation

# Cria uma variável vazia para armazenar a senha gerada.
senha_final = ""

# Inicia um loop infinito para pedir a entrada do usuário.
# O loop só vai parar quando uma entrada válida for fornecida.
while True:
    try:
        # Pede ao usuário o tamanho da senha e converte a entrada para um número inteiro.
        quantidade_de_caracteres = int(input("Digite o tamanho da senha desejada: "))
        # Se a conversão for bem-sucedida, sai do loop.
        break
    except ValueError:
        # Se a conversão falhar (o usuário digitou um texto), imprime uma mensagem de erro e o loop continua.
        print("Entrada inválida. Por favor digite um número inteiro.")

# Usa um loop 'for' para gerar cada caractere da senha.
# O loop vai rodar exatamente a quantidade de vezes que o usuário pediu.
# O '_' é usado por convenção, pois a variável do loop não será utilizada
for _ in range(quantidade_de_caracteres):
    caractere_sorteado = random.choice(cartacteres_disponiveis)
    senha_final += caractere_sorteado

# Imprime o número de caracteres e a senha gerada.
print(f"O número de caracteres é: {quantidade_de_caracteres}")
print(f"A senha gerada é: {senha_final}!")