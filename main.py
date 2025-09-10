from agents.loyalty_offer_agent import create_loyalty_agent
from autogen import UserProxyAgent

def main():
    assistant = create_loyalty_agent()

    user = UserProxyAgent(name="User", human_input_mode="TERMINAL")
    
    user.initiate_chat(
        assistant,
        message="What are my loyalty offers?",
        summary_method="last_msg"
    )

if __name__ == "__main__":
    main()
