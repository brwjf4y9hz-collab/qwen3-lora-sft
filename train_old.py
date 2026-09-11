from datasets import load_dataset
from peft import LoraConfig
from transformers import AutoTokenizer
from trl import SFTConfig, SFTTrainer


MODEL_NAME = "/root/autodl-tmp/models/Qwen3-0.6B"
TRAIN_FILE = "data/train.jsonl"
OUTPUT_DIR = "outputs/qwen3-0.6b-lora"


def main():
    # 1. Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True,
    )

    # 2. Dataset
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

    # 3. LoRA
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules="all-linear",
    )

    # 4. SFT config
    training_args = SFTConfig(
        output_dir=OUTPUT_DIR,

        num_train_epochs=1,

        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,

        gradient_accumulation_steps=4,

        learning_rate=1e-4,

        logging_steps=1,

        save_strategy="epoch",
        eval_strategy="epoch",

        bf16=True,

        gradient_checkpointing=True,
        assistant_only_loss=True,
        max_length=1024,

        report_to="none",
    )

    # 5. Trainer
    trainer = SFTTrainer(
        model=MODEL_NAME,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["test"],
        processing_class=tokenizer,
        peft_config=lora_config,
    )

    # 6. Train
    trainer.train()

    # 7. Save LoRA adapter
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

    print(f"Training finished. Adapter saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
