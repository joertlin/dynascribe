# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import config

openai.api_key = config.OPENAI_API_KEY
audio_file= open(r"C:\Users\blaze\Videos\2023-05-11 08-46-46.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript['text'])