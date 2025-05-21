# /src/agent.py
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
import os


class ChatAgent:
    def __init__(self):
        self.base_url = "https://openrouter.ai/api/v1"
        self.model = "together:meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
        self.temperature = 0.6
        if not os.environ.get("OPENAI_API_KEY"):
            self.api_key = os.environ["OPENAI_API_KEY"] = "11f52000dfbf683a72c0f5743b5bcaa2cfbc3b4789f08b6be2412289e445fafa"

    def base_model():
        return init_chat_model(
            api_key=self.api_key,
            model=self.model,
            temperature=self.temperature,
        )
    
    def chat_agent():
        return create_react_agent(
            model=self.base_model(),
            tools=[],
            prompt=f"""
You are a meditation assistant. You have to summarize and enhance the text given to you and give clear and friendly instructions to the user.
The text is about meditation.
{"text"}
You have to respond with user input of "yes" or "no" and if the user input is "yes", you have to continue to help the user meditate else you have to say "FALSE" and do not give any other information.
Please check the current step is correct and if not, please just say "FALSE" and do not give any other information.
The current step is {{step+1}}.
Answer without structured data, just answer in one paragraph.
"""
)
    def speech_agent():
        return create_react_agent(
            model=self.base_model(),
            tools=[],
            prompt=f"""
You are a meditation assistant. You have to give a simple conversation to help the user meditate. Please refer to the steps to do meditation below and generate a simple conversation for each step.:
The current step is {{step+1}}.
1:A greeting to the user.
2.Close your eyes and take a deep breath.
3.Hear the white noise around you and try to focus on it.
4.Continue to breathe deeply and let go of any tension in your body.
5.Imagine a peaceful place and visualize it in your mind which allow yourself to relax and enjoy the moment.
6.The end of the meditation session.
The user input will be "yes" or "no" and if the user input is "yes", you have to continue your work else you have to say "FALSE" and do not give any other information.
Answer without structured data, just answer in one paragraph.
"""
)
