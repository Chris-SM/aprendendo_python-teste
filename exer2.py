# num1 = int(input("Qual tabuada gostaria de ver?  "))

# ate = int(input("Ate qual numero? "))
# x=0
# while x < (ate+1):
#     print(f"{num1} X {x} = {num1*x}")
#     x+=1


x = int(input("Qual tabuada gostaria de ver?  "))
while x != 0:
    y=0
    while y < 11:
        print(f"{x} X {y} = {x*y}")
        y+=1
    x = int(input("Qual tabuada gostaria de ver agora?  "))