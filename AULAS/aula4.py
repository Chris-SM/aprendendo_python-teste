# # numeroCli = int(input("Quantos clientes você gostaria de cadastrar? "))
# # clientes = [["Jose Carlos","Vanessa","Camila"],[35,40,10],["Amarelo","Verde","Vermelho"]]
# # vetor = [0 for i in range(numeroCli)]

# # print(clientes[0][1])
# # print(clientes[1][1])
# # print(clientes[2][1])
# # for i in range(numeroCli)
# #     clientes.insert(i,input("Digite o numero do cliente",i,": "))
# # print(clientes)
# # clientes.pop(2)
# # print(clientes)

# numeroCli = int(input("Quantos clientes você gostaria de cadastrar? "))
# vetor = [0 for i in range(numeroCli)]
# for i in range(numeroCli):
#     print(f"\n Digite os dados da pessoa {i}:")
#     nome = input("Nome: ")
#     idade = int(input("Idade: "))
#     sexo = input("Sexo: ")

#     vetor[i] = {
#         "nome" : nome,
#         "idade" : idade,
#         "sexo" : sexo
#     }

# print("\n Lista de Pessoas Cadastradas:")
# for pessoas in vetor:
#     print(pessoas)
# print(vetor[0]["nome"])

from random import randint

computador = randint(0,100)
# print(computador)
Nadivinhou = True
tentatica = 0
while(Nadivinhou):
    digi = int(input("Advinhe o numero: "))
    tentatica+=1
    if(digi<computador):
        print("\nMaior que isso\n")
    elif(digi>computador):
        print("\nMenor que isso\n")
    else:
        print(f"\n!!!!Parabéns você acertou!!!!\n Em {tentatica} tentativas")
        Nadivinhou = False