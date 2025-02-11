import cx_Oracle

# conexão
DB_USER = "seu_usuario"
DB_PASSWORD = "sua_senha"
DB_DSN = "host:porta/banco"

with open("createTableOracle.sql", "r") as file:
    sql_script = file.read()

# conecta ao Oracle e executa script
try:
    connection = cx_Oracle.connect(DB_USER, DB_PASSWORD, DB_DSN)
    cursor = connection.cursor()
    for statement in sql_script.split(";"):
        if statement.strip():
            cursor.execute(statement)
    connection.commit()
    print("Tabela e dados criados com sucesso no Oracle!")
except Exception as e:
    print(f"Erro ao criar tabela no Oracle: {e}")
finally:
    cursor.close()
    connection.close()

