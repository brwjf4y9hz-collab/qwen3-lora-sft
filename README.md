# Qwen3 LoRA SFT

A minimal supervised fine-tuning project based on Qwen3 and LoRA.

## Model

- Base Model: Qwen/Qwen3-0.6B
- Fine-tuning: LoRA
- Frameworks: Transformers, TRL, PEFT
- Training Platform: AutoDL

## Pipeline

Dataset
→ Chat Template
→ Tokenization
→ Qwen3
→ LoRA SFT
→ Evaluation
→ Hugging Face

## Project Structure

```text
.
├── data/
│   └── train.jsonl
├── train.py
├── inference.py
├── requirements.txt
└── README.md

