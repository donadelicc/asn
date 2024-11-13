from azure.storage.blob import BlobServiceClient
import os
import json
from datetime import datetime
from dotenv import load_dotenv


def upload_to_blob_storage(data):
    """Upload JSON data to Azure Blob Storage"""
    load_dotenv()

    try:
        # Get connection string from environment variable
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        if not connect_str:
            raise ValueError("Azure Storage connection string not found")

        # Create the BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        
        # Get container client (create if not exists)
        container_name = "waitlist-data"
        container_client = blob_service_client.get_container_client(container_name)
        if not container_client.exists():
            container_client.create_container()

        # Generate unique blob name using timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        blob_name = f"waitlist_{timestamp}.json"
        
        # Convert data to JSON string
        json_data = json.dumps(data, indent=4)
        
        # Upload to blob storage
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(json_data, overwrite=True)
        
        return True
    except Exception as e:
        print(f"Error uploading to blob storage: {str(e)}")
        return False