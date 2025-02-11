# extract.py - extração dos dados Oracle

import cx_Oracle
import pandas as pd
from config import DB_CONFIG

# Criar uma função que conecta ao Oracle e faz a query na tabela SALES_TRANSACTIONS.
# Retornar os dados como um pandas.DataFrame (ou outro formato que facilite as transformações).


def extract_data():
    try:
        # Criando a string de conexão (DSN)
        dsn = cx_Oracle.makedsn(DB_CONFIG["host"], DB_CONFIG["port"], service_name=DB_CONFIG["service"])

        # Criando a conexão com Oracle
        conn = cx_Oracle.connect(DB_CONFIG["user"], DB_CONFIG["password"], dsn)

        # Cria DataFrame a partir do select
        query = "SELECT * FROM SALES_TRANSACTIONS"
        df = pd.read_sql(query, conn)

        conn.close()

        return df

    except cx_Oracle.DatabaseError as e:
        print("Erro na conexão com Oracle:", e)
        return None

# Teste de extração
if __name__ == "__main__":
    data = extract_data()
    if data is not None:
        print(data.head())  # Exibir as primeiras linhas
    else:
        print("Erro na extração dos dados.")











