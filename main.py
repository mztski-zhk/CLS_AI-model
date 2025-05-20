import src.agent
import src.stt
from threading import Timer, start
import time
import src.tools

if __name__ == "__main__":
    agent = src.agent.VoiceAgent(
    # Initialize the speech-to-text tool
    speech_to_text = Timer(8.0, src.stt.SpeechToText)
    prompt = speech_to_text.start()

    run_agent = agent.invoke(
        message=(
            [
                ("system", "You are a helpful assistant."),
                ("user", prompt),
            ],
        )
    )
)