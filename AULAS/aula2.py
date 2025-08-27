# # Operadores

# num1 = int(input('Digite um numero: '))
# num2 = int(input('Digite o segundo numero: '))

# soma = num1+num2
# subt = num1-num2
# mult = num1*num2
# divi = num1/num2
# divT = num1//num2
# sobr = num1%num2
# elev = num1**num2
# raiz1 = num1**0.5
# raiz2 = num2**0.5

# print('A soma é: ',soma)
# print('A subtração é: ',subt)
# print('A multiplicação é: ',mult)
# print('A divisão é: ',divi)
# print('A divisão inteira é: ',divT)
# print('A sobra é: ',sobr)
# print('Elevado é: ',elev)
# print('A raiz do 1° é: ',raiz1)
# print('A raiz do 2° é: ',raiz2)

print('====================================')
print('Seja Bem vindo, ao sistema de horas')
print('====================================')

hora = int(input("Digite uma hora "))

if hora < 12:
    print("Bom dia!")
elif hora < 18:
    print('Boa tarde!')
else :
    print("Boa noite!")