import mysql.connector

coneccao = mysql.connector.connect(host='localhost',user='root',password="root")

criar_banco = """create database if not exists db_cliente"""
cursor = coneccao.cursor()
cursor.execute(criar_banco)

coneccao = mysql.connector.connect(host='localhost',database='db_cliente',user='root',password="root")


criar_tabela = [
    """create table if not exists tb_cliente(
          nr_cnpj char(14) primary key,
          nm_razao_social varchar(30) not null,
          nm_pais varchar(20),
          nm_email varchar(40) not null 
        );""",

    """create table if not exists tb_produto(
          cd_produto int auto_increment primary key,
          nm_produto varchar(25) not null,
          vl_unitario decimal(5,2) not null 
        );""",

    """create table if not exists tb_nota(
          cd_nota int auto_increment primary key,
          dt_emissao date not null,
          dt_envio date not null,
          vl_total decimal(6,2),
          fk_nr_cnpj char(14),
          foreign key (fk_nr_cnpj) references tb_cliente (nr_cnpj)
        );""",
        
    """create table if not exists tb_item(
          cd_item int auto_increment primary key,
          qt_produto int not null,
          vl_total_item decimal(5,2),
          fk_cd_produto int,
          fk_cd_nota int,
          foreign key (fk_cd_produto) references tb_produto (cd_produto),
          foreign key (fk_cd_nota) references tb_nota (cd_nota)
        );"""
                ]


cursor = coneccao.cursor()
for tabela in criar_tabela:
    cursor.execute(tabela)
    print("Tabela criado com sucesso")