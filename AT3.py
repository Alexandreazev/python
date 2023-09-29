# Solicita ao usuário a entrada de valores e os armazena em uma lista
valores = []

n = int(input("Quantos valores você deseja inserir na lista? "))

for i in range(n):
    valor = float(input(f"Digite o valor {i + 1}: "))
    valores.append(valor)

# Calcula o maior e o menor valor na lista
maior_valor = max(valores)
menor_valor = min(valores)

# Calcula a diferença entre o maior e o menor valor
diferenca = maior_valor - menor_valor

# Exibe a diferença
print(f"A diferença entre o maior e o menor valor na lista é: {diferenca}")