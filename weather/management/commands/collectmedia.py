# your_app/management/commands/collectmedia.py

import os
from django.core.management.base import BaseCommand
from azure.storage.blob import BlobServiceClient, BlobClient, ContentSettings

from pathlib import Path
from dotenv import load_dotenv
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = settings.BASE_DIR
dotenv_path = os.path.join(BASE_DIR, 'utility', '.env')

SA_CON = os.getenv('AZURE_SA_CON')

print(SA_CON)
class Command(BaseCommand):
    help = 'Collect media files from local directory and upload to Azure Blob Storage'

    def handle(self, *args, **kwargs):
        local_media_directory = BASE_DIR / 'media'
        
        connection_string = SA_CON
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client('appmedia')
    
        for root, dirs, files in os.walk(local_media_directory):
                for file_name in files:
                    local_file_path = os.path.join(root, file_name)
                    azure_file_path = f"{file_name}"  # Adjust this path in Azure as needed

                    with open(local_file_path, "rb") as data:
                
                        blob_client = container_client.get_blob_client(azure_file_path)
         
                        blob_client.upload_blob(data, overwrite=True)

                    self.stdout.write(self.style.SUCCESS(f"Uploaded {file_name} to Azure Blob Storage"))

            
