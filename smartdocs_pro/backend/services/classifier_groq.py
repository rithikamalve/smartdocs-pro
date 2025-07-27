from groq import Groq
from config import load_config

client = Groq(api_key=load_config().get('GROQ_API_KEY'))

def classify(text):
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[
            {
                "role": "user",
                "content": f"Classify this document in one word only:\n{text}"
            }
        ],
        temperature=1,
        max_completion_tokens=128,
        top_p=1,
        stream=False,
        stop=None,
    )
    return completion.choices[0].message.content 