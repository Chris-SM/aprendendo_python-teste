import mysql.connector

coneccao = mysql.connector.connect(host='localhost',database='db_cliente',user='root',password='root')

criar_tabela = """create table tb_cliente(
                    nr_cnpj char(14) primary key,
                    nm_razao_social varchar(35) not null,
                    nm_pais varchar(20),
                    nm_email varchar(40) not null
                );
"""

cursor = coneccao.cursor()
cursor.execute(criar_tabela)
print("Tabela criado com sucesso")