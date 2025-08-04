### 🧠 GPT-2: Generative Pretrained Transformer 2

GPT-2 is a large transformer-based language model developed by **OpenAI**, capable of generating coherent and contextually relevant paragraphs of text. This repository provides an implementation for running GPT-2 using the Hugging Face 🤗 `transformers` library.

---

### 📌 Overview

- **Model Name:** GPT-2 (Generative Pretrained Transformer 2)  
- **Developed By:** [OpenAI](https://openai.com/research/gpt-2)  
- **Architecture:** Decoder-only Transformer  
- **Pretraining Corpus:** 8 million web pages (WebText dataset)  
- **Objective:** Causal Language Modeling (next-token prediction)  
- **Context Window:** 1024 tokens  
- **Variants Available:** 124M, 355M, 774M, and 1.5B parameters

---

## 📚 Model Details

| Model Variant   | Parameters | Layers | Hidden Size | Attention Heads |
|----------------|------------|--------|--------------|------------------|
| `gpt2`         | 124M       | 12     | 768          | 12               |
| `gpt2-medium`  | 355M       | 24     | 1024         | 16               |
| `gpt2-large`   | 774M       | 36     | 1280         | 20               |
| `gpt2-xl`      | 1.5B       | 48     | 1600         | 25               |

---

## 🧪 Capabilities

- Autoregressive text generation
- Language modeling and completion
- Creative writing, summarization, Q&A (with instruction fine-tuning)
- Few-shot, zero-shot, and one-shot tasks using context learning

---

## 🔧 Setup

Install dependencies:


### Example Usage:

```bash
pip install transformers torch tensorflow
```

```bash
from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="gpt2")
set_seed(42)

outputs = generator(
    "Once upon a time, in a world governed by AI,", 
    max_length=50, 
    num_return_sequences=3
)

for i, output in enumerate(outputs):
    print(f"Generated #{i+1}: {output['generated_text']}")
```

```bash
from transformers import GPT2Tokenizer, GPT2Model
import torch

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2Model.from_pretrained("gpt2")

text = "The future of AI is"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)

print("Hidden states shape:", outputs.last_hidden_state.shape)
```
