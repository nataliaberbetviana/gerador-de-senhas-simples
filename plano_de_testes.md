# Plano de Testes para o Gerador de Senhas

## Objetivo
Garantir que a função 'gerar_senha' produza senhas seguras e confiáveis.

---

### Teste de Comprimento da Senha
**Motivo:** Este teste verifica se a senha gerada tem o comprimento exato que o usuário solicitou. É a validação mais básica para garantir que a função está funcionando corretamente.

### Teste de Aleatoriedade
**Motivo:** Uma senha segura precisa ser aleatória. Este teste garante que a função não está retornando a mesma senha para o mesmo input, verificando se os resultados são diferentes.

### Teste de Conteúdo
**Motivo:**  Este teste garante que a senha gerada contém apenas os caracteres válidos que você definiu (letras, números, pontuação). Ele previne que o gerador crie caracteres inesperados ou indesejados.

### Teste de Diversidade de Caracteres
**Motivo:** Uma senha segura deve ter uma mistura de tipos de caracteres. Este teste garante que a senha gerada contém pelo menos um caractere de cada categoria: letras maiúsculas, minúsculas, números e caracteres especiais.