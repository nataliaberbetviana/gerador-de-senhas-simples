# Importa as bibliotecas necessárias para o teste
import string
from gerador import gerar_senha
import pytest

# --- Teste de Comprimento da Senha ---
# Usa 'parametrize' para testar a função com 3 tamanhos diferentes de senha.
@pytest.mark.parametrize("tamanho", [8, 12, 20])
def test_comprimento_da_senha_com_varios_tamanhos(tamanho):
    senha_gerada = gerar_senha(tamanho)
    assert len(senha_gerada) == tamanho


# --- Teste de Aleatoriedade ---
# Verifica se a senha gerada é diferente a cada chamada da função.
def test_senha_aleatoria():
    tamanho_desejado = 15
    primeira_senha = gerar_senha(tamanho_desejado)
    segunda_senha = gerar_senha(tamanho_desejado)
    assert primeira_senha != segunda_senha


# --- Teste de Validade do Conteúdo ---
# Garante que a senha contém apenas caracteres do conjunto permitido.
def test_conteudo_da_senha_eh_valido():
    tamanho = 15
    senha_gerada = gerar_senha(tamanho)
    caracteres_validos = string.ascii_letters + string.digits + string.punctuation
    for caractere in senha_gerada:
        assert caractere in caracteres_validos


# --- Teste de Diversidade do Conteúdo ---
# Verifica se a senha gerada tem pelo menos um caractere de cada tipo.
def test_senha_contem_todos_os_tipos_de_caracteres():
    tamanho_desejado = 20
    senha_gerada = gerar_senha(tamanho_desejado)

    # Usa 'any()' para verificar a presença de cada tipo de caractere.
    assert any(char in string.ascii_uppercase for char in senha_gerada)
    assert any(char in string.digits for char in senha_gerada)
    assert any(char in string.punctuation for char in senha_gerada)
    assert any(char in string.ascii_lowercase for char in senha_gerada)