import torch
from datasets import load_dataset
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer
from trl import DPOConfig, DPOTrainer

SFT_ADAPTER = "outputs/qwen3-0.6b-lora-v2"
DATA_FILE = "data/dpo/dpo_train_v0.jsonl"
OUTPUT_DIR = "outputs/qwen3-0.6b-dpo-v0"


def main():
    use_bf16 = torch.cuda.is_available() and torch.cuda.is_bf16_supported()
    dtype = torch.bfloat16 if use_bf16 else torch.float16

    print("=" * 60)
    print("CUDA:", torch.cuda.is_available())
    print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU")
    print("BF16 supported:", use_bf16)
    print("Training dtype:", dtype)
    print("=" * 60)

    # Directly load the existing SFT V2 PEFT model and keep the adapter trainable.
    # No merge is needed.
    model = AutoPeftModelForCausalLM.from_pretrained(
        SFT_ADAPTER,
        is_trainable=True,
        dtype=dtype,
        trust_remote_code=True,
    )
    model.config.use_cache = False

    tokenizer = AutoTokenizer.from_pretrained(
        SFT_ADAPTER,
        trust_remote_code=True,
    )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    dataset = load_dataset(
        "json",
        data_files=DATA_FILE,
        split="train",
    ).train_test_split(
        test_size=0.2,
        seed=42,
    )

    print(dataset)
    print("Train preference pairs:", len(dataset["train"]))
    print("Eval preference pairs:", len(dataset["test"]))

    args = DPOConfig(
        output_dir=OUTPUT_DIR,

        num_train_epochs=2,
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        gradient_accumulation_steps=1,

        learning_rate=5e-6,
        beta=0.1,
        loss_type="sigmoid",

        max_length=512,

        logging_steps=5,
        eval_strategy="epoch",
        save_strategy="epoch",
        save_total_limit=2,

        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,

        bf16=use_bf16,
        fp16=not use_bf16,

        gradient_checkpointing=False,

        report_to="none",
        seed=42,
    )

    # Important:
    # - model is already a PeftModel
    # - do NOT pass peft_config again
    # - ref_model=None => DPOTrainer uses the initial policy as reference
    trainer = DPOTrainer(
        model=model,
        ref_model=None,
        args=args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["test"],
        processing_class=tokenizer,
    )

    print("\n" + "=" * 60)
    print("DPO Trainable Parameters")
    print("=" * 60)
    trainer.model.print_trainable_parameters()

    print("\n" + "=" * 60)
    print("Start DPO Training")
    print("=" * 60)

    trainer.train()

    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

    if torch.cuda.is_available():
        allocated = torch.cuda.max_memory_allocated() / 1024**3
        reserved = torch.cuda.max_memory_reserved() / 1024**3
        print(f"\nPeak allocated memory: {allocated:.2f} GB")
        print(f"Peak reserved memory: {reserved:.2f} GB")

    print(f"\nDPO adapter saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
