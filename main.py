# 13 inno design macbook

from pydantic import BaseModel, Field
import src.tts
import src.stt
import src.agent
import os
if __name__ == "__main__":
    introducton = """
Hello! We are Utopia, and I am a meditation assistant. I will help you meditate and guide you through the process.
"""
    src.tts.TextToSpeech(introducton)
    os.system("ffplay -nodisp -autoexit -volume 1000 -i 0.wav")

    for i in range(6):
        # get user input
        userinp = src.stt.SpeechToText().flow()
        if userinp is None:
            i = i - 1
        print(userinp)
        
        try:
            step = i

            speechresponse = src.agent.ChatAgent.speech_agent().invoke(
                {"messages": [{"role": "user", "content": userinp}]},
            )

            chatresponse = src.agent.ChatAgent.chat_agent().invoke(
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
