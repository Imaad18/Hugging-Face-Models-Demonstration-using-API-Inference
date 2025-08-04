<img width="225" height="225" alt="meta" src="https://github.com/user-attachments/assets/61575cf4-b782-420f-ba27-347605c5e6c1" />


# 🦙 LLaMA 3.1 (8B Instruct) — Text Generation Demo

This folder contains a demo for text generation using the **Meta LLaMA-3.1 8B Instruct** model via Hugging Face Inference API through the **Novita** provider.

---

## 📌 Model Summary

**LLaMA-3.1-8B-Instruct** is a cutting-edge, instruction-tuned large language model from Meta. It excels at natural language understanding, reasoning, and task-following.

| Property             | Description                                 |
|----------------------|---------------------------------------------|
| 🔹 Model Name        | `meta-llama/Llama-3.1-8B-Instruct`          |
| 🔹 Type              | Transformer-based LLM (chat-style)          |
| 🔹 Parameters        | 8 Billion                                    |
| 🔹 Capability        | Instruction-following, dialogue             |
| 🔹 Provider          | `novita` via Hugging Face Inference API     |

---

## 🧪 Demo Overview

This script sends a user prompt to the LLaMA 3.1 model and prints the model’s response in a conversational format. Ideal for tasks like:

- Text generation
- Conversational AI
- Reasoning-based Q&A
- Agent workflows

---

## 🚀 Getting Started

### ✅ 1. Install Required Package

```bash
pip install huggingface_hub
```

### Set your Hugging Face API
# For Colab:

```bash
from google.colab import userdata
import os

os.environ["HF_TOKEN"] = userdata.get("HF_TOKEN")  # securely fetch
```

# For Kaggle

```bash
import os
from kaggle_secrets import UserSecretsClient

user_secrets = UserSecretsClient()
os.environ["HF_TOKEN"] = user_secrets.get_secret("HF_TOKEN")
```
