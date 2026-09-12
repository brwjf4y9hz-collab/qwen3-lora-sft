import argparse
import json
from pathlib import Path

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_PATH = "/root/autodl-tmp/models/Qwen3-0.6B"
EVAL_FILE = "data/eval_v2.jsonl"

ADAPTER_PATHS = {
    "v0": "outputs/qwen3-0.6b-lora",
    "v1": "outputs/qwen3-0.6b-lora-v1",
    "v2": "outputs/qwen3-0.6b-lora-v2",
    "dpo_v0": "outputs/qwen3-0.6b-dpo-v0",
    "dpo_v1": "outputs/qwen3-0.6b-dpo-v1-hard",
}

OUTPUT_FILES = {
    "base": "results/eval_v2_base.jsonl",
    "v0": "results/eval_v2_v0.jsonl",
    "v1": "results/eval_v2_v1.jsonl",
    "v2": "results/eval_v2_v2.jsonl",
    "dpo_v0": "results/eval_v2_dpo_v0.jsonl",
    "dpo_v1": "results/eval_v2_dpo_v1.jsonl",
}

def load_model(mode):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    base_model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    if mode == "base":
        model = base_model
    else:
        adapter_path = ADAPTER_PATHS[mode]
        if not Path(adapter_path).exists():
            raise FileNotFoundError(f"Adapter not found: {adapter_path}")
        model = PeftModel.from_pretrained(base_model, adapter_path)
    model.eval()
    return tokenizer, model

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["base", "v0", "v1", "v2","dpo_v0", "dpo_v1"], required=True)
    parser.add_argument("--max-new-tokens", type=int, default=256)
    args = parser.parse_args()

    tokenizer, model = load_model(args.mode)
    with open(EVAL_FILE, encoding="utf-8") as f:
        samples = [json.loads(line) for line in f]

    Path("results").mkdir(exist_ok=True)

    output_file = OUTPUT_FILES[args.mode]

    with open(output_file, "w", encoding="utf-8") as out:
        for n, sample in enumerate(samples, 1):
            messages = [{"role": "user", "content": sample["prompt"]}]
            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
                enable_thinking=False,
            )
            inputs = tokenizer(text, return_tensors="pt").to(model.device)

            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=args.max_new_tokens,
                    do_sample=False,
                )

            generated = outputs[0][inputs["input_ids"].shape[1]:]
            response = tokenizer.decode(generated, skip_special_tokens=True)

            record = {
                "id": sample["id"],
                "topic": sample["topic"],
                "prompt": sample["prompt"],
                "response": response,
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")

            print(f"[{n:02d}/{len(samples)}] {sample['topic']} | {sample['prompt']}")
            print(response[:180].replace("\n", " "))
            print("-" * 80)

    print(f"\nSaved: {output_file}")

if __name__ == "__main__":
    main()
