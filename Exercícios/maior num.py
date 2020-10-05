num = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num > num2:
    print(f'{num} é maior')
elif num2 > num:
    print(f'{num2} é maior')
elif num == num2:
    print('Números iguais')