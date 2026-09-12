# Eval V2 heuristic score

- Overall concept coverage: **0.459**

## 1. [lora] 在LoRA里，如果把rank r增大，通常对可训练参数量、表达能力和显存开销分别有什么影响？

- Heuristic score: **0.50**
- Group hits: `[False, True, False, True]`

### Model response

rank增大通常会增加模型参数数量和显存占用，但可以降低训练时的参数梯度更新频率，从而降低显存开销。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 2. [lora] 为什么LoRA能明显减少训练显存，但不能让基座模型权重完全不占显存？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

即使LoRA只占基座权重的较小比例，训练时仍需要显存训练数据、LoRA参数和中间激活，因此显存限制仍然受限。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 3. [lora] LoRA中的ΔW=BA表达了什么含义？为什么这里称为低秩更新？

- Heuristic score: **0.75**
- Group hits: `[True, True, False, True]`

### Model response

ΔW=BA表示权重参数被更新为原始权重加上一个低秩矩阵B乘以一个低秩向量A，因此总更新量由矩阵秩决定。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 4. [lora] 如果LoRA的rank设置得过小，模型可能出现什么现象？

- Heuristic score: **0.00**
- Group hits: `[False, False]`

### Model response

可能无法有效学习Adapter参数，导致模型表现变差。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 5. [lora] 如果LoRA的rank设置得很大，在小数据集上可能有什么风险？

- Heuristic score: **0.67**
- Group hits: `[True, False, True]`

### Model response

模型参数过多，容易过拟合，尤其在小样本或低维任务中。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 6. [lora] LoRA里的target_modules决定了什么？

- Heuristic score: **0.67**
- Group hits: `[True, True, False]`

### Model response

它告诉LoRA哪些模块需要被训练，从而控制可训练参数数量和更新频率。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 7. [lora] LoRA和QLoRA在显存节省方式上最核心的区别是什么？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

QLoRA通常只训练少量Adapter权重，而LoRA通常训练大量基座参数。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 8. [lora] 为什么LoRA训练结束后通常只需要保存Adapter？

- Heuristic score: **0.33**
- Group hits: `[False, True, False]`

### Model response

Adapter只负责微调少量可训练参数，其余权重保持原样，因此不需要保存所有原始权重。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 9. [lora] LoRA里的lora_alpha主要控制什么？

- Heuristic score: **0.75**
- Group hits: `[False, True, True, True]`

### Model response

主要控制LoRA参数缩放比例，影响模型更新频率和参数规模。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 10. [lora] 如何用训练日志证明你做的是参数高效微调而不是全参数微调？

- Heuristic score: **0.33**
- Group hits: `[True, False, False]`

### Model response

通过记录训练过程中的损失、学习率、epoch、batch size、数据量和模型参数变化，可以对比不同配置下的表现，从而判断是否主要优化了可训练参数而不是固定模型结构。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 11. [post_training] SFT和预训练在数据形式与训练目标上分别有什么区别？

- Heuristic score: **0.40**
- Group hits: `[True, False, False, True, False]`

### Model response

SFT通常直接对少量示例进行监督更新，目标更偏向任务泛化；预训练通常在大量通用数据上进行多模态、多任务学习，目标更偏向模型能力泛化。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 12. [post_training] 为什么SFT项目不能只看train loss？

- Heuristic score: **0.50**
- Group hits: `[True, True, False, False]`

### Model response

因为train loss只反映过拟合，不能全面反映模型泛化能力、任务适配度或实际应用场景表现。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 13. [post_training] 训练loss下降而eval loss连续上升，最可能说明什么？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

可能因为过拟合、数据偏差或模型能力提升过快，需要结合验证集和测试集进一步分析。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 14. [post_training] 为什么不能把测试集原题加入训练集后再继续用同一测试集汇报效果？

- Heuristic score: **0.25**
- Group hits: `[False, False, False, True]`

### Model response

这样会导致训练数据和测试数据混用，可能产生数据偏差，影响模型泛化能力。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 15. [post_training] assistant_only_loss=True通常意味着什么？

- Heuristic score: **0.25**
- Group hits: `[False, True, False, False]`

### Model response

通常指只计算模型输出与目标的损失，不计算训练过程中的学习率、batch size、epoch等元信息。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 16. [post_training] SFT和DPO最核心的监督信号有什么区别？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

SFT主要通过反馈直接调整模型输出，而DPO通过对比不同候选回答，引导模型选择更符合目标的回复。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 17. [post_training] 为什么smoke test通过后，正式训练最好重新从Base Model开始？

- Heuristic score: **0.25**
- Group hits: `[True, False, False, False]`

### Model response

因为Smoke Test可能已经破坏了模型的某些关键能力，重新训练从头开始能更准确地评估新版本的性能。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 18. [post_training] train、validation、test三份数据分别承担什么角色？

- Heuristic score: **1.00**
- Group hits: `[True, True, True, True, True]`

### Model response

训练数据用于模型学习；验证数据用于调整超参数和选择模型；测试数据用于最终评估模型效果。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 19. [post_training] 为什么SFT数据里同一知识点最好设计多种问法？

- Heuristic score: **0.50**
- Group hits: `[True, False, False, True]`

### Model response

同一知识点的多种表达方式能覆盖不同语境、表达方式和用户意图，提高泛化能力。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 20. [post_training] 一个完整的SFT bad-case飞轮应该怎样循环？

- Heuristic score: **0.00**
- Group hits: `[False, False, False, False, False]`

### Model response

应该包含一个明确的错误、一个用户反馈、一个明确的纠正、一个新任务、一个重复错误、一个反馈循环，形成一个闭环。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 21. [attention] 请完整描述Scaled Dot-Product Attention从Q、K、V到输出的计算流程。

- Heuristic score: **0.40**
- Group hits: `[True, False, False, True, False]`

### Model response

1. 将Q、K、V标准化为归一化矩阵；2. 计算QK^T^T；3. 计算QK^T^T/√N；4. 计算K^TQ^T/√N；5. 计算QK^T/√N；6. 计算K^TQ/√N；7. 计算QK^T/√N；8. 计算QK^T/√N；9. 计算QK^T/√N；10. 计算QK^T/√N；11. 计算QK^T/√N；12. 计算QK^T/√N；13. 计算QK^T/√N；14. 计算QK^T/√N；15. 计算QK^T/√N；16. 计算QK^T/√N；17. 计算QK^T/√N；18. 计算QK^T/√N；19. 计算Q

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 22. [attention] 在Self-Attention中，Query、Key和Value各自承担什么角色？

- Heuristic score: **0.60**
- Group hits: `[True, True, True, False, False]`

### Model response

Query负责提取当前token的特征；Key负责计算Query和Query之间的相似度；Value负责将Query特征映射到对应Key的表示上。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 23. [attention] 为什么Attention分数要除以sqrt(d_k)？

- Heuristic score: **0.00**
- Group hits: `[False, False, False, False]`

### Model response

因为每个位置的Q和K向量长度相同，要比较它们的相对重要性，需要除以它们的平方根长度，以标准化。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 24. [attention] 一个token如何通过Self-Attention从整句话其他位置获取上下文信息？

- Heuristic score: **0.60**
- Group hits: `[True, True, False, True, False]`

### Model response

它通过计算与当前token的Q/K/V矩阵元素，将当前token与多个历史位置连接，最终得到一个包含上下文信息的输出。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 25. [attention] Multi-Head Attention为什么不是只用一个Attention头？

- Heuristic score: **0.50**
- Group hits: `[True, True, False, False]`

### Model response

因为不同头可以同时学习不同特征，从而提升模型对不同输入表示的建模能力。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 26. [attention] Causal Mask在自回归语言模型中具体阻止了什么？

- Heuristic score: **0.25**
- Group hits: `[True, False, False, False]`

### Model response

它屏蔽了未来位置的预测，防止模型在生成当前token时依赖已知未来token。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 27. [attention] Padding Mask和Causal Mask解决的问题有什么不同？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

Padding Mask限制哪些位置可以使用额外输入；Causal Mask限制哪些位置不能在当前时间步前看到。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 28. [attention] Self-Attention与Cross-Attention在Q、K、V来源上有什么区别？

- Heuristic score: **0.83**
- Group hits: `[True, True, True, True, True, False]`

### Model response

Self-Attention通常只从当前序列中获取Q/K/V；Cross-Attention通常从目标序列中获取Q/K/V。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 29. [attention] 为什么标准Self-Attention在序列长度n上常被说成O(n²)？

- Heuristic score: **0.00**
- Group hits: `[False, False, False, False]`

### Model response

因为每个位置需要与所有其他位置计算注意力分数，导致总计算量呈平方级增长。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 30. [attention] RoPE是怎样把位置信息作用到Attention里的？

- Heuristic score: **0.20**
- Group hits: `[False, False, False, False, True]`

### Model response

通过在Attention中添加位置偏移量，让位置信息以更自然的方式嵌入注意力权重中。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 31. [kv_cache] 自回归解码时，KV Cache到底缓存哪些张量？

- Heuristic score: **1.00**
- Group hits: `[True, True, True, True]`

### Model response

通常缓存当前token的K/V和Attention中间结果，以减少重复计算和显存开销。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 32. [kv_cache] 如果关闭KV Cache，每生成一个新token会重复计算什么？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

每生成新token时会重新计算当前历史token的注意力和位置信息，导致显存消耗急剧增加。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 33. [kv_cache] 为什么KV Cache能加速decode，却会额外占用显存？

- Heuristic score: **0.60**
- Group hits: `[True, True, False, True, False]`

### Model response

KV Cache存储了历史Key-Value对，这些数据在后续请求中被重复使用，因此显存占用主要来自缓存本身，而不是每次请求都重新计算。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 34. [kv_cache] LLM推理里的prefill和decode分别在做什么？

- Heuristic score: **0.40**
- Group hits: `[True, False, False, True, False]`

### Model response

prefill为后续token化做初始化，decode根据当前token选择后续token。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 35. [kv_cache] 为什么上下文越长，KV Cache通常越占显存？

- Heuristic score: **0.75**
- Group hits: `[True, True, True, False]`

### Model response

历史token需要保存更多的历史KV对，因此更长的上下文会增加需要存储的历史信息量。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 36. [kv_cache] 为什么batch size增大会提高KV Cache显存占用？

- Heuristic score: **0.75**
- Group hits: `[True, False, True, True]`

### Model response

每个batch中更多的token被处理，每个token需要保存更多KV Cache，因此显存占用增加。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 37. [kv_cache] KV Cache和FlashAttention分别主要优化什么问题？

- Heuristic score: **0.60**
- Group hits: `[True, False, True, True, False]`

### Model response

KV Cache主要优化显存和延迟；FlashAttention主要优化计算开销和内存访问效率。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 38. [kv_cache] 为什么KV Cache通常不需要缓存历史Query？

- Heuristic score: **0.75**
- Group hits: `[False, True, True, True]`

### Model response

因为历史Query可能被多次查询，但历史KV可能只被使用一次。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 39. [kv_cache] GQA/MQA为什么能减小KV Cache？

- Heuristic score: **0.40**
- Group hits: `[True, True, False, False, False]`

### Model response

GQA直接计算QK^T，不需要额外计算QK^T和QK^T，因此可以共享KV Cache。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 40. [kv_cache] 正确实现KV Cache会不会改变模型理论上的生成结果？为什么？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

不会。模型内部的KV Cache主要影响计算效率和稳定性，它不改变模型对输入和输出的抽象表示或理论推理能力。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 41. [agent] 请用搜索实时天气的例子描述一次完整ReAct循环。

- Heuristic score: **0.20**
- Group hits: `[False, False, False, True, False]`

### Model response

用户输入天气查询，系统搜索实时数据并返回结果；用户确认后，系统调用天气API更新状态并返回最终答案。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 42. [agent] LLM Agent相比普通聊天模型，多出来的核心能力通常有哪些？

- Heuristic score: **0.20**
- Group hits: `[True, False, False, False, False]`

### Model response

可以执行任务、规划行动、管理状态、抽象问题、推理和决策，从而完成更复杂或多阶段的任务。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 43. [agent] 如果模型声称“我已经调用天气API并得到25℃”，但系统实际上没有执行任何工具，这属于什么问题？

- Heuristic score: **0.25**
- Group hits: `[False, False, True, False]`

### Model response

属于工具调用失败，模型应明确说明实际调用失败并提供错误信息。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 44. [agent] Agent调用工具后为什么必须读取Observation再决定下一步？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

工具返回结果后才可验证是否符合预期、调整策略或继续下一步，因此必须先读取结果才能继续推理。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 45. [agent] Agent中的Planning解决的是什么问题？

- Heuristic score: **0.25**
- Group hits: `[True, False, False, False]`

### Model response

规划负责确定执行路径、资源分配、约束条件和目标，使Agent能够合理地从初始状态出发，逐步完成任务。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 46. [agent] Agent中的Memory和当前上下文窗口有什么区别？

- Heuristic score: **0.75**
- Group hits: `[True, True, False, True]`

### Model response

Memory保存历史输入和输出，当前上下文窗口是当前已知对话历史，用于后续查询。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 47. [agent] 评估Tool Use时，除了最终任务成功率，还可以看哪些指标？

- Heuristic score: **0.00**
- Group hits: `[False, False, False, False]`

### Model response

可解释性、调用频率、延迟、资源消耗、错误率、调用格式是否正确、是否符合约束、是否符合预期输出、是否符合格式要求、是否符合工具限制、是否符合工具文档、是否符合工具版本、是否符合工具评测标准。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 48. [agent] 为什么Agent系统通常要设置最大步数或终止条件？

- Heuristic score: **0.25**
- Group hits: `[False, True, False, False]`

### Model response

这可以防止无限循环或过拟合，同时控制模型行为和计算开销。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 49. [agent] Reasoning、Action和Observation三者在Agent里分别是什么？

- Heuristic score: **0.75**
- Group hits: `[True, True, True, False]`

### Model response

Reasoning是Agent根据当前信息和目标选择下一步行为；Action是执行具体操作；Observation是Agent完成操作后获得的结果反馈。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 50. [agent] 如果一个搜索工具连续两次返回无关结果，Agent应该怎样处理？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

应检查是否重复或过时，同时明确说明已排除结果，并引导用户重新查询或提供更具体需求。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

