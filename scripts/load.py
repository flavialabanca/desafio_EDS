import psycopg2
from config import PG_CONFIG

def load_data(data):
    try:
        # Criando a conexão com PostgreSQL
        conn = psycopg2.connect(
            host=PG_CONFIG["host"],
            port=PG_CONFIG["port"],
            database=PG_CONFIG["database"],
            user=PG_CONFIG["user"],
            password=PG_CONFIG["password"]
        )
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO ANALYTICS_TRANSACTIONS (TRANSACTION_ID, CUSTOMER_ID, AMOUNT, TRANSACTION_DATE, CATEGORY)
        VALUES (%s, %s, %s, %s, %s)
        """

        # Carrega dados
        for row in data:
            cursor.execute(insert_query, (
                row["TRANSACTION_ID"],
                row["CUSTOMER_ID"],
                row["AMOUNT"],
                row["TRANSACTION_DATE"],
                row["CATEGORY"]
            ))

        # Confirmando as inserções
        conn.commit()
        print("Dados carregados com sucesso na tabela ANALYTICS_TRANSACTIONS.")

        # Fechando conexão
        cursor.close()
        conn.close()

    except psycopg2.DatabaseError as e:
        print("Erro ao conectar ou carregar os dados:", e)


