import os 
import pandas as pd
from google.cloud import storage

credential_path = rf"C:\Users\dougl\Desktop\Pessoal\Estudos\Portfólio\exalted-breaker-455520-m1-c0df463a5449.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

base = pd.read_csv(rf'C:\Users\dougl\Desktop\Pessoal\Estudos\Portfólio\perfume-e-commerce-dataset-2024\ebay_mens_perfume.csv')

df = pd.DataFrame(base)
print(df.head())

df.to_parquet(rf'C:\Users\dougl\Desktop\Pessoal\Estudos\Portfólio\perfume-e-commerce-dataset-2024\ebay_mens_perfume.parquet')

def upload_files_to_gcs(parquet_file_path, bucket_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(parquet_file_path)
    print(f"File {parquet_file_path} uploaded to {destination_blob_name}")

parquet_file_path = rf'C:\Users\dougl\Desktop\Pessoal\Estudos\Portfólio\perfume-e-commerce-dataset-2024\ebay_mens_perfume.parquet'    
bucket_name = 'dbportfoliodoug'
destination_blob_name = 'Perfumes_dataset/ebay_mens_perfume.parquet'

upload_files_to_gcs(parquet_file_path, bucket_name, destination_blob_name)