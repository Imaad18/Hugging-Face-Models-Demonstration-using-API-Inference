import os
from huggingface_hub import InferenceClient

# Ensure HF_TOKEN is set in environment variables
hf_token = os.environ.get("HF_TOKEN")
if not hf_token:
    raise EnvironmentError("Please set the 'HF_TOKEN' environment variable.")

# Initialize Inference Client with Featherless AI provider
client = InferenceClient(
    provider="featherless-ai",
    api_key=hf_token,
)

# Define the conversation messages
messages = [
    {"role": "user", "content": "What is the capital of France?"}
]

# Send the request
completion = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    messages=messages,
)

# Print the generated response
response = completion.choices[0].message
print(f"🤖 Assistant: {response['content']}")
