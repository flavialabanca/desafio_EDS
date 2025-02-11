import psycopg2
from psycopg2 import sql

# Configurar os parâmetros de conexão
DB_PARAMS = {
    "dbname": "seu_banco",
    "user": "seu_usuario",
    "password": "sua_senha",
    "host": "localhost",
    "port": 5432
}

# Definir o SQL para criar a tabela
CREATE_TABLE_SQL = """
create table ANALYTICS_TRANSACTIONS (
    TRANSACTION_ID integer PRIMARY KEY,
    CUSTOMER_ID integer not null,
    AMOUNT numeric(10,2) not null,
    TRANSACTION_DATE date,
    CATEGORY TEXT
);
"""

# Conectar ao banco e criar a tabela
def create_table():
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        cur.execute(CREATE_TABLE_SQL)
        conn.commit()
        cur.close()
        conn.close()
        print("Tabela criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar a tabela: {e}")

if __name__ == "__main__":
    create_table()

