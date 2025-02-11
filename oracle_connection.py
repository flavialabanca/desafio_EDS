import cx_Oracle

# configura conexão oracle
HOST = "host_name"
PORT = 1521
SERVICE_NAME = "service_name"
USER = "user"
PASSWORD = "password"

# Criando a conexão
dsn = cx_Oracle.makedsn(HOST, PORT, service_name=SERVICE_NAME)
conn = cx_Oracle.connect(user=USER, password=PASSWORD, dsn=dsn)

print("Conexão com Oracle bem-sucedida!")

conn.close()

