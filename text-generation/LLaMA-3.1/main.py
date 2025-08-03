"""
LLaMA-3.1 Text Generation Demo using Hugging Face Inference API (Novita Provider)

Author: Imaad Mahmood
GitHub: https://github.com/imaad18
Model: meta-llama/Llama-3.1-8B-Instruct
"""

import os
from huggingface_hub import InferenceClient

# Load the HF API token securely (adjust based on environment)
HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found. Please set it as an environment variable.")

# Initialize the InferenceClient for the Novita provider
client = InferenceClient(
    provider="novita",
    api_key=HF_TOKEN,
)

# Define your input prompt
prompt = "What is the capital of France?"

# Create a chat-style message for the model (similar to OpenAI format)
messages = [
    {"role": "user", "content": prompt}
]

# Call the chat completion API
completion = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=messages,
)

# Extract and print the model's reply
response = completion.choices[0].message.content
print(f"\n🤖 LLaMA-3.1 Response:\n{response}")
