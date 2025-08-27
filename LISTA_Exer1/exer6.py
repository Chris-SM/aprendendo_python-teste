num1 = int(input('Digite sua idade: '))

if num1<16:
    print(f"não vota")
elif num1<18 or num1>65:
    print(f"voto opcional")
else:
    print(f"voto obrigatório")

