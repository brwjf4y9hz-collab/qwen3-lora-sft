# Eval V2 heuristic score

- Overall concept coverage: **0.523**

## 1. [lora] 在LoRA里，如果把rank r增大，通常对可训练参数量、表达能力和显存开销分别有什么影响？

- Heuristic score: **0.50**
- Group hits: `[False, True, False, True]`

### Model response

rank r增大通常会增加模型参数数量和显存占用，但可以降低每个token的token嵌入维度，从而降低显存开销；同时降低训练时需要训练的token数量，降低显存开销。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 2. [lora] 为什么LoRA能明显减少训练显存，但不能让基座模型权重完全不占显存？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

即使LoRA只占基座权重的较小比例，训练时仍需要显存训练参数、LoRA参数和额外的初始化、缓存、缓存更新和模型保存。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 3. [lora] LoRA中的ΔW=BA表达了什么含义？为什么这里称为低秩更新？

- Heuristic score: **0.75**
- Group hits: `[True, True, False, True]`

### Model response

ΔW=BA表示权重参数主要由B和A构成，因此更新量只包含少量秩，因此称为低秩更新。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 4. [lora] 如果LoRA的rank设置得过小，模型可能出现什么现象？

- Heuristic score: **0.00**
- Group hits: `[False, False]`

### Model response

可能无法有效学习Adapter参数，导致Adapter能力过强或过弱，甚至出现过拟合或过拟合。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 5. [lora] 如果LoRA的rank设置得很大，在小数据集上可能有什么风险？

- Heuristic score: **0.67**
- Group hits: `[True, False, True]`

### Model response

模型参数过多、训练成本高，容易过拟合；小数据集可能无法充分学习任务分布，导致泛化能力不足。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 6. [lora] LoRA里的target_modules决定了什么？

- Heuristic score: **0.67**
- Group hits: `[True, True, False]`

### Model response

它决定了哪些模块会被冻结，哪些模块会通过LoRA微调。通常会冻结一部分基础模块，只更新目标模块。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 7. [lora] LoRA和QLoRA在显存节省方式上最核心的区别是什么？

- Heuristic score: **0.75**
- Group hits: `[True, False, True, True]`

### Model response

QLoRA通常通过冻结少量基座参数并微调大量Adapter参数，减少基座显存；LoRA则通过冻结少量基座参数并微调少量基座参数，因此QLoRA通常更高效地利用基座显存。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 8. [lora] 为什么LoRA训练结束后通常只需要保存Adapter？

- Heuristic score: **0.67**
- Group hits: `[True, True, False]`

### Model response

Adapter只负责微调少量低秩权重，其余权重由基座模型独立训练，因此不需要保存基座模型。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 9. [lora] LoRA里的lora_alpha主要控制什么？

- Heuristic score: **0.25**
- Group hits: `[False, False, True, False]`

### Model response

主要控制LoRA权重衰减程度，越大越强，影响可训练参数变化幅度和训练稳定性。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 10. [lora] 如何用训练日志证明你做的是参数高效微调而不是全参数微调？

- Heuristic score: **0.00**
- Group hits: `[False, False, False]`

### Model response

可以对比训练时显存、梯度更新频率、epoch完成率、warm-up步长、学习率衰减和模型大小，说明是否主要在训练过程中动态调整参数。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 11. [post_training] SFT和预训练在数据形式与训练目标上分别有什么区别？

- Heuristic score: **0.40**
- Group hits: `[True, False, False, True, False]`

### Model response

SFT通常直接对少量示例进行监督反馈，目标是让模型快速掌握新任务；预训练通常在大量通用数据上进行，目标是让模型具备通用能力。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 12. [post_training] 为什么SFT项目不能只看train loss？

- Heuristic score: **0.75**
- Group hits: `[True, True, True, False]`

### Model response

train loss只反映过拟合，但过拟合还可能影响验证/测试泛化、模型质量、可解释性、资源消耗和可维护性。需要综合多个指标和指标评估方式。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 13. [post_training] 训练loss下降而eval loss连续上升，最可能说明什么？

- Heuristic score: **0.50**
- Group hits: `[True, True, False, False]`

### Model response

可能因为训练数据过拟合，模型开始过度学习局部最优解，此时需要增加正则化、早停或换一个更合适的任务/数据集。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 14. [post_training] 为什么不能把测试集原题加入训练集后再继续用同一测试集汇报效果？

- Heuristic score: **0.25**
- Group hits: `[False, False, False, True]`

### Model response

训练集通常用于泛化，测试集应独立验证模型是否真正泛化，而不是重复使用它来训练或评估。重复使用测试集会影响结果，因为它可能包含更多已知数据，导致过拟合。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 15. [post_training] assistant_only_loss=True通常意味着什么？

- Heuristic score: **0.25**
- Group hits: `[False, True, False, False]`

### Model response

通常指只计算模型输出与目标的损失，不计算训练过程中的学习率、batch size、epoch等元信息，因此更关注任务性能。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 16. [post_training] SFT和DPO最核心的监督信号有什么区别？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

SFT主要通过反馈直接调整模型对任务的期望；DPO通过任务和对齐信息选择最优回答；因此DPO更关注对齐和任务一致性，而SFT更关注模型对任务目标的映射。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 17. [post_training] 为什么smoke test通过后，正式训练最好重新从Base Model开始？

- Heuristic score: **0.25**
- Group hits: `[True, False, False, False]`

### Model response

因为Smoke Test可能已经破坏了模型对关键任务的稳定性，重新从基础模型开始可以更准确地评估正式任务的表现。

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

- Heuristic score: **0.25**
- Group hits: `[True, False, False, False]`

### Model response

同一知识点的多种表达方式能覆盖不同语境、语气和意图，降低对单一种类模型的依赖，同时增加数据多样性。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 20. [post_training] 一个完整的SFT bad-case飞轮应该怎样循环？

- Heuristic score: **0.00**
- Group hits: `[False, False, False, False, False]`

### Model response

应该包含一个bad-case错误、一个用户反馈、一个改进目标、一个新prompt、一个新测试、一个新bad-case，形成一个闭环。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 21. [attention] 请完整描述Scaled Dot-Product Attention从Q、K、V到输出的计算流程。

- Heuristic score: **0.60**
- Group hits: `[True, False, False, True, True]`

### Model response

1. 将Q和K标准化为归一化矩阵；2. 计算QK^T矩阵的分数；3. 将分数与V标准化后拼接；4. 计算Attention Scores的加权平均；5. 将输出重新归一化并拼接。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 22. [attention] 在Self-Attention中，Query、Key和Value各自承担什么角色？

- Heuristic score: **0.60**
- Group hits: `[True, True, True, False, False]`

### Model response

Query负责提取当前token的特征；Key负责计算Query和Query之间的QKdot；Value负责将QKdot结果映射到对应token的输出。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 23. [attention] 为什么Attention分数要除以sqrt(d_k)？

- Heuristic score: **0.25**
- Group hits: `[True, False, False, False]`

### Model response

因为每个位置的Q和K向量长度都为d_k，要比较它们的相对重要性，需要除以它们的平方根，使分数在0到1之间。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 24. [attention] 一个token如何通过Self-Attention从整句话其他位置获取上下文信息？

- Heuristic score: **0.80**
- Group hits: `[True, True, False, True, True]`

### Model response

模型通过当前token的Q/K/V向量与历史token的Q/K/V进行加权相加，最终得到当前token的注意力权重分布，再根据这些分布选择下一个token。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 25. [attention] Multi-Head Attention为什么不是只用一个Attention头？

- Heuristic score: **0.50**
- Group hits: `[True, True, False, False]`

### Model response

因为不同头可以同时学习不同特征，因此需要独立计算和保存每个头的信息。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 26. [attention] Causal Mask在自回归语言模型中具体阻止了什么？

- Heuristic score: **0.25**
- Group hits: `[True, False, False, False]`

### Model response

它屏蔽了未来位置与当前位置的注意力，防止模型在生成当前token时依赖未来token，从而避免循环依赖。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 27. [attention] Padding Mask和Causal Mask解决的问题有什么不同？

- Heuristic score: **0.75**
- Group hits: `[True, False, True, True]`

### Model response

Padding Mask用于屏蔽不需要的padding位置；Causal Mask用于屏蔽未来位置；两者共同防止位置越界。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 28. [attention] Self-Attention与Cross-Attention在Q、K、V来源上有什么区别？

- Heuristic score: **0.83**
- Group hits: `[True, True, True, True, True, False]`

### Model response

Self-Attention通常只从当前序列的Q/K/V中提取信息；Cross-Attention通常从目标序列的Q/K/V中提取信息，再通过注意力对目标序列的V进行加权聚合。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 29. [attention] 为什么标准Self-Attention在序列长度n上常被说成O(n²)？

- Heuristic score: **0.75**
- Group hits: `[True, True, True, False]`

### Model response

因为每个位置需要与n-1个位置计算Q/KQ和K/KQ，总计算量为O(n²)。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 30. [attention] RoPE是怎样把位置信息作用到Attention里的？

- Heuristic score: **0.80**
- Group hits: `[True, True, True, False, True]`

### Model response

RoPE通过对位置向量进行线性变换，让位置信息以Q/K的权重传递到Attention的K和V中，从而让位置对注意力权重产生非线性影响。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 31. [kv_cache] 自回归解码时，KV Cache到底缓存哪些张量？

- Heuristic score: **1.00**
- Group hits: `[True, True, True, True]`

### Model response

通常缓存当前token的K/V、Attention和位置信息，以减少重复计算和显存开销。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 32. [kv_cache] 如果关闭KV Cache，每生成一个新token会重复计算什么？

- Heuristic score: **1.00**
- Group hits: `[True, True, True, True]`

### Model response

每生成新token时会重新计算当前历史token的K/V，因此会重复计算历史token的KV缓存。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 33. [kv_cache] 为什么KV Cache能加速decode，却会额外占用显存？

- Heuristic score: **0.80**
- Group hits: `[True, True, True, True, False]`

### Model response

KV Cache保存了历史K/V，可以复用这些历史信息，避免重复计算；显存占用主要由Cache大小决定，而不是重复计算的token数量。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 34. [kv_cache] LLM推理里的prefill和decode分别在做什么？

- Heuristic score: **0.40**
- Group hits: `[True, False, False, True, False]`

### Model response

prefill为后续token化做初始化；decode根据当前token选择后续token，可能需要多次token化和tokenization。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 35. [kv_cache] 为什么上下文越长，KV Cache通常越占显存？

- Heuristic score: **0.75**
- Group hits: `[True, True, True, False]`

### Model response

历史token的KV Cache需要保存历史token的Q/K对，历史长度增加时这些历史对和KV Cache的大小也增加。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 36. [kv_cache] 为什么batch size增大会提高KV Cache显存占用？

- Heuristic score: **0.75**
- Group hits: `[True, False, True, True]`

### Model response

每个batch中更多的token被处理，每个token需要保存更多历史KV，因此显存占用会增加。

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

- Heuristic score: **1.00**
- Group hits: `[True, True, True, True]`

### Model response

历史Query可能被多次重复使用，但KV Cache只保存当前需要的Key和Value，而不是历史Query。这样可以减少重复计算和存储开销。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 39. [kv_cache] GQA/MQA为什么能减小KV Cache？

- Heuristic score: **0.20**
- Group hits: `[True, False, False, False, False]`

### Model response

GQA直接计算QK^T，不需要额外计算QK^T和KV Cache；MQA直接计算QK^T和KV Cache，但需要额外存储和缓存。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 40. [kv_cache] 正确实现KV Cache会不会改变模型理论上的生成结果？为什么？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

不会。模型内部的KV Cache主要影响计算效率和稳定性，它不改变模型对输入和输出的抽象表示或理论能力。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 41. [agent] 请用搜索实时天气的例子描述一次完整ReAct循环。

- Heuristic score: **0.20**
- Group hits: `[False, False, False, True, False]`

### Model response

用户输入天气查询，系统搜索实时数据并返回结果；用户确认后，系统调用天气API更新状态并返回最终天气信息。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 42. [agent] LLM Agent相比普通聊天模型，多出来的核心能力通常有哪些？

- Heuristic score: **0.40**
- Group hits: `[True, True, False, False, False]`

### Model response

可以执行任务、规划路径、管理状态、抽象问题、调用外部工具、模拟场景、生成摘要、生成代码、管理资源、管理任务进度、管理多任务、管理上下文、管理资源、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务、管理上下文、管理任务进度、管理多任务

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 43. [agent] 如果模型声称“我已经调用天气API并得到25℃”，但系统实际上没有执行任何工具，这属于什么问题？

- Heuristic score: **0.25**
- Group hits: `[False, False, True, False]`

### Model response

属于工具调用失败，模型应明确说明实际调用失败，而不是简单重复模型声明。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 44. [agent] Agent调用工具后为什么必须读取Observation再决定下一步？

- Heuristic score: **0.50**
- Group hits: `[True, True, False, False]`

### Model response

工具返回的Observation通常包含关键信息，这些信息需要根据当前任务目标和上下文进一步判断下一步应做什么。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 45. [agent] Agent中的Planning解决的是什么问题？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

规划负责确定任务步骤、选择哪些工具、如何分配资源、如何处理约束和目标，以使系统能够有效执行下一步。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 46. [agent] Agent中的Memory和当前上下文窗口有什么区别？

- Heuristic score: **0.75**
- Group hits: `[True, True, False, True]`

### Model response

Memory保存历史输入和输出，当前上下文窗口是当前已知对话历史，用于后续查询；历史窗口可能包含更多历史信息，但当前对话可能已经结束。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 47. [agent] 评估Tool Use时，除了最终任务成功率，还可以看哪些指标？

- Heuristic score: **0.00**
- Group hits: `[False, False, False, False]`

### Model response

可复现性、工具调用格式是否正确、是否符合预期、是否包含必要的上下文、是否返回了预期格式、是否使用了正确的工具、是否验证了工具调用的正确性、是否在工具失败时提供了有意义的错误信息、是否在工具失败时返回了合理的错误提示。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 48. [agent] 为什么Agent系统通常要设置最大步数或终止条件？

- Heuristic score: **0.25**
- Group hits: `[False, True, False, False]`

### Model response

这可以防止无限循环、过拟合或资源耗尽，同时控制模型行为范围。

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

应检查是否因重复请求或过早返回而重复执行，同时记录失败次数并根据策略调整策略，例如增加失败次数阈值或限制重复请求次数。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

