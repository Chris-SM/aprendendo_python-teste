import mysql.connector

coneccao = mysql.connector.connect(host='localhost',database='db_cliente',user='root',password="root")
permitido = True
while permitido:
    cnpj = input("Digite o numero do cnpj: ")
    if cnpj.__len__()==14:
        permitido = False
    else:
        print("Tem que ter 14 digitos!!!>:(")

razao = input("Digite o numero do razao social: ")
pais = input("Digite o nome do pais: ")
email = input("Digite o numero do email: ")

inserir = f"insert into tb_cliente values('{cnpj}','{razao}','{pais}','{email}')"


print(inserir)

cursor = coneccao.cursor()
cursor.execute(inserir)
coneccao.commit()
print("Tabela criado com sucesso")