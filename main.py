from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent

import src.stt

# init
import os
if not os.environ.get("OPENAI_API_KEY"):
    api_key = os.environ["OPENAI_API_KEY"] = "11f52000dfbf683a72c0f5743b5bcaa2cfbc3b4789f08b6be2412289e445fafa"

base_url = "https://openrouter.ai/api/v1"
model = "together:deepseek-ai/Deepseek-R1-Distill-Llama-70B-free"
temperature = 0.4

basemodel = init_chat_model(
    api_key=api_key,
    model=model,
    temperature=temperature,
)

chatagent = create_react_agent(
    model=basemodel,
    tools=[],
    prompt="""
You are a helpful assistant.
"""
)

promptagents = create_react_agent(
    model=basemodel,
    tools=[],
    prompt="""
You are a helpful assistant.
"""
)

if __name__ == "__main__":
    for i in range(4):
        # get user input
        userinp = src.stt.SpeechToText().flow()
        if userinp is None:
            i = i - 1
        print(userinp)
        
        try:
            agent = chatagent
            response = agent.invoke(
                {"messages": [{"role": "user", "content": userinp}]}
            )

            print(response)
        except Exception as e:
            print(f"An error occurred: {str(e)}")