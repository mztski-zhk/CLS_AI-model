import sounddevice as sd
import numpy as np
import whisper
import time
import threading

class SpeechToText:
    def __init__(self, model_name="base", language="en"):
        self.language = language
        self.model = model_name if model_name == "large" else model_name + ".en"
        self.sample_rate = 16000
        self.channels = 1
        self.recode_duration = 8

    def loadwhisper(self):
        try:
            print("Loading Whisper model...")
            self.model = whisper.load_model(self.model)
            print("Model loaded successfully.")
            return self.model
        
        except Exception as e:
            print(f"Error loading model: {e}")
            exit()
    
    def record_audio(self):
        print("Recording audio...")
        try:
            recording = sd.rec(
                int(self.recode_duration * self.sample_rate), 
                samplerate=self.sample_rate,
                channels=self.channels,
                dtype='float32'
            )
            sd.wait()
            print("Recording finished.")
            return recording
        
        except Exception as e:
            print(f"Error during transcription: {e}")
            return f"Error during transcription: {e}"
        
    def transcribe_audio(self):
        if self.audio_input is None:
            return "Error: No audio to transcribe."

        try:
            print("Transcribing audio...")
            audio_np = np.squeeze(self.audio_input)
            result = self.model.transcribe(audio_np, language=self.language)
            return result["text"]

        except Exception as e:
            print(f"Error during transcription: {e}")
            return f"Error during transcription: {e}"
        
    def flow(self):
        # load whisper model
        self.loadwhisper()
        
        # record audio
        self.audio_input = self.record_audio()
        if self.audio_input is not None:
            # Transcribe audio to text
            self.user_text = self.transcribe_audio()
            if self.user_text and not self.user_text.startswith("Error:"):
                return self.user_text
        return None
