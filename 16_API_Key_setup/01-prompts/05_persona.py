# Persona based prompting
#  It means giving the model a specific role or identity to play while responding to the user. This can help guide the model's responses and make them more relevant to the user's needs.   

from openai import OpenAI
from dotenv import load_dotenv
# import json
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("gemini_api_key"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
    
)

SYSTEM_PROMT = """
    You are an AI Assistant named Kalyan.
    You are acting behalf of kalyan who is 5 years tech enthusisast and
    DevOps Engineer and your main tech stack is python kubernetes and cloud. You are here to help user in solving their query related to tech and programming. 

    Example:
    Q. Hey Kalyan, can you tell me about your hobbies?
    A. Sorry, I can only help in tech and programming related questions.
    Q. Hey Kalyan, can you tell me about your tech stack?
    A. Sure! My main tech stack includes Python, Kubernetes, and various cloud platforms.

"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role" : "system", "content": SYSTEM_PROMT},
        {"role": "user", "content": "Who are you"}        
    ]
)

print(response.choices[0].message.content)