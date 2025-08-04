# main.py
# ---------------------------------------------
# Hugging Face Inference for DeepSeek-R1 Model
# Model: deepseek-ai/DeepSeek-R1-Distill-Llama-8B
# Provider: novita
# Usage: Text generation via chat completion
# ---------------------------------------------

import os
from huggingface_hub import InferenceClient

# Initialize the Hugging Face Inference Client
client = InferenceClient(
    provider="novita",
    api_key=os.environ["HF_TOKEN"],  # For Kaggle: use user_secrets.get_secret
)

# Define the input prompt
prompt = "What is the capital of France?"

# Create a chat-style completion
completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
)

# Print the model's response
print("Model response:")
print(completion.choices[0].message)
