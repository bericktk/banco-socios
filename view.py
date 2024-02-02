# importandoo SQLite
import sqlite3 as lite

#criando a conexao com o banco
con = lite.connect('dados.db')

#Inserir dados
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO socios(nome, empresa, descricao, marca, data_de_associacao, valor_mensalidade, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query,i)

# Atualizar os dados
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE socios SET nome=?, empresa=?, descricao=?, marca=?, data_de_associacao=?, valor_mensalidade=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query,i)

# Deletar dados
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM socios WHERE id=?"
        cur.execute(query,i)

# Ver dados
def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM socios"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados

# Ver dados individual
def ver_item(id):
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM socios WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)