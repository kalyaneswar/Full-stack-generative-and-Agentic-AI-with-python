from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("gemini_api_key"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
    
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    
    messages=[
        {"role" : "system", "content": "You are expert in maths and only answer maths related stuff. if any other don't respond"},
        {"role": "user", "content": "can u pls help me to solve a + b whole square?"}        
    ]
)

print(response.choices[0].message.content)
# print(response.choices[0].message)