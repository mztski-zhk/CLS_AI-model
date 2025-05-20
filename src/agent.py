import getpass
import os

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = "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"

class VoiceAgent:
    def __init__(self):
        self.api_key = os.environ["OPENAI_API_KEY"]
        self.base_url = "https://openrouter.ai/api/v1"
        self.model = "deepseek/deepseek-v3-base:free"
        self.temperature = 0.4
        self.openai_api_key = self.api_key
        self.tools = [
            "stt",
            "tts"
        ]

    def invoke(self):
        from langchain_core.llms import ChatOpenAI
        from stt import SpeechToText
        self.agent = ChatOpenAI(
            api_key=self.openai_api_key,
            tools=self.tools,
            llm=self.llm,
            temperature=self.temperature,
            max_iterations=3,
            return_intermediate_steps=True,
        )

        self.agentwithtools = self.agent.bind_tools([
            self.tools["tts"]
        ])
