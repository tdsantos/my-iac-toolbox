Use o seguinte comando para exportar os registros DNS da sua zona hospedada para um arquivo JSON:

aws route53 list-resource-record-sets --hosted-zone-id ZONE_ID --output json > route53-records.json

Substitua ZONE_ID pelo ID da sua zona hospedada.

Passo 2: Converter JSON para CSV

Use Python para converter o arquivo JSON exportado para um arquivo CSV.

1. Instalar Pandas
Certifique-se de ter o Python instalado, juntamente com a biblioteca pandas. Instale pandas com o comando:

pip install pandas

2. Script Python para Converter JSON para CSV
Salve o seguinte script Python em um arquivo, por exemplo, json_to_csv.py:

import json
import pandas as pd

# Abra o arquivo JSON
with open('route53-records.json') as json_file:
    data = json.load(json_file)

# Prepare os dados para o DataFrame
records = []
for record in data['ResourceRecordSets']:
    for rr in record.get('ResourceRecords', [{'Value': ''}]):
        records.append({
            'Name': record['Name'],
            'Type': record['Type'],
            'TTL': record.get('TTL', ''),
            'Value': rr['Value']
        })

# Crie o DataFrame e salve como CSV
df = pd.DataFrame(records)
df.to_csv('route53-records.csv', index=False)


3. Executar o Script
Execute o script com o comando:

python json_to_csv.py

Isso criará um arquivo route53-records.csv no mesmo diretório.
