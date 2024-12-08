import boto3
from botocore.exceptions import ClientError
from decouple import config

def create_bucket(bucket_name):
    """Cria um bucket no LocalStack S3"""
    s3_client = boto3.client(
        's3', 
        endpoint_url='http://localhost:4566',  # URL padrão do LocalStack
        aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'),
        region_name='us-east-1'
    )
    
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} criado com sucesso!")
    except ClientError as e:
        print(f"Erro ao criar bucket: {e}")
    
def upload_file(file_name, bucket_name):
    """Faz upload de um arquivo para o bucket"""
    s3_client = boto3.client(
        's3', 
        endpoint_url='http://localhost:4566',
        aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'),
        region_name='us-east-1'
    )
    
    try:
        s3_client.upload_file(file_name, bucket_name, file_name)
        print(f"Arquivo {file_name} enviado para {bucket_name}")
    except ClientError as e:
        print(f"Erro ao fazer upload: {e}")

def main():
    bucket_name = 'meu-bucket-local'
    
    # Cria o bucket
    create_bucket(bucket_name)
    
    # Faz upload de um arquivo
    upload_file('test.txt', bucket_name)

if __name__ == '__main__':
    main()
