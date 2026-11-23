import ollama

response = ollama.chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "Explain Artificial Intelligence."
        }
    ]
)

print(response["message"]["content"])