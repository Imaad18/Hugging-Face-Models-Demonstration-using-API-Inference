from transformers import pipeline, set_seed, GPT2Tokenizer, GPT2Model
import torch

# -------------------------------
# Part 1: Quick text generation
# -------------------------------
print("🔹 Text Generation with pipeline API")

generator = pipeline('text-generation', model='gpt2')
set_seed(42)

prompt = "Hello, I'm a language model,"
outputs = generator(prompt, max_length=30, num_return_sequences=3)

for i, output in enumerate(outputs):
    print(f"\nGenerated #{i+1}: {output['generated_text']}")

# -------------------------------
# Part 2: Manual model access (PyTorch)
# -------------------------------
print("\n🔹 Manual Tokenizer + GPT2Model (PyTorch)")

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')

text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)

print("Hidden state shape:", output.last_hidden_state.shape)
