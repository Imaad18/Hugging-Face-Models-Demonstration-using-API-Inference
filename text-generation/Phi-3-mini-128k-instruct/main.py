import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Set random seed for reproducibility
torch.random.manual_seed(0)

# Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-128k-instruct",
    device_map="cuda",
    torch_dtype="auto",
    trust_remote_code=True,
)

tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-128k-instruct", trust_remote_code=True)

# Function to convert chat-style messages into ChatML format (used by Phi-3)
def format_chat(messages):
    prompt = ""
    for msg in messages:
        role = msg["role"]
        content = msg["content"]
        if role == "system":
            prompt += f"<|system|>\n{content}\n"
        elif role == "user":
            prompt += f"<|user|>\n{content}\n"
        elif role == "assistant":
            prompt += f"<|assistant|>\n{content}\n"
    prompt += "<|assistant|>\n"  # Add this to let model know it should respond next
    return prompt

# Chat history
messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "Can you provide ways to eat combinations of bananas and dragonfruits?"},
    {"role": "assistant", "content": "Sure! Here are some ways to eat bananas and dragonfruits together:\n1. Banana and dragonfruit smoothie: Blend bananas and dragonfruits with milk and honey.\n2. Banana and dragonfruit salad: Mix sliced bananas and dragonfruits with lemon juice and honey."},
    {"role": "user", "content": "What about solving an 2x + 3 = 7 equation?"},
]

# Convert messages into prompt
prompt = format_chat(messages)

# Tokenize prompt
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

# Generate output
generation_args = {
    "max_new_tokens": 100,
    "temperature": 0.0,
    "do_sample": False,
}
output = model.generate(**inputs, **generation_args)

# Decode and print response
response = tokenizer.decode(output[0], skip_special_tokens=True)
# Optional: Extract just the final assistant response
final_answer = response.split("<|assistant|>\n")[-1].strip()

print(final_answer)
