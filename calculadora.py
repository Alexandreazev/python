# Função para realizar a soma
def soma(a, b):
    return a + b

# Função para realizar a subtração
def subtracao(a, b):
    return a - b

# Função para realizar a multiplicação
def multiplicacao(a, b):
    return a * b

# Função para realizar a divisão
def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

# Função para imprimir o vetor de resultados
def imprimir_resultados(resultados):
    print("Resultados:")
    for i, resultado in enumerate(resultados):
        print(f"Resultado {i+1}: {resultado}")

# Inicialização do vetor de resultados
resultados = [0] * 10

# Contador de cálculos realizados
calculos_realizados = 0

while calculos_realizados < 10:
    print("Escolha a operação:")
    print("Digite 1 para soma.")
    print("Digite 2 para subtração.")
    print("Digite 3 para multiplicação.")
    print("Digite 4 para divisão.")
    print("Digite 5 para sair da calculadora.")
    
    escolha = input("Digite sua escolha: ")
    
    if escolha == '5':
        break
    
    if escolha not in ['1', '2', '3', '4']:
        print("Escolha inválida. Tente novamente.")
        continue
    
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    
    if escolha == '1':
        resultados[calculos_realizados] = soma(a, b)
    elif escolha == '2':
        resultados[calculos_realizados] = subtracao(a, b)
    elif escolha == '3':
        resultados[calculos_realizados] = multiplicacao(a, b)
    elif escolha == '4':
        resultados[calculos_realizados] = divisao(a, b)
    
    calculos_realizados += 1

imprimir_resultados(resultados)
 