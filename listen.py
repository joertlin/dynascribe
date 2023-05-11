import os
import time
import sys
import keyboard
import json
import requests

import config
import openai

def listener(directory):
    while True:
        # Break the loop if 'q' is pressed
        if keyboard.is_pressed('q'):
            print("Stopping listener...")
            break

        for file in os.listdir(directory):
            if file.endswith(".wav"):
                wav_file = file
                wav_path = os.path.join(directory, wav_file)
                
                json_file = update_ext(file)
                json_path = os.path.join(directory, json_file)
                
                updated_size = 0
                size = -1

                if not os.path.exists(json_path):
                    print("Found a file")
                    while size!=updated_size:
                        size = updated_size
                        print("Size: %0f"%size)
                        time.sleep(5)
                        updated_size = os.path.getsize(wav_path)

                    print("File is ready for transcription.")
                    transcription = transcribe(directory, wav_file)
                    query = format_query_text(transcription)

                    r = openai_chat(query, OPENAI_LLM_MODEL)
                    content = r["choices"][0]["message"]["content"].replace('"', '')
                    tags_and_content = DYNALIST_TAGS + [content]
                    formatted_content = " ".join(tags_and_content)

                    bundle = {
                        "raw_transcritpion":transcription,
                        "query":query,
                        "content":formatted_content
                    }
                    to_json(bundle, os.path.join(directory, json_file))
                    result = add_to_dynalist_inbox(bundle["content"], DYNALIST_KEY)

                    print("Transcription complete. Searching for nextfile.")

        # Wait for a short interval before checking the directory again
        time.sleep(5)

def transcribe(directory, wav_file):
    wav_path = os.path.join(directory, wav_file)
    json_file = update_ext(wav_file)

    print(f"Processing {wav_file}...")
    audio_file= open(wav_path, "rb")
    transcription = openai.Audio.transcribe("whisper-1", audio_file)
    transcription = transcription['text']

    #print(transcript)
    #transcriptions = asr_model.transcribe([wav_path])
    #transcription = transcriptions[0]
    print("Transcription:\n  %s"%transcription)

    return transcription
    
def openai_chat(query_content, llm_model, query_role="user"):
    r = openai.ChatCompletion.create(
        model=llm_model, 
        messages=[{'role': query_role, 'content': query_content}],
        temperature=0,
        stream=False
    )
    
    return r

def format_query_text(transcription):
    return OPENAI_ASSISTANT_SETUP + transcription

def to_json(package, json_file_path):
    with open(json_file_path, 'w') as file:
        json.dump(package, file, indent=4)

def update_ext(filename, new_extension=".json"):
    updated_file_extension = os.path.splitext(filename)[0] + new_extension
    
    return updated_file_extension

def add_to_dynalist_inbox(content, token):
    url = 'https://dynalist.io/api/v1/inbox/add'
    headers = {'Content-Type': 'application/json'}
    data = {
        'token': token,
        'content': content
    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python listen.py <directory_path>")
        sys.exit(1)

    openai.api_key = config.OPENAI_API_KEY
    OPENAI_ASSISTANT_SETUP = config.OPENAI_ASSISTANT_SETUP
    OPENAI_LLM_MODEL = config.OPENAI_LLM_MODEL
    
    DYNALIST_KEY = config.DYNLIST_API_KEY
    DYNALIST_TAGS = config.DYNALIST_TAGS
    
    directory = sys.argv[1]

    print(f"Listening for .wav files in {directory}... Press Ctrl+C to stop.")
    listener(directory)