import json
import sys
from collections import Counter

TRAIN_FILE = "data/train_v2.jsonl"
EVAL_FILE = "data/eval_v2.jsonl"

TARGET = {
    "post_training": 90,
    "attention": 80,
    "lora": 50,
    "kv_cache": 40,
    "agent": 40,
}

def load_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

def main():
    train = load_jsonl(TRAIN_FILE)
    eval_data = load_jsonl(EVAL_FILE)

    print("Train samples:", len(train))

    topic_counts = Counter()
    type_counts = Counter()
    prompts = []

    for i, x in enumerate(train, 1):
        assert "topic" in x, f"line {i}: missing topic"
        assert "type" in x, f"line {i}: missing type"
        assert "messages" in x, f"line {i}: missing messages"
        assert len(x["messages"]) == 2, f"line {i}: messages length != 2"
        assert x["messages"][0]["role"] == "user", f"line {i}: first role != user"
        assert x["messages"][1]["role"] == "assistant", f"line {i}: second role != assistant"

        q = x["messages"][0]["content"].strip()
        a = x["messages"][1]["content"].strip()
        assert q, f"line {i}: empty prompt"
        assert a, f"line {i}: empty answer"

        prompts.append(q)
        topic_counts[x["topic"]] += 1
        type_counts[x["type"]] += 1

    print("\nTopic counts:")
    for k, v in topic_counts.items():
        print(f"  {k:16s}: {v}")

    print("\nType counts:")
    for k, v in type_counts.most_common():
        print(f"  {k:16s}: {v}")

    assert len(train) == 300, f"expected 300, got {len(train)}"
    assert topic_counts == Counter(TARGET), f"topic counts mismatch: {topic_counts}"
    assert len(prompts) == len(set(prompts)), "duplicate prompts in train_v2"

    eval_prompts = {x["prompt"].strip() for x in eval_data}
    leaks = sorted(set(prompts) & eval_prompts)

    print("\nExact prompt leaks with eval_v2:", len(leaks))
    for x in leaks:
        print("  -", x)

    assert not leaks, "exact eval leakage detected"

    print("\nDataset V2 check passed!")

if __name__ == "__main__":
    main()
