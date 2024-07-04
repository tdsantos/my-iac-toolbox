import json
import pandas as pd

# Abra o arquivo JSON
with open('route53-records.json') as json_file:
    data = json.load(json_file)

# Prepare os dados para o DataFrame
records = []
for record in data['ResourceRecordSets']:
    for rr in record.get('ResourceRecords', []):
        records.append({
            'Name': record['Name'],
            'Type': record['Type'],
            'TTL': record.get('TTL', ''),
            'Value': rr['Value']
        })

# Crie o DataFrame e salve como CSV
df = pd.DataFrame(records)
df.to_csv('route53-records.csv', index=False)
