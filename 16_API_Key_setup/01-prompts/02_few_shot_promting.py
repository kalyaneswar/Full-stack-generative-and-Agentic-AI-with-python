# few shot promting
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("gemini_api_key"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
    
)

SYSTEM_PROMT = """
You are expert in coding only . Your name Alexa and If user ask anything apart from coding just say sorry!


Examples:
Q: Can you please explain a+b whole square?
A: Sorry!, I can only help in coding related questions.

Q: Hey, Can u write a python code for adding 2 numbers
A: def add(a+b):
    return a+b
"""
# few shot promting means : Directly giving the instruction to model with examples
# Zero shot promting means : The model is giving direct question or task without prior example



response = client.chat.completions.create(
    model="gemini-2.5-flash",
    
    messages=[
        {"role" : "system", "content": SYSTEM_PROMT},
        {"role": "user", "content": "can u pls help me to solve a + b whole square"}        
    ]
)

print(response.choices[0].message.content)