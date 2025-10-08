import mysql.connector

coneccao = mysql.connector.connect(host='localhost',database='db_cliente',user='root',password="root")
permitido = True
while permitido:
    cnpj = input("Digite o numero do cnpj que deseja mudar: ")
    if cnpj.__len__()==14:
        permitido = False
    else:
        print("Tem que ter 14 digitos!!!>:(")

razao = input("Digite a nova razão social: ")

mudar = f"update tb_cliente set nm_razao_social = '{razao}' where nr_cnpj = '{cnpj}'"


cursor = coneccao.cursor()
cursor.execute(mudar)
coneccao.commit()
print("Atualizado com sucesso")