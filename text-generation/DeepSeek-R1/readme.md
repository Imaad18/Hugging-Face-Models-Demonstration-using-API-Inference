<img width="300" height="168" alt="dp" src="https://github.com/user-attachments/assets/fce0bd5b-1c7a-4ee4-8c55-542efc408bfc" />


# 🧠 DeepSeek-R1-Distill-LLaMA-8B

The **DeepSeek-R1-Distill-LLaMA-8B** is a high-performance, instruction-tuned, distilled version of LLaMA, designed for fast and efficient inference while preserving strong generalization capabilities.

## 🔍 Model Overview

- **Model Name**: `deepseek-ai/DeepSeek-R1-Distill-Llama-8B`
- **Architecture**: Distilled from LLaMA-2 base
- **Parameters**: 8 Billion
- **Type**: Chat / Instruction-following
- **Provider**: [`novita`](https://huggingface.co/novita)
- **License**: Apache 2.0
- **Hosted on**: [Hugging Face Hub](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B)

## 🚀 Key Features

- 🔬 **Distilled architecture** — Smaller size, faster inference with minimal accuracy trade-off.
- 📚 **Instruction-tuned** — Optimized for multi-turn dialogue and reasoning tasks.
- 💡 **Chat-ready** — Compatible with OpenAI-style chat completions API.
- 🧠 **Efficient deployment** — Ideal for inference APIs, research experiments, and AI assistants.

## 🧠 Use Cases

- AI chatbots and assistants
- Document/question answering
- Reasoning and educational tools
- Multi-turn dialogue systems
- Code and content generation

## ⚙️ Technical Details

| Attribute            | Value                                      |
|----------------------|--------------------------------------------|
| Architecture         | Decoder-only Transformer (LLaMA)           |
| Distilled From       | LLaMA-2                                    |
| Parameters           | 8B                                          |
| Context Length       | 4K tokens                                  |
| Quantization Support | Yes (int4/int8) with third-party tools     |
| Fine-tuned On        | Instructions, multi-turn chat, reasoning   |
| Output Format        | OpenAI-style Chat Completions (`messages`) |

## 📦 Hosted Access

You can use the model through the Hugging Face `InferenceClient` with `provider="novita"`:

```bash
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="novita",
    api_key="your_huggingface_token",
)

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
    messages=[
        {"role": "user", "content": "Explain quantum computing in simple terms."}
    ],
)

print(completion.choices[0].message)
```
