from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import os

def get_player_offers(player_id: str) -> str:
    """Fetches active loyalty offers for a player using Azure AI Search."""
    service_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
    index_name = os.getenv("AZURE_SEARCH_INDEX")
    key = os.getenv("AZURE_SEARCH_KEY")

    search_client = SearchClient(service_endpoint, index_name, AzureKeyCredential(key))

    results = search_client.search(search_text=f"*", filter=f"playerId eq '{player_id}' and status eq 'active'")

    offers = []
    for result in results:
        offers.append(f"{result['offerType']} - {result['amount']} (valid until {result['validUntil']})")

    return "\n".join(offers) if offers else "You currently have no active loyalty offers."
