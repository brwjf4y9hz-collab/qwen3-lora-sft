import json
from pathlib import Path


BASE_FILE = "results/baseline.jsonl"
SFT_FILE = "results/sft.jsonl"
OUTPUT_FILE = "results/comparison.md"


def load_jsonl(path):
    data = {}

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            data[item["id"]] = item

    return data


def main():
    base = load_jsonl(BASE_FILE)
    sft = load_jsonl(SFT_FILE)

    lines = []

    lines.append("# Base vs LoRA-SFT Evaluation\n")

    for idx in sorted(base.keys()):

        prompt = base[idx]["prompt"]
        base_response = base[idx]["response"]
        sft_response = sft[idx]["response"]

        lines.append(f"## Case {idx}\n")
        lines.append(f"### Prompt\n{prompt}\n")

        lines.append("### Base\n")
        lines.append(base_response)
        lines.append("\n")

        lines.append("### LoRA-SFT\n")
        lines.append(sft_response)
        lines.append("\n")

        lines.append("### Analysis\n")
        lines.append("- Result: TODO")
        lines.append("- Error type: TODO")
        lines.append("- Improvement: TODO")
        lines.append("- Next data action: TODO\n")

        lines.append("---\n")

    Path(OUTPUT_FILE).write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    print(f"Comparison saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()