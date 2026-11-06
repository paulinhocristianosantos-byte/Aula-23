import mysql.connector 
import pandas as pd 
from mysql.connector import Error

try:
    conexao = mysql.connector.connect(
        host='localhost', #ou IP do servidor 
        user='root',
        password='',
        database='escola'
    )
    if conexao.is_connected():
        print("Conectado com Sucesso!")

    #cria um cursor (objeto q permite executar comandos)
    cursor = conexao.cursor()

    #executa uma consulta 
    cursor.execute("SELECT * FROM aluno LIMIT 5")

    #busca resultados 
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)


except Error as e:
   print(f"Erro ao conectar ou executar: {e}")

finally:

    #fecha o cursor (se ja foi criado)
    if 'cursor' in locals():
        try:
            cursor.close()
        except Exception: 
            pass # se já estiver fechado ou ocorrer erro, ignore 
# fecha a conexao (se ja foi criada e ainda etá conectada)
if 'conexao' in locals() and conexao.is_connected():
    conexao.close()
    print("Conexão encerrada")
    
    

    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão Encerrada")


