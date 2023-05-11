OPENAI_API_KEY = ""
DYNLIST_API_KEY = ""

# App setups
## NeMo
NEMO_ASR_MODEL="QuartzNet15x5Base-En"

## OPENAI
OPENAI_LLM_MODEL = "gpt-3.5-turbo"

## Dynalist
DYNALIST_TAGS = ["#scribe"]

# Test setups
OPENAI_ASSISTANT_SETUP = "You are a transcription assistant. I will give you an unformatted "
OPENAI_ASSISTANT_SETUP += "text string, and you will return the string formatted with "
OPENAI_ASSISTANT_SETUP += "punctionation and likely misspelled words corrected. Interpret the word "'hashtag'" as the symbol #:"
TEST_TRANSCRIPTION = "this is a recording we are testing a python library called nemo hello world"