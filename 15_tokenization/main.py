import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there I'm Kalyan"
token = enc.encode(text)

print(f"Tokens : {token}")
# [25216, 1354, 5477, 658, 7606, 270]

dec = enc.decode([25216, 1354, 5477, 658, 7606, 270])
print(dec)