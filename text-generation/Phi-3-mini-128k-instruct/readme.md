![phi](https://github.com/user-attachments/assets/eac35168-5259-417f-8722-01c01066f6ad)


# Phi-3 Mini (128k) Instruct - Chat-ready Model

[![Hugging Face](https://img.shields.io/badge/HuggingFace-Model-yellow?logo=huggingface)](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct)  
**Model:** `microsoft/Phi-3-mini-128k-instruct`  
**Type:** Instruction-tuned, causal language model  
**Context Length:** 128,000 tokens  
**Architecture:** Transformer decoder-only (GPT-like)  
**License:** MIT  

---

## 📌 Overview

`Phi-3-mini-128k-instruct` is a 3.8 billion parameter **instruction-tuned** model developed by Microsoft, part of the Phi-3 family. It is trained to follow natural language instructions and optimized for conversational tasks, math reasoning, code generation, and long-context understanding (up to **128k tokens**).

This model uses the **ChatML** format (`<|system|>`, `<|user|>`, `<|assistant|>`) for prompt construction, enabling clear role-based multi-turn conversations similar to ChatGPT.

---

## 🚀 Key Features

- 🔁 **128k context length** – handle long documents and multi-turn conversations
- 💬 **Instruction-tuned** – suitable for chat, reasoning, question-answering
- 🧠 **Reasoning & math** – good performance on equations, logic, and structured answers
- 🧾 **ChatML prompt formatting** – clearly distinguish system, user, and assistant roles
- 🧪 Lightweight – 3.8B parameters, suitable for consumer GPUs (12–16GB VRAM)

---

## 🛠️ Installation & Setup

```bash
pip install transformers accelerate
```
