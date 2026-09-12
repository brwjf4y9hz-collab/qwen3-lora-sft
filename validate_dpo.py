import json
from collections import Counter

TRAIN_FILE = "data/dpo/dpo_train_v0.jsonl"
EVAL_FILE = "data/eval_v2.jsonl"

def load_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

def one_message(messages, role, line_no, field):
    assert isinstance(messages, list) and len(messages) == 1, f"line {line_no}: {field} must be a one-message list"
    assert messages[0]["role"] == role, f"line {line_no}: {field} role must be {role}"
    text = messages[0]["content"].strip()
    assert text, f"line {line_no}: empty {field}"
    return text

def main():
    data = load_jsonl(TRAIN_FILE)
    eval_data = load_jsonl(EVAL_FILE)

    topics = Counter()
    prompts = []

    for i, x in enumerate(data, 1):
        assert "topic" in x
        prompt = one_message(x["prompt"], "user", i, "prompt")
        chosen = one_message(x["chosen"], "assistant", i, "chosen")
        rejected = one_message(x["rejected"], "assistant", i, "rejected")

        assert chosen != rejected, f"line {i}: chosen == rejected"

        prompts.append(prompt)
        topics[x["topic"]] += 1

    assert len(data) == 100, f"expected 100 pairs, got {len(data)}"
    assert len(prompts) == len(set(prompts)), "duplicate prompts found"

    eval_prompts = {x["prompt"].strip() for x in eval_data}
    leaks = sorted(set(prompts) & eval_prompts)

    print("Preference pairs:", len(data))
    print("Topic counts:", dict(topics))
    print("Exact prompt leaks with eval_v2:", len(leaks))

    for x in leaks:
        print("-", x)

    assert not leaks, "eval leakage detected"

    print("DPO dataset check passed!")

if __name__ == "__main__":
    main()
