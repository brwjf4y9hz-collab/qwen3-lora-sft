import argparse
import json
import torch

from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel


MODEL_PATH = "/root/autodl-tmp/models/Qwen3-0.6B"
ADAPTER_PATHS = {
    "v0": "outputs/qwen3-0.6b-lora",
    "v1": "outputs/qwen3-0.6b-lora-v1",
}

EVAL_FILE = "data/eval_prompts.jsonl"


def load_model(mode):

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_PATH,
        trust_remote_code=True,
    )

    base_model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )

    if mode == "base":
        print("Using Base Model")
        model = base_model

    else:
        adapter_path = ADAPTER_PATHS[mode]

        print(f"Loading adapter: {adapter_path}")

        model = PeftModel.from_pretrained(
            base_model,
            adapter_path,
    )
    model.eval()

    return tokenizer, model


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--mode",
        choices=["base", "v0", "v1"],
        required=True,
    )

    args = parser.parse_args()

    tokenizer, model = load_model(args.mode)

    output_file = {
        "base": "results/baseline.jsonl",
        "v0": "results/sft_v0.jsonl",
        "v1": "results/sft_v1.jsonl",
    }
    output_file = output_file[args.mode]

    with open(EVAL_FILE, "r", encoding="utf-8") as f:
        samples = [
            json.loads(line)
            for line in f
        ]

    results = []

    for sample in samples:

        prompt = sample["prompt"]

        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]

        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False,
        )

        inputs = tokenizer(
            text,
            return_tensors="pt",
        ).to(model.device)

        with torch.no_grad():

            outputs = model.generate(
                **inputs,
                max_new_tokens=256,
                do_sample=False,
            )

        input_length = inputs["input_ids"].shape[1]

        generated_ids = outputs[0][input_length:]

        response = tokenizer.decode(
            generated_ids,
            skip_special_tokens=True,
        )

        result = {
            "id": sample["id"],
            "prompt": prompt,
            "response": response,
        }

        results.append(result)

        print("=" * 80)
        print("Question:", prompt)
        print(f"{args.mode.upper()}:", response)

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as f:

        for result in results:

            f.write(
                json.dumps(
                    result,
                    ensure_ascii=False,
                )
                + "\n"
            )

    print()
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()