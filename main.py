print("Script started")

import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {"role": "user", "content": "Say hello briefly."}
    ]
)

print("Got response")
print(response["message"]["content"])




