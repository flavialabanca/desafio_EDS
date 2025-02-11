# transform.py - transformação dos dados segundo o requisito

def transform_data(data):
    transformed_data = []
    for row in data:
        # Excluir registros onde AMOUNT <= 0.
        # (só trata os maiores | mais ágil | menores não serão gravados)
        if row["AMOUNT"] > 0:  
          
            #Normalizar a coluna CUSTOMER_ID para letras maiúsculas.
            row["CUSTOMER_ID"] = row["CUSTOMER_ID"].upper()
            
            # Adicionar uma nova coluna chamada CATEGORY, categorizando os valores da transação
            if row["AMOUNT"] < 100:
                row["CATEGORY"] = "LOW"
            elif 100 <= row["AMOUNT"] <= 500:
                row["CATEGORY"] = "MEDIUM"
            else:
                row["CATEGORY"] = "HIGH"
            
            transformed_data.append(row)
    return transformed_data
