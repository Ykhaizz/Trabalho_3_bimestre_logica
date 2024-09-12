# Função para exibir o menu de operações
def exibir_menu(): # Def utilizamos para uma rotina que será repetida, em diferentes partes do programa
    print("Escolha a operação desejada:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

# Solicita ao usuário que escolha uma operação
exibir_menu()
operacao = input("Digite o número da operação (1/2/3/4): ")

# Solicita ao usuário que insira dois números
numero1 = float(input("Digite o primeiro número: ")) #float é um numero inteiro, não sendo dicimal
numero2 = float(input("Digite o segundo número: "))

# Executa a operação escolhida e exibe o resultado
if operacao == '1':
    resultado = numero1 + numero2
    print(f"O resultado da adição é: {resultado}")
elif operacao == '2':
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == '3':
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == '4':
    # Verifica se o divisor é zero antes de realizar a divisão
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha uma opção entre 1, 2, 3 ou 4.")
