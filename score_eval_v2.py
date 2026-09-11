import argparse
import json
from collections import defaultdict

def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f]

def norm(text):
    return text.lower().replace(" ", "")

def hit(answer, group):
    a = norm(answer)
    return any(norm(k) in a for k in group)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pred", required=True)
    parser.add_argument("--eval", default="data/eval_v2.jsonl")
    args = parser.parse_args()

    refs = {x["id"]: x for x in load_jsonl(args.eval)}
    preds = {x["id"]: x for x in load_jsonl(args.pred)}

    by_topic = defaultdict(list)
    rows = []

    for idx in sorted(refs):
        ref = refs[idx]
        pred = preds[idx]
        groups = ref["must_include_groups"]
        hits = [hit(pred["response"], g) for g in groups]
        score = sum(hits) / len(hits)
        by_topic[ref["topic"]].append(score)
        rows.append((idx, ref["topic"], score, hits, ref["prompt"], pred["response"]))

    overall = sum(r[2] for r in rows) / len(rows)

    print("\n=== Heuristic concept-coverage ===")
    for topic, values in by_topic.items():
        print(f"{topic:16s}: {sum(values)/len(values):.3f}")
    print(f"{'overall':16s}: {overall:.3f}")
    print("\n注意：这是关键词/概念覆盖初筛，不等于最终正确率；还需要人工或LLM-as-a-Judge复核。")

    report = args.pred.replace(".jsonl", "_score.md")
    with open(report, "w", encoding="utf-8") as f:
        f.write("# Eval V2 heuristic score\n\n")
        f.write(f"- Overall concept coverage: **{overall:.3f}**\n\n")
        for idx, topic, score, hits, prompt, response in rows:
            f.write(f"## {idx}. [{topic}] {prompt}\n\n")
            f.write(f"- Heuristic score: **{score:.2f}**\n")
            f.write(f"- Group hits: `{hits}`\n\n")
            f.write("### Model response\n\n")
            f.write(response + "\n\n")
            f.write("### Human review\n\n")
            f.write("- Correctness (0/1/2): TODO\n")
            f.write("- Completeness (0/1/2): TODO\n")
            f.write("- Hallucination (0/1): TODO\n")
            f.write("- Notes: TODO\n\n")

    print(f"Saved report: {report}")

if __name__ == "__main__":
    main()
