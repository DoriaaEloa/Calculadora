print("1 - Soma: ")
print("2 - Subtração ")
print("3 - Multiplicação ")
print("4 - Divisão ")
escolha = int(input("Escolha a operação: "))

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

# É melhor botar == a opção para melhor estrutura 
if escolha == 1:
    print("O resultado da soma é ", num1 + num2)
elif escolha == 2:
    print("O resultado da subtração é ", num1 - num2)
elif escolha == 3:
    print("O resultado da multiplicação é ", num1 * num2)
elif escolha == 4:
    if num1 and num2 != 0:
     print("O resultado da divisão é ", num1 / num2)
    # roda se o número for diferente de 0
    else:
        print("O número 0 não é permitido")
    # roda se algum número for 0
else:
    print("Número inválido")