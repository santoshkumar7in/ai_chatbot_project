from azure.storage.blob import BlobServiceClient
from datetime import datetime
import os

def save_chat_to_blob(player_id, chat_log):
    blob_conn_str = os.getenv("AZURE_BLOB_CONNECTION_STRING")
    container_name = os.getenv("BLOB_CONTAINER_NAME", "chat-history")

    blob_service = BlobServiceClient.from_connection_string(blob_conn_str)
    container = blob_service.get_container_client(container_name)
    if not container.exists():
        container.create_container()

    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    blob_name = f"{player_id}/chat_{timestamp}.txt"

    blob_client = container.get_blob_client(blob_name)
    blob_client.upload_blob(chat_log, overwrite=True)
