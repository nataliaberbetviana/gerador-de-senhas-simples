# Importa a biblioteca 'string' para conjuntos de caracteres
# e a biblioteca 'random' para sortear os caracteres.
import string
import random

# --- Parte 1: A Função de Geração de Senha ---
# Esta função é responsável por criar a senha e devolvê-la.
# Ela não lida com a entrada do usuário.
def gerar_senha(quantidade_de_caracteres):
    # Conjunto de todos os caracteres que podem ser usados na senha.
    caracteres_disponiveis = string.ascii_letters + string.digits + string.punctuation

    # Variável vazia para guardar a senha à medida que ela é construída.
    senha_final = ""

    # Loop que se repete o número exato de vezes do tamanho da senha.
    for _ in range(quantidade_de_caracteres):
        # Escolhe um caractere aleatório e o adiciona à senha.
        caractere_sorteado = random.choice(caracteres_disponiveis)
        senha_final += caractere_sorteado

    # Devolve a senha pronta.
    return senha_final


# --- Parte 2: O Bloco de Execução Principal ---
# Este bloco roda o programa e lida com a entrada e saída.
if __name__ == "__main__":
    # Loop para garantir que o usuário digite um número válido.
    while True:
        try:
            # Pede o tamanho da senha ao usuário e converte para um número.
            tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
            break  # Sai do loop se a entrada for válida.
        except ValueError:
            # Captura o erro se o usuário digitar algo que não é um número.
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # Chama a função gerar_senha para criar a senha.
    senha_gerada = gerar_senha(tamanho_senha)

    # Imprime a senha final para o usuário.
    print(f"O número de caracteres é: {tamanho_senha}")
    print(f"A senha gerada é: {senha_gerada}")