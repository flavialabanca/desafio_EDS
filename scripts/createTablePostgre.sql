--- cria tabela postgre para carga

create table ANALYTICS_TRANSACTIONS (
    TRANSACTION_ID integer PRIMARY KEY,
    CUSTOMER_ID integer not null,
    AMOUNT numeric(10,2) not null,
    TRANSACTION_DATE date,
    CATEGORY TEXT
);

