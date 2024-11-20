import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    endpoint = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT")
    api_key = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_KEY")
    az_storage_connection_string = os.getenv("AZURE_STORAGE_ACCOUNT_CONNECTION_STRING")
    container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

