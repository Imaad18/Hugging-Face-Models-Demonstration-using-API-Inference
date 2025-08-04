import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load tokenizer and model (StableBeluga2)
tokenizer = AutoTokenizer.from_pretrained("stabilityai/StableBeluga2", use_fast=False)
model = AutoModelForCausalLM.from_pretrained(
    "stabilityai/StableBeluga2",
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True,
    device_map="auto"
)

# Define system prompt
system_prompt = (
    "### System:\n"
    "You are Stable Beluga, an AI that follows instructions extremely well. "
    "Help as much as you can. Remember, be safe, and don't do anything illegal.\n\n"
)

# User message
message = "Write me a poem please"
prompt = f"{system_prompt}### User: {message}\n\n### Assistant:\n"

# Tokenize and move to GPU
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

# Generate output
output = model.generate(
    **inputs,
    do_sample=True,
    top_p=0.95,
    top_k=0,
    max_new_tokens=256
)

# Decode and print result
print(tokenizer.decode(output[0], skip_special_tokens=True))
