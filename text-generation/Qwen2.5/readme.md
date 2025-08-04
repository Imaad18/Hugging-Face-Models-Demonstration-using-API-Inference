
---

## 🧠 Model Details

| Key              | Description                                   |
|------------------|-----------------------------------------------|
| **Model Name**   | `Qwen/Qwen2.5-7B-Instruct`                    |
| **Provider**     | `featherless-ai` via Hugging Face API         |
| **Parameters**   | 7 Billion                                      |
| **Capabilities** | Chat, reasoning, multi-turn dialogue           |
| **Languages**    | Multilingual (English, Chinese, etc.)         |
| **License**      | Open source (Apache 2.0)                       |

---

## 💻 Works With

- ✅ Google Colab
- ✅ Kaggle Notebooks
- ✅ Local Python environment

---

## 🚀 Quick Start

### 🔸 1. Install Dependencies

```bash
pip install huggingface_hub
```

### For Colab
```bash
from google.colab import userdata
import os

os.environ["HF_TOKEN"] = userdata.get("HF_TOKEN")
```

### Kaggle
```bash
import os
from kaggle_secrets import UserSecretsClient

user_secrets = UserSecretsClient()
os.environ["HF_TOKEN"] = user_secrets.get_secret("HF_TOKEN")
```
