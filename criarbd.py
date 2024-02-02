# Importando SQLite
import sqlite3 as lite

# criando conexão
con = lite.connect('dados.db')

# criando as tabelas
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE socios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, empresa TEXT, descricao TEXT, marca TEXT, data_de_associacao DATE, valor_mensalidade DECIMAL, serie TEXT, imagem TEXT)")
    