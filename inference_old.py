import torch

from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


MODEL_NAME = "/root/autodl-tmp/models/Qwen3-0.6B"
ADAPTER_PATH = "outputs/qwen3-0.6b-lora"


def main():
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True,
    )

    base_model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype="auto",
        device_map="auto",
        trust_remote_code=True,
    )

    model = PeftModel.from_pretrained(
        base_model,
        ADAPTER_PATH,
    )

    model.eval()

    question = "请用通俗语言解释Agent中的ReAct。"

    messages = [
        {
            "role": "user",
            "content": question,
        }
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    inputs = tokenizer(
        text,
        return_tensors="pt",
    ).to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=256,
            temperature=0.7,
            do_sample=True,
        )

    input_length = inputs["input_ids"].shape[1]

    generated_ids = outputs[0][input_length:]

    response = tokenizer.decode(
        generated_ids,
        skip_special_tokens=True,
    )

    print(response)


if __name__ == "__main__":
    main()
