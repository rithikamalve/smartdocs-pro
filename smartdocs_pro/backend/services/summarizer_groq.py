from groq import Groq
from config import load_config

# Load Groq API client with your key from .env
client = Groq(api_key=load_config().get('GROQ_API_KEY'))

def summarize(text):
    # Call Groq with a summarization-capable model
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[
            {
                "role": "user",
                "content": f"Summarize this document clearly and concisely:\n{text}"
            }
        ],
        temperature=0.5,
        max_completion_tokens=1024,
    )
    # Return the summarized text
    return completion.choices[0].message.content
