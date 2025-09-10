from autogen import AssistantAgent, UserProxyAgent, register_function
from tools.player_offer_tool import get_player_offers

# Register function as a tool
@register_function
def get_player_offers_tool(player_id: str) -> str:
    return get_player_offers(player_id)

def create_loyalty_agent():
    assistant = AssistantAgent(
        name="LoyaltySupportAgent",
        llm_config={
            "config_list": [{"model": "gpt-4", "api_key": os.getenv("AZURE_OPENAI_KEY")}],
            "temperature": 0.2,
        },
        system_message="""
        You are a helpful support agent for WindCreek Casino. Your job is to help players
        understand their current loyalty offers. Call `get_player_offers_tool(player_id)` with
        the player’s ID and summarize the offers in a clear, friendly response.
        """
    )
    return assistant
