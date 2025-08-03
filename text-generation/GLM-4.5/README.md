# 🤖 GLM-4.5 | Text Generation Demo

This folder demonstrates how to use the [GLM-4.5](https://huggingface.co/zai-org/GLM-4.5) model for high-quality text generation via the Hugging Face Inference API. GLM-4.5 is a next-generation foundation model optimized for intelligent agents, supporting reasoning, coding, and multi-modal interactions.

---

## 🔍 About GLM-4.5

GLM-4.5 and GLM-4.5-Air are large language models that unify tool usage, reasoning, and conversational AI. They operate in two modes:

- **🧠 Thinking Mode** — for complex multi-step reasoning and tool execution  
- **⚡ Instant Mode** — for fast, general-purpose responses  

| Model Variant    | Total Parameters | Active Parameters | Benchmark Score | Efficiency |
|------------------|------------------|-------------------|------------------|------------|
| GLM-4.5          | 355B             | 32B               | 63.2 (3rd Place) | High       |
| GLM-4.5-Air      | 106B             | 12B               | 59.8             | Very High  |

Both models are open-source under the **MIT license**, enabling commercial and research use.

---


<img width="750" height="526" alt="scrnli_DVvS7vV8z8tfBX" src="https://github.com/user-attachments/assets/92db533a-deb9-4790-af0d-f2051a78803e" />



## 📁 Files in This Folder

| File Name           | Description                                           |
|---------------------|-------------------------------------------------------|
| `glm_text_demo.py`  | Python script for running GLM-4.5 via Hugging Face API |
| `README.md`         | Model overview and instructions (this file)           |

---

## ⚙️ How to Run

### 1. Install Dependencies

```bash
pip install -q huggingface_hub
```


### On Kaggle:

from kaggle_secrets import UserSecretsClient
user_secrets = UserSecretsClient()
HF_TOKEN = user_secrets.get_secret("HF_TOKEN")


### On Colab:

from google.colab import userdata
HF_TOKEN = userdata.get("HF_TOKEN")


### Run The Model

from huggingface_hub import InferenceClient

client = InferenceClient(
    model="zai-org/GLM-4.5",
    token=HF_TOKEN
)

response = client.chat.completions.create(
    messages=[{"role": "user", "content": "What are large language models used for?"}]
)

print(response.choices[0].message.content)


### Author = Imaad Mahmood
