# Qwen3-0.6B Post-training Pipeline

基于 **Qwen3-0.6B**，完成从数据构造、LoRA SFT、固定评测、Bad Case Analysis 到 DPO Preference Optimization 的完整后训练闭环。

本项目重点不是单纯“跑通微调”，而是通过多轮实验分析：

* SFT 为什么会过拟合
* 数据规模与数据质量如何影响能力分布
* 如何使用固定测试集进行公平对比
* 为什么训练指标不能直接代表下游效果
* DPO 如何使用 frozen reference policy
* Easy Negative 与 Hard Negative preference data 的差异
* Preference Accuracy 为什么不等于真实生成正确率
* 如何通过 Bad Case Analysis 驱动下一轮数据构造

---

## 1. Pipeline

```text
Qwen3-0.6B Base
      │
      ▼
SFT V0
10 samples
      │
      ├── Severe Overfitting
      ▼
Bad Case Analysis
      │
      ▼
SFT V1
100 samples
      │
      ├── Targeted Repair
      ▼
Fixed 50-question Eval Set
      │
      ▼
SFT V2
300 multi-format samples
      │
      ├── Correction
      ├── Scenario
      ├── Mechanism
      ├── Formula
      └── Comparison
      │
      ▼
DPO V0
100 Easy Preference Pairs
      │
      ├── External Eval Improved
      ▼
DPO V1
100 Hard-Negative Preference Pairs
      │
      └── Preference Objective Improved
          but External Generalization Regressed
```

---

# 2. Base Model

```text
Qwen/Qwen3-0.6B
```

Local path:

```text
/root/autodl-tmp/models/Qwen3-0.6B
```

Training environment:

```text
PyTorch      2.14.0+cu126
Transformers 5.17.0
PEFT         0.20.0
TRL          1.12.0
GPU          RTX 3080 Ti
```

BF16 is enabled.

---

# 3. LoRA Configuration

All main SFT experiments use:

```python
LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules="all-linear",
)
```

Typical trainable parameters:

```text
~10.09M trainable parameters

~1.6% of total model parameters
```

This allows parameter-efficient post-training while keeping most Base Model parameters frozen.

---

# 4. SFT V0 — Smoke Test

Dataset:

```text
10 samples
```

Topics:

```text
LLM
Transformer
SFT
LoRA
Agent
ReAct
Tool Use
```

Training configuration:

```text
epochs = 10
learning_rate = 2e-4
batch_size = 2
assistant_only_loss = True
```

Validation loss:

```text
Epoch 1: 2.957
Epoch 2: 2.826  ← best
Epoch 3: 2.937
Epoch 4: 3.213
...
Epoch 10: 4.398
```

Training loss continued decreasing while validation loss increased sharply.

Conclusion:

```text
Train Loss ↓
Eval Loss  ↑
→ Severe Overfitting
```

This experiment demonstrated that:

> Lower training loss does not necessarily mean better generalization.

V0 was therefore treated only as a smoke test.

---

# 5. SFT V1 — Bad Case Driven Data Expansion

Dataset increased from:

```text
10 → 100 samples
```

Five domains:

```text
LoRA          20
Post-training 20
Attention     20
KV Cache      20
Agent         20
```

Training:

```text
epochs = 3
learning_rate = 1e-4
```

Validation loss:

```text
Epoch 1: 2.718
Epoch 2: 2.693  ← best
Epoch 3: 2.772
```

The best checkpoint was selected based on validation loss.

Important observation:

```text
Epoch 2 > Epoch 3
```

Therefore the last checkpoint was not necessarily the best checkpoint.

---

# 6. Fixed Evaluation Set

To avoid changing evaluation criteria between experiments, a fixed 50-question test set was created:

```text
LoRA          10
Post-training 10
Attention     10
KV Cache      10
Agent         10
```

Training datasets were checked against this test set.

```text
Exact prompt leakage = 0
```

Generation settings were kept fixed:

```text
enable_thinking = False
do_sample = False
max_new_tokens = 256
```

This reduces evaluation noise between checkpoints.

---

# 7. SFT V2 — Multi-format Training Data

Dataset:

```text
300 samples
```

Distribution:

```text
Post-training 90
Attention     80
LoRA          50
KV Cache      40
Agent         40
```

Data types include:

```text
Definition
Scenario
Comparison
Why
Correction
Risk
Mechanism
Formula
```

Training:

```text
epochs = 2
learning_rate = 1e-4
```

Results:

```text
Epoch 1 eval loss: 2.541
Epoch 2 eval loss: 2.531
```

No severe V0-style overfitting was observed.

However, evaluation revealed an important phenomenon:

> Increasing data quantity did not uniformly improve all domains.

For example, Attention improved while some other abilities regressed.

This showed that:

```text
Data Distribution
      ↓
Capability Distribution
```

---

# 8. Heuristic Evaluation

A lightweight concept-coverage evaluator was built using required keyword/concept groups.

Important:

> This metric is only an automatic screening metric and is NOT equivalent to correctness.

Results:

| Model  |  LoRA |  Post | Attention | KV Cache | Agent | Overall |
| ------ | ----: | ----: | --------: | -------: | ----: | ------: |
| Base   | 0.550 | 0.535 |     0.538 |    0.685 | 0.475 |   0.557 |
| SFT V0 | 0.425 | 0.455 |     0.407 |    0.505 | 0.340 |   0.426 |
| SFT V1 | 0.492 | 0.385 |     0.397 |    0.640 | 0.435 |   0.470 |
| SFT V2 | 0.433 | 0.395 |     0.507 |    0.655 | 0.365 |   0.471 |

The Base Model sometimes receives a higher heuristic score because longer responses may contain more target keywords.

Therefore heuristic scores were supplemented with manual Bad Case Analysis.

---

# 9. DPO

## Preference Data Format

Each DPO record contains:

```json
{
  "prompt": [...],
  "chosen": [...],
  "rejected": [...]
}
```

DPO optimizes:

```text
chosen > rejected
```

while remaining anchored to a frozen Reference Policy.

Conceptually:

```text
Policy:
SFT-V2 + DPO updates

Reference:
SFT-V2 frozen
```

---

# 10. PEFT Reference Policy Design

The project uses:

```text
TRL 1.12.0
PEFT 0.20.0
```

When an existing PEFT model is passed to `DPOTrainer` with:

```python
ref_model=None
```

TRL copies the pretrained SFT adapter into a frozen reference adapter.

Therefore memory layout becomes:

```text
                    Policy LoRA
                   /
Qwen3 Base Model --
                   \
                    Reference LoRA
```

Only one full Base Model is required.

This avoids keeping two complete 0.6B models in GPU memory.

---

# 11. DPO V0 — Easy Negatives

Dataset:

```text
100 preference pairs
```

Examples of rejected responses contained obvious factual errors.

Training configuration:

```text
epochs = 2
learning_rate = 5e-6
beta = 0.1
loss_type = sigmoid
```

Validation:

```text
Epoch 1:
eval_loss             = 0.3573
reward_accuracy       = 0.95
reward_margin         = 0.935

Epoch 2:
eval_loss             = 0.2885
reward_accuracy       = 1.00
reward_margin         = 1.207
```

The DPO preference objective was successfully optimized.

External fixed evaluation:

```text
SFT V2:  0.471
DPO V0:  0.523
```

Improvement:

```text
+0.052
```

Domain changes:

```text
LoRA          0.433 → 0.475
Post-training 0.395 → 0.415
Attention     0.507 → 0.613
KV Cache      0.655 → 0.700
Agent         0.365 → 0.410
```

All five domains improved over SFT V2.

---

# 12. DPO V1 — Hard Negative Ablation

To investigate preference-data quality, DPO V1 kept all training hyperparameters fixed and modified only the preference-pair difficulty.

Instead of:

```text
Correct Answer
vs
Obviously Wrong Answer
```

Hard negatives used:

```text
Mostly Correct Answer
vs
Mostly Correct + One Critical Error
```

Both DPO V0 and DPO V1 start independently from SFT V2.

```text
SFT V2
├── DPO V0 Easy Negatives
└── DPO V1 Hard Negatives
```

This creates a clean data-quality ablation.

Training results:

```text
Epoch 1:
eval_loss       = 0.5516
reward_accuracy = 1.00
reward_margin   = 0.310

Epoch 2:
eval_loss       = 0.4949
reward_accuracy = 1.00
reward_margin   = 0.455
```

Hard negatives produced much smaller margins than Easy Negatives, showing that the preference task was more difficult.

However, fixed external evaluation decreased:

| Model  |  LoRA |  Post | Attention |    KV | Agent |   Overall |
| ------ | ----: | ----: | --------: | ----: | ----: | --------: |
| DPO V0 | 0.475 | 0.415 |     0.613 | 0.700 | 0.410 | **0.523** |
| DPO V1 | 0.500 | 0.415 |     0.388 | 0.625 | 0.365 | **0.459** |

This demonstrates:

> Better optimization of the preference objective does not guarantee better downstream generation quality.

---

# 13. Main Findings

## Finding 1 — Training Loss ≠ Generalization

SFT V0:

```text
train loss ↓
eval loss ↑
```

Severe overfitting occurred despite low training loss.

---

## Finding 2 — More Data ≠ Uniform Improvement

```text
100 samples → 300 samples
```

did not improve every domain.

Capability distribution strongly depended on training-data distribution.

---

## Finding 3 — Automatic Metrics ≠ Correctness

Keyword coverage sometimes rated factually incorrect answers highly.

Therefore evaluation should combine:

```text
Automatic Metrics
+
Manual / LLM-as-a-Judge
+
Bad Case Analysis
```

---

## Finding 4 — DPO Training Metrics ≠ Downstream Accuracy

DPO V1 achieved:

```text
Preference Accuracy = 1.0
```

but external evaluation dropped to:

```text
0.459
```

Therefore:

```text
Preference Objective
≠
Open-ended Generation Correctness
```

---

## Finding 5 — Harder Preference Data Is Not Always Better

Hard negatives improved some fine-grained LoRA behavior but degraded Attention, KV Cache and Agent performance.

Preference-data difficulty must match model capacity and target behavior.

---

## Finding 6 — DPO Is Not Primarily Knowledge Injection

DPO helped the model prefer better responses, but did not reliably teach concepts that the small Base Model did not understand well.

Persistent weaknesses included:

```text
Cross-Attention
RoPE
GQA / MQA
Prefill / Decode
Tool Hallucination
```

This suggests that SFT / continued pretraining is more appropriate for introducing missing knowledge, while DPO is more suited to preference and behavior alignment.

---

# 14. Final Model Selection

Final selected checkpoint:

```text
outputs/qwen3-0.6b-dpo-v0
```

Reason:

```text
SFT V2       0.471
DPO V0       0.523
DPO V1 Hard  0.459
```

DPO V0 achieved the best external post-training evaluation among the fine-tuned models.

DPO V1 was retained as an ablation / failed experiment rather than selected as the production checkpoint.

---

# 15. Project Takeaways

This project implemented a complete post-training loop:

```text
Data Construction
      ↓
SFT
      ↓
Evaluation
      ↓
Bad Case Analysis
      ↓
Data Improvement
      ↓
SFT
      ↓
Preference Data
      ↓
DPO
      ↓
External Evaluation
      ↓
Ablation
      ↓
Final Model Selection
```

The core lesson is:

> Post-training is not simply “lower the loss”. The real work is designing data, maintaining clean evaluation, analyzing failure patterns, and determining whether training improvements actually transfer to downstream behavior.
