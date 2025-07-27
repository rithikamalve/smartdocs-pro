from groq import Groq
from config import load_config

client = Groq(api_key=load_config().get('GROQ_API_KEY'))

SUPPORTED_LANGUAGES = ["fr", "de", "es", "it", "pt", "nl", "sv", "pl", "ja", "ko"]  # Add your full list

def translate_text(text, target_lang):
    if target_lang not in SUPPORTED_LANGUAGES:
        raise Exception(f"Unsupported target language: {target_lang}")
    
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[
            {
                "role": "user",
                "content": f"Translate the following text to {target_lang}. Only provide the translated text without any explanation or formatting:\n\n{text}"
            }
        ],
        temperature=0.3,
        max_completion_tokens=1024,
    )
    return {
        "translation": completion.choices[0].message.content.strip()
    }
