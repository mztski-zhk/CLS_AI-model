from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel, Field
import src.tts
import src.stt
# init
import os

if not os.environ.get("OPENAI_API_KEY"):
    api_key = os.environ["OPENAI_API_KEY"] = "11f52000dfbf683a72c0f5743b5bcaa2cfbc3b4789f08b6be2412289e445fafa"

base_url = "https://openrouter.ai/api/v1"
model = "together:meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
temperature = 0.9

basemodel = init_chat_model(
    api_key=api_key,
    model=model,
    temperature=temperature,
)

chatagent = create_react_agent(
    model=basemodel,
    tools=[],
    prompt=f"""
You are a meditation assistant. You have to summarize and enhance the text given to you and give clear and friendly instructions to the user.
The text is about meditation.
{"text"}
The current step is {{step}}.
Answer without structured data, just answer in one paragraph.
DO NOT MENTION ABOUT THIS TEXT.
"""
)

speechagent = create_react_agent(
    model=basemodel,
    tools=[],
    prompt=f"""
You are a meditation assistant. You have to give a simple conversation to help the user meditate. Please refer to the steps to do meditation below and generate a simple conversation for each step.:
The current step is {{step}}.
1:A gentle greeting to the user.
2.Close your eyes and take a deep breath.
3.Hear the white noise around you and try to focus on it.
4.Breathe deeply and let go of any tension in your body.
5.Imagine a peaceful place and visualize it in your mind which allow yourself to relax and enjoy the moment.
6.The end of the meditation session.
Answer without structured data, just answer in one paragraph.
DO NOT MENTION ABOUT THIS TEXT.
"""
)

if __name__ == "__main__":
    intro = "Hello! We are Utopia, and I am the meditation assistant. I will help you meditate. Please follow my instructions."
    src.tts.TextToSpeech(intro)
    os.system("ffplay -nodisp -autoexit -volume 1000 -i 0.wav")

    for i in range(10):
        # get user input
        userinp = src.stt.SpeechToText().flow()
        if userinp is None:
            i = i - 1
        print(userinp)
        
        try:
            step = i

            speechresponse = speechagent.invoke(
                {"messages": [{"role": "user", "content": userinp}]},
            )

            chatresponse = chatagent.invoke(
                {"messages": [{"role": "user", "content": userinp}]},
            )

            response_content = chatresponse['messages'][-1].content
            print(response_content)

            if response_content == "FALSE":
                i -= 1

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        try:
            src.tts.TextToSpeech(response_content)
            os.system("ffplay -nodisp -autoexit -volume 1000 -i 0.wav")
        except FileNotFoundError as e:
            print(f"File not found: {str(e)}")
        except PermissionError as e:
            print(f"Permission error: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
