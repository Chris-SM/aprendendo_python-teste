import mysql.connector

coneccao = mysql.connector.connect(host='localhost',database='db_cliente',user='root',password="root")
permitido = True
while permitido:
    cnpj = input("Digite o numero do cnpj que deseja deletar: ")
    if cnpj.__len__()==14:
        permitido = False
    else:
        print("Tem que ter 14 digitos!!!>:(")

deletar = f"delete from tb_cliente where nr_cnpj = '{cnpj}';"


cursor = coneccao.cursor()
cursor.execute(deletar)
coneccao.commit()
print("Deletado com sucesso")