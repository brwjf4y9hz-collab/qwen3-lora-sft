import torch

from datasets import load_dataset
from peft import LoraConfig
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import SFTConfig, SFTTrainer


MODEL_PATH = "/root/autodl-tmp/models/Qwen3-0.6B"
TRAIN_FILE = "data/train_v1.jsonl"
OUTPUT_DIR = "outputs/qwen3-0.6b-lora-v1"


def main():

    # ==================================================
    # 0. GPU / Precision
    # ==================================================

    use_bf16 = torch.cuda.is_available() and torch.cuda.is_bf16_supported()

    dtype = (
        torch.bfloat16
        if use_bf16
        else torch.float16
    )

    print("=" * 60)
    print("CUDA:", torch.cuda.is_available())
    print("GPU:", torch.cuda.get_device_name(0))
    print("BF16 supported:", use_bf16)
    print("Training dtype:", dtype)
    print("=" * 60)


    # ==================================================
    # 1. Tokenizer
    # ==================================================

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_PATH,
        trust_remote_code=True,
    )


    # ==================================================
    # 2. Base Model
    # ==================================================

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=dtype,
        trust_remote_code=True,
    )

    # 训练时不需要 KV Cache
    model.config.use_cache = False


    # ==================================================
    # 3. Dataset
    # ==================================================

    dataset = load_dataset(
        "json",
        data_files=TRAIN_FILE,
        split="train",
    )

    dataset = dataset.train_test_split(
        test_size=0.2,
        seed=42,
    )

    print()
    print("Dataset:")
    print(dataset)

    print("Train samples:", len(dataset["train"]))
    print("Eval samples:", len(dataset["test"]))


    # ==================================================
    # 4. LoRA
    # ==================================================

    lora_config = LoraConfig(
        r=16,

        lora_alpha=32,

        lora_dropout=0.05,

        bias="none",

        task_type="CAUSAL_LM",

        target_modules="all-linear",
    )


    # ==================================================
    # 5. SFT Config
    # ==================================================

    training_args = SFTConfig(
        output_dir=OUTPUT_DIR,

        # 现在只有 8 条 train 数据
        # 所以故意训练多轮做 pipeline sanity check
        num_train_epochs=3,

        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,

        # 小数据实验先不要累积
        gradient_accumulation_steps=1,

        learning_rate=1e-4,

        logging_steps=1,

        eval_strategy="epoch",
        save_strategy="epoch",

        save_total_limit=2,

        # 3080 Ti 根据支持情况自动选
        bf16=use_bf16,
        fp16=not use_bf16,

        # 0.6B + LoRA 对 3080 Ti 不需要开
        gradient_checkpointing=False,

        max_length=512,

        # 只让 assistant 的回答产生 loss
        assistant_only_loss=True,

        report_to="none",

        seed=42,
        load_best_model_at_end=True,

        metric_for_best_model="eval_loss",

        greater_is_better=False,
    )


    # ==================================================
    # 6. SFT Trainer
    # ==================================================

    trainer = SFTTrainer(
        model=model,

        args=training_args,

        train_dataset=dataset["train"],
        eval_dataset=dataset["test"],

        processing_class=tokenizer,

        peft_config=lora_config,
    )


    # ==================================================
    # 7. 检查 LoRA 参数
    # ==================================================

    print()
    print("=" * 60)
    print("LoRA Trainable Parameters")
    print("=" * 60)

    trainer.model.print_trainable_parameters()


    # ==================================================
    # 8. Train
    # ==================================================

    print()
    print("=" * 60)
    print("Start Training")
    print("=" * 60)

    trainer.train()


    # ==================================================
    # 9. Save Adapter
    # ==================================================

    trainer.save_model(OUTPUT_DIR)

    tokenizer.save_pretrained(
        OUTPUT_DIR
    )


    # ==================================================
    # 10. GPU Memory
    # ==================================================

    if torch.cuda.is_available():

        allocated = (
            torch.cuda.max_memory_allocated()
            / 1024**3
        )

        reserved = (
            torch.cuda.max_memory_reserved()
            / 1024**3
        )

        print()
        print(
            f"Peak allocated memory: "
            f"{allocated:.2f} GB"
        )

        print(
            f"Peak reserved memory: "
            f"{reserved:.2f} GB"
        )


    print()
    print(
        f"Training finished. "
        f"LoRA adapter saved to: {OUTPUT_DIR}"
    )


if __name__ == "__main__":
    main()