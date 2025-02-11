## Desafio Técnico - EDS

Este projeto implementa uma pipeline de ETL que utiliza o Airflow via docker para extrair os dados de um banco Oracle, faz o tratamento necessário pedido pelo usuário e os carrega numa nova tabela dentro de um banco Postgre.

## Pré-requisitos
Antes de iniciar, certifique-se de ter os seguintes componentes instalados:

- Python 3+
- Docker (opcional, mas recomendado para rodar o Airflow)
- Oracle Client (necessário para conexão com o Oracle)
- PostgreSQL
- Apache Airflow

## Configuração

### 1. Clonar o repositório

```bash
git clone https://github.com/flavialabanca/Desafio-Tecnico-EDS.git
cd Desafio-Tecnico-EDS
```

### 2. Instalar dependências
Crie um ambiente virtual e instale as dependências:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3. Configurar conexões

Execute o script `config.py` para configurar automaticamente as conexões com o Oracle e PostgreSQL no Airflow:
```bash
python config.py
```

### 4. Executar o Airflow
Caso esteja rodando via Docker:
```bash
docker-compose up -d
```
Caso esteja rodando localmente:
```bash
airflow db init
airflow webserver -p 8080 &
airflow scheduler &
```

Acesse o Airflow via [http://localhost:8080](http://localhost:8080).


### 5. Executar o pipeline
Após configurar as conexões, ative e execute a DAG no Airflow.

## Estrutura do Projeto
```
.
├── scripts/setup_oracle.py  # cria tabela e massa de testes no Oracle
├── createTableOracle.sql  # script SQL para tabela oracle
├── createTablePostgre.sql  # script SQL para criar tabela no PostgreSQL
├── oracle_connection.py   # script para conexão com o banco Oracle
├── dags/
│   ├── etl_pipeline.py  # script principal da DAG
├── scripts/
│   ├── extract.py       # extrai dados do oracle
│   ├── transform.py     # transforma os dados conforme requisito
│   ├── load.py          # carrega os dados no postgre
├── config.py            # configuração das conexões
├── requirements.txt
├── README.md
```

## Logs e Monitoramento
Os logs das execuções podem ser visualizados no Airflow, na aba de "Logs" da DAG.

