from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel, Field


import src.stt

# init
import os

import src.tts
if not os.environ.get("OPENAI_API_KEY"):
    api_key = os.environ["OPENAI_API_KEY"] = "11f52000dfbf683a72c0f5743b5bcaa2cfbc3b4789f08b6be2412289e445fafa"

base_url = "https://openrouter.ai/api/v1"
model = "together:meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
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

        try:
            src.tts.TextToSpeech(response)
            os.system("ffplay -nodisp -autoexit -volume 1000 -i 0.wav")
        except FileNotFoundError as e:
            print(f"File not found: {str(e)}")
        except PermissionError as e:
            print(f"Permission error: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
