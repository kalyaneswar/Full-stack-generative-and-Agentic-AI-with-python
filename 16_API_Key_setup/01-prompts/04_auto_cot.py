
from openai import OpenAI
from dotenv import load_dotenv
import json
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
    
)



SYSTEM_PROMT = """
    You are expert in AI assistant resolving user's querys using chain of thought promt. You will be given a question and you have to answer it in a step by step manner. You can also refuse to answer if the question is out of your domain.
    You work on START, PLAN and OUTPUT format. You will first start with START, then you will give a PLAN and at the end you will give the OUTPUT.

    RULES:
    1. You will always follow the START, PLAN and OUTPUT format.
    2. Strictly follow json format for your answer.
    3. Only run one STEP at a time, and wait for the next instruction.

    OUTPUT:
    {step: "START" | "PLAN" | "OUTPUT",content: "string"}

    EXAMPLE:
    Q. Hey can you solve 2 + 3 * 5 / 10

    A. {
        "step": "START",
        "content": "I will solve the expression 2 + 3 * 5 / 10 step by step."
    }
    {
        "step": "PLAN",
        "content": "According to order of operations (PEMDAS/BODMAS), I will first perform multiplication and division, then addition."
    }
    {
        "step": "OUTPUT",
        "content": "2 + 3 * 5 / 10 = 2 + 15 / 10 = 2 + 1.5 = 3.5"
    }

"""

message_history = [
    {"role" : "system", "content": SYSTEM_PROMT},
]

print("\n\n\n\n")

user_query = input("User: ")
message_history.append({"role": "user", "content": user_query}) 

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=message_history
    )  

    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})
    passed_result = json.loads(raw_result)

    if passed_result.get("step") == "START":
        print("🔥 STARTING LLM LOOP")
        print(passed_result.get("content"))
        continue

    if passed_result.get("step") == "PLAN":
        print("🧠 PLANNING LLM LOOP")
        print(passed_result.get("content"))
        continue

    if passed_result.get("step") == "OUTPUT":
        print("🤖 OUTPUT FROM LLM")
        print(passed_result.get("content"))
        break


print("\n\n\n\n")