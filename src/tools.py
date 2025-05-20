# /src/tools.py
from tts import TextToSpeech
from stt import SpeechToText
from langchain_core.tools import tool

class tools():
    def __init__(self):
        self.tools = {
            "tts": TextToSpeech(),
        }

    @tool
    def tts(self,text):
        return self.tools["tts"]
    