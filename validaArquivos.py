import boto3

s3_client = boto3.client(
    's3', 
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

# Listar os objetos do bucket
response = s3_client.list_objects_v2(Bucket='meu-bucket-local')

# Imprimir os objetos caso existam
for content in response.get('Contents', []):
    print(f"Arquivo: {content['Key']}, Tamanho: {content['Size']} bytes")