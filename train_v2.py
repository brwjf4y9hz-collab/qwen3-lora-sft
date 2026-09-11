import torch

from datasets import load_dataset
from peft import LoraConfig
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import SFTConfig, SFTTrainer

MODEL_PATH = "/root/autodl-tmp/models/Qwen3-0.6B"
TRAIN_FILE = "data/train_v2.jsonl"
OUTPUT_DIR = "outputs/qwen3-0.6b-lora-v2"

def main():
    use_bf16 = torch.cuda.is_available() and torch.cuda.is_bf16_supported()
    dtype = torch.bfloat16 if use_bf16 else torch.float16

    print("=" * 60)
    print("CUDA:", torch.cuda.is_available())
    print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU")
    print("BF16 supported:", use_bf16)
    print("Training dtype:", dtype)
    print("=" * 60)

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_PATH,
        trust_remote_code=True,
    )

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        dtype=dtype,
        trust_remote_code=True,
    )
    model.config.use_cache = False

    dataset = load_dataset(
        "json",
        data_files=TRAIN_FILE,
        split="train",
    )

    dataset = dataset.train_test_split(
        test_size=0.2,
        seed=42,
    )

    print(dataset)
    print("Train samples:", len(dataset["train"]))
    print("Eval samples:", len(dataset["test"]))

    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules="all-linear",
    )

    training_args = SFTConfig(
        output_dir=OUTPUT_DIR,

        # Keep LoRA hyperparameters fixed relative to V1.
        # V2 changes the dataset design, not the adapter configuration.
        num_train_epochs=2,

        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        gradient_accumulation_steps=1,

        learning_rate=1e-4,

        logging_steps=10,
        eval_strategy="epoch",
        save_strategy="epoch",
        save_total_limit=2,

        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,

        bf16=use_bf16,
        fp16=not use_bf16,

        gradient_checkpointing=False,
        max_length=512,
        assistant_only_loss=True,

        report_to="none",
        seed=42,
    )

    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["test"],
        processing_class=tokenizer,
        peft_config=lora_config,
    )

    print("\n" + "=" * 60)
    print("LoRA Trainable Parameters")
    print("=" * 60)
    trainer.model.print_trainable_parameters()

    print("\n" + "=" * 60)
    print("Start V2 Training")
    print("=" * 60)

    trainer.train()

    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

    if torch.cuda.is_available():
        allocated = torch.cuda.max_memory_allocated() / 1024**3
        reserved = torch.cuda.max_memory_reserved() / 1024**3
        print(f"\nPeak allocated memory: {allocated:.2f} GB")
        print(f"Peak reserved memory: {reserved:.2f} GB")

    print(f"\nTraining finished. LoRA adapter saved to: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
