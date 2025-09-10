import os
import json
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from datetime import datetime

def log_chat_event(player_id, query, response):
    conn_str = os.getenv("AZURE_SERVICE_BUS_CONNECTION_STRING")
    queue_name = os.getenv("SERVICE_BUS_QUEUE_NAME")

    message_body = {
        "timestamp": datetime.utcnow().isoformat(),
        "playerId": player_id,
        "query": query,
        "response": response,
        "eventType": "LoyaltyOfferQuery"
    }

    with ServiceBusClient.from_connection_string(conn_str) as client:
        sender = client.get_queue_sender(queue_name)
        sender.send_messages(ServiceBusMessage(json.dumps(message_body)))
