#test.py

from extract import extract_data
from transform import transform_data
from load import load_data

# Execução de teste
if __name__ == "__main__":
    print("Iniciando teste do pipeline ETL...\n")

    raw_data = extract_data()
    print(f"Dados extraídos:\n{raw_data}\n")

    transformed_data = transform_data(raw_data)
    print(f"Dados transformados:\n{transformed_data}\n")

    load_data(transformed_data)
    print("\nPipeline de teste concluído!")

