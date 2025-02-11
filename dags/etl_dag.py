from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator
from datetime import datetime
from etl_pipeline.extract import extract_data
from etl_pipeline.transform import transform_data
from etl_pipeline.load import load_data

@dag(
    start_date=datetime(2025, 2, 10),
    schedule="0 0 * * *",  # Executa diariamente à meia-noite (00:00 UTC)
    catchup=False,
    doc_md="""
    ## DAG - Desafio EDS
    Executa pipeline ETL com extração dos dados da tabela Oracle,
    transformação e carregamento dos dados no PostgreSQL.
    """
)
def dag_desafio_eds():
    start = EmptyOperator(task_id="start")
    
    @task()
    def extract_task():
        data = extract_data()
        if not data:
            raise ValueError("Falha na extração dos dados.")
        return data
    
    @task()
    def transform_task(data):
        transformed_data = transform_data(data)
        if not transformed_data:
            raise ValueError("Nenhum dado válido para carga!")
        return transformed_data
        
    @task()
    def load_task(transformed_data):
    try:
        load_data(transformed_data)
        print("Carga finalizada com sucesso!")
    except Exception as e:
        print(f"Erro na carga: {e}")
        raise ValueError("A carga dos dados falhou. Verifique os logs para mais detalhes.")

    end = EmptyOperator(task_id="end")
    
    # Definição do fluxo das tasks
    raw_data = extract_task()
    transformed_data = transform_task(raw_data)
    load_task(transformed_data)

    start >> raw_data >> transformed_data >> load_task(transformed_data) >> end

# Instancia a DAG
criar_DAG = dag_desafio_eds()

