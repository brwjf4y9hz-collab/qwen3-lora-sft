import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

BASE_MODEL = "/root/autodl-tmp/models/Qwen3-0.6B"
SFT_ADAPTER = "outputs/qwen3-0.6b-lora-v2"
MERGED_DIR = "outputs/qwen3-0.6b-sft-v2-merged"

def main():
    print("Loading Base Model on CPU...")
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        dtype=torch.bfloat16,
        device_map="cpu",
        trust_remote_code=True,
    )

    print("Loading SFT V2 LoRA adapter...")
    model = PeftModel.from_pretrained(
        base_model,
        SFT_ADAPTER,
        is_trainable=False,
    )

    print("Merging SFT V2 adapter into Base Model...")
    model = model.merge_and_unload()

    tokenizer = AutoTokenizer.from_pretrained(
        BASE_MODEL,
        trust_remote_code=True,
    )

    model.save_pretrained(
        MERGED_DIR,
        safe_serialization=True,
    )
    tokenizer.save_pretrained(MERGED_DIR)

    print(f"Merged model saved to: {MERGED_DIR}")

if __name__ == "__main__":
    main()
