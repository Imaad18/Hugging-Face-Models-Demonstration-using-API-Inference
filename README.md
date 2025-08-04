<img width="318" height="159" alt="hf" src="https://github.com/user-attachments/assets/ab30522f-b925-442b-a4ce-3803d4c8ecab" />


# 🤗 Hugging Face Models Demonstration via API Inference

[![License](https://img.shields.io/github/license/Imaad18/Hugging-Face-Models-Demonstration-using-API-Inference)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/Imaad18/Hugging-Face-Models-Demonstration-using-API-Inference?style=social)](https://github.com/Imaad18/Hugging-Face-Models-Demonstration-using-API-Inference/stargazers)


> A modular, CUDA-accelerated framework for showcasing text generation with Hugging Face models like Phi-3, Mistral, and StableBeluga using local API-style inference.

---

## 📌 Project Goals

- ✅ Demonstrate usage of different Hugging Face models for text generation  
- ✅ Provide modular scripts with consistent inference pipelines  
- ✅ Emphasize real-world prompts and system/user/assistant formatting  
- ✅ Enable fast local inference using CUDA (GPU)  
- ✅ Serve as a template for building LLM-based applications  

---

## 🧠 Supported Models

| Model Name                   | Parameters | Context Length | Key Features                                     |
|-----------------------------|------------|----------------|--------------------------------------------------|
| Phi-3 Mini (128K Instruct)  | 3.8B       | 128,000        | Lightweight, instruction-tuned, long context     |
| Mistral 7B Instruct v0.2    | 7B         | ~32,000        | Strong general-purpose reasoning & instruction   |
| StableBeluga 2              | ~7B        | ~32,000        | Fine-tuned assistant-style model by Stability AI |

Each model is organized in its own folder inside the `text-generation/` directory, with a dedicated inference script and prompt format.

---

## 📁 Repository Structure

Hugging-Face-Models-Demonstration-using-API-Inference/
│
├── text-generation/
│ ├── phi-3-mini/
│ │ ├── model_inference.py
│ │ └── README.md
│ ├── mistral/
│ │ ├── model_inference.py
│ │ └── README.md
│ ├── stablebeluga/
│ │ ├── model_inference.py
│ │ └── README.md
│
├── requirements.txt
└── README.md ← This file


Each subfolder has:
- `model_inference.py`: for running the model
- `README.md`: usage guide and examples for that specific model

---

## 🔧 Setup Instructions

### ✅ Requirements

- Python 3.9+
- CUDA-enabled GPU (recommended: 8GB+ VRAM)
- Installed PyTorch with GPU support
- Hugging Face Transformers library

### 🔌 Installation

Clone the repository and install dependencies:
```bash
git clone https://github.com/Imaad18/Hugging-Face-Models-Demonstration-using-API-Inference.git
cd Hugging-Face-Models-Demonstration-using-API-Inference
pip install -r requirements.txt
```



Each folder contains:

- `main.py` – Clean demo for inference
- `README.md` – Model-specific notes

---

## 🚀 Models Demonstrated

| 🧠 Model Name | ⚙️ Access | 🔗 Hugging Face Link |
|--------------|-----------|----------------------|
| DeepSeek R1 Distill | API | [Link](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B) |
| Qwen 0.5B Chat | API | [Link](https://huggingface.co/Qwen/Qwen1.5-0.5B-Chat) |
| Mistral 7B Instruct | API | [Link](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) |
| StableBeluga 2 | Local | [Link](https://huggingface.co/stabilityai/StableBeluga2) |
| Phi-3 Mini | Local | [Link](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct) |
| GPT-2 | Local | [Link](https://huggingface.co/gpt2) |

---

## ⚙️ Setup & Usage

### 🧪 API-Based Inference (e.g., Qwen, DeepSeek, Mistral)

```bash
# Set your Hugging Face API token
export HF_TOKEN=your_huggingface_token
```

# Example
cd text-generation/Qwen2.5
python main.py


### Author
Imaad Mahmood
🎓 AI Undergraduate | 🧠 ML & LLM Enthusiast | 🌍 Based in Bahawalpur, Pakistan
🔗 GitHub: @Imaad18
📫 Email: imaadmahmood18102004@gmail.com
