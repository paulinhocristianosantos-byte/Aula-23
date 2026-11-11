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

    #define a query de INSERT usando placeholders (%s)
    sql = "INSERT INTO aluno (nome, cpf, data_nascimento, email, telefone, data_matricula, id_curso) VALUES (%s, %s, %s, %s, %s, %s, %s)"

# valores q serão substituidos nos placeholders, na mesma ordem 
    valores = ("joana", "11122253344", "2005-04-21", "joana@email.com", "21911110002", "2026-02-07", "1")

#executa o INSERT no banco, substiuindo os %s pelos valores em "valores"
#o connector trata automaticamente aspas, datas e acentos 

    cursor.execute(sql, valores)

#confirma (grava) as alterações da transação no banco 
# sem commit(), o insert ficaria só na memoria e seria descartado 
    conexao.commit()

#mostra o id (AUTO_INCREMENT) gerado na ultima inserção 
    print(f"Linha inserida. ID gerado: {cursor.lastrowid}")

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


