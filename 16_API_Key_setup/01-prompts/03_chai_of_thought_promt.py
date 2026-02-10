# 03_chai_of_thought_promt

from openai import OpenAI
from dotenv import load_dotenv
import json
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("gemini_api_key"),
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




response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    
    messages=[
        {"role" : "system", "content": SYSTEM_PROMT},
        {"role": "user", "content": "write the code to add n numbers in js"},
        {"role": "assistant", "content": json.dumps({
    "step": "START",
    "content": "I will write a JavaScript code to add n numbers step by step"
        })},
        {"role": "assistant", "content": json.dumps({
    "step": "PLAN",
    "content": "I will create a function that takes an array of numbers as input and returns the sum of those numbers."
        })},
         {"role": "assistant", "content": json.dumps({
    "step": "OUTPUT",   
    "content": "Output: The sum of [] is: 0\n\n// Using Array.prototype.reduce (more concise):\nfunction sumNumbersReduce(numbers) {\n  return numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);\n}\n\nconsole.log(`Sum using reduce for [1, 2, 3, 4, 5]: ${sumNumbersReduce(myNumbers)}`); // Output: Sum using reduce for [1, 2, 3, 4, 5]: 15\n```"
        })}

            
    ]
)

print(response.choices[0].message.content)