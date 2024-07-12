#!/usr/bin/env python
# coding: utf-8

# In[20]:


import speech_recognition as sr
from gtts import gTTS
import pygame
from io import BytesIO

# Initialize recognizer class (for recognizing speech)
recognizer = sr.Recognizer()

# Function to convert speech to text
def speech_to_text():
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
    
    return ""

# Function to convert text to speech and play using pygame
def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Main function to execute speech-to-text and text-to-speech
def main():
    # Speech to text
    input_text = speech_to_text()
    
    # Text to speech
    if input_text:
        text_to_speech(input_text)

if __name__ == "__main__":
    main()


# In[ ]:




