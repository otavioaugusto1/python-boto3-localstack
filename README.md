# Projeto inicial que consiste em criar um Bucket S3 e subir um arquivo "test.txt" nele.


## Estrutura do projeto

localstack-demo/

│

├── app.py

├── requirements.txt

└── test.txt





# Listar serviços disponíveis
```
localstack status services
```

# Ver logs
```
localstack logs
```

# Parar o LocalStack
```
localstack stop
```

# Verificar conteúdo do arquivo:
```
awslocal s3 cp s3://meu-bucket-local/test.txt -
```

# Script Python para imprimir os objetos nos Bucket
```
import boto3

s3_client = boto3.client(
    's3', 
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)
```

# Listar objetos no bucket
```
response = s3_client.list_objects_v2(Bucket='meu-bucket-local')
```
# Imprimir detalhes dos objetos
```
for content in response.get('Contents', []):
    print(f"Arquivo: {content['Key']}, Tamanho: {content['Size']} bytes")
```