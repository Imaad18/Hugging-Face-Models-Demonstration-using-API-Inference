# text-generation/Gemma3/gemma3_text_demo.py

from transformers import AutoTokenizer, BitsAndBytesConfig, Gemma3ForCausalLM
import torch

model_id = "google/gemma-3-1b-it"

# Load model with 8-bit quantization for memory efficiency
quantization_config = BitsAndBytesConfig(load_in_8bit=True)

model = Gemma3ForCausalLM.from_pretrained(
    model_id,
    quantization_config=quantization_config,
    device_map="auto"
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_id)

# Chat-style messages
messages = [
    [
        {
            "role": "system",
            "content": [{"type": "text", "text": "You are a helpful assistant."}],
        },
        {
            "role": "user",
            "content": [{"type": "text", "text": "Write a poem on Hugging Face, the company"}],
        },
    ]
]

# Tokenize chat input
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device).to(torch.bfloat16)

# Generate output
with torch.inference_mode():
    outputs = model.generate(**inputs, max_new_tokens=64)

# Decode and print
print(tokenizer.batch_decode(outputs, skip_special_tokens=True)[0])
