# Eval V2 heuristic score

- Overall concept coverage: **0.426**

## 1. [lora] 在LoRA里，如果把rank r增大，通常对可训练参数量、表达能力和显存开销分别有什么影响？

- Heuristic score: **0.75**
- Group hits: `[True, False, True, True]`

### Model response

通常，rank r增大通常会降低显存开销、降低可训练参数量、通常会降低表达能力。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 2. [lora] 为什么LoRA能明显减少训练显存，但不能让基座模型权重完全不占显存？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

因为LoRA只训练少量新增参数，因此显存和计算开销通常可以忽略不计，但基座模型的权重仍然需要显存和计算，因此不能完全完全不占显存。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 3. [lora] LoRA中的ΔW=BA表达了什么含义？为什么这里称为低秩更新？

- Heuristic score: **0.75**
- Group hits: `[True, True, False, True]`

### Model response

ΔW=BA表达了低秩矩阵B的秩，即新增参数W的秩等于B的秩。因为B是秩r的矩阵，所以新增参数W的秩也r，因此称为低秩更新。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 4. [lora] 如果LoRA的rank设置得过小，模型可能出现什么现象？

- Heuristic score: **0.50**
- Group hits: `[True, False]`

### Model response

模型可能出现显存和计算开销增加，以及可训练参数和表达能力下降。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 5. [lora] 如果LoRA的rank设置得很大，在小数据集上可能有什么风险？

- Heuristic score: **0.67**
- Group hits: `[True, True, False]`

### Model response

可能显存和计算开销增加，模型表达能力下降。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 6. [lora] LoRA里的target_modules决定了什么？

- Heuristic score: **0.33**
- Group hits: `[True, False, False]`

### Model response

target_modules决定了LoRA低秩矩阵的秩，从而影响可训练参数和表达能力。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 7. [lora] LoRA和QLoRA在显存节省方式上最核心的区别是什么？

- Heuristic score: **0.25**
- Group hits: `[False, False, False, True]`

### Model response

显存使用率

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 8. [lora] 为什么LoRA训练结束后通常只需要保存Adapter？

- Heuristic score: **0.00**
- Group hits: `[False, False, False]`

### Model response

因为LoRA只训练新增的神经元，通常可以完全忽略其他部分，因此只需要保存和训练LoRA参数，以节省显存和计算资源。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 9. [lora] LoRA里的lora_alpha主要控制什么？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

lora_alpha主要控制LoRA参数量，是定义LoRA低秩矩阵秩r的超参数。r越大，可训练参数和表达能力通常越强，但显存和计算开销也会增加。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 10. [lora] 如何用训练日志证明你做的是参数高效微调而不是全参数微调？

- Heuristic score: **0.00**
- Group hits: `[False, False, False]`

### Model response

通过分析训练过程中显存、计算和模型存储的使用情况，可以判断是否使用了预训练模型的参数并进行微调，从而证明是参数高效微调。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 11. [post_training] SFT和预训练在数据形式与训练目标上分别有什么区别？

- Heuristic score: **0.80**
- Group hits: `[True, True, False, True, True]`

### Model response

预训练主要使用大规模无标注语料学习语言结构、词汇和语法，而SFT使用高质量指令与回答数据继续训练模型，使其学会按照用户指令完成任务。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 12. [post_training] 为什么SFT项目不能只看train loss？

- Heuristic score: **0.75**
- Group hits: `[True, True, True, False]`

### Model response

因为训练数据可能包含噪声或不相关样本，这些会影响模型训练效果和泛化能力，因此需要结合验证集和测试集进行评估。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 13. [post_training] 训练loss下降而eval loss连续上升，最可能说明什么？

- Heuristic score: **0.50**
- Group hits: `[False, True, True, False]`

### Model response

显式可训练参数过多或模型结构过于复杂，导致显存和计算开销增加，同时可能因为训练显式参数的显存和计算开销增加，从而使得显式训练损失下降，但显式验证损失可能持续上升。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 14. [post_training] 为什么不能把测试集原题加入训练集后再继续用同一测试集汇报效果？

- Heuristic score: **0.00**
- Group hits: `[False, False, False, False]`

### Model response

因为测试集通常不包含训练数据，加入测试集后，模型可能无法充分利用其未训练的特征和数据，导致评估结果不准确。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 15. [post_training] assistant_only_loss=True通常意味着什么？

- Heuristic score: **0.25**
- Group hits: `[False, True, False, False]`

### Model response

通常表示模型仅使用输入输出样本的损失计算损失函数，并忽略其他潜在影响。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 16. [post_training] SFT和DPO最核心的监督信号有什么区别？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

SFT使用显式指令或标签继续训练模型，而DPO利用问答或推理任务中的输出继续训练模型。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 17. [post_training] 为什么smoke test通过后，正式训练最好重新从Base Model开始？

- Heuristic score: **0.50**
- Group hits: `[True, False, False, True]`

### Model response

因为Smoke Test通常使用简单、无标注的数据和任务，能够快速发现模型在实际任务中的表现和问题，而正式训练通常需要更多高质量的数据和任务，能够更好地训练模型并提高性能。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 18. [post_training] train、validation、test三份数据分别承担什么角色？

- Heuristic score: **1.00**
- Group hits: `[True, True, True, True, True]`

### Model response

train数据用于训练神经网络模型，validation数据用于评估模型性能并调整超参数，test数据通常用于最终评估模型在未使用训练和测试数据集上的表现。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 19. [post_training] 为什么SFT数据里同一知识点最好设计多种问法？

- Heuristic score: **0.25**
- Group hits: `[True, False, False, False]`

### Model response

因为同一知识点通常可以通过多种问法出现，不同的问法可以捕捉不同的语义或表达方式，从而提高模型对知识点的理解和记忆效果。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 20. [post_training] 一个完整的SFT bad-case飞轮应该怎样循环？

- Heuristic score: **0.00**
- Group hits: `[False, False, False, False, False]`

### Model response

循环输入并继续使用SFT模型中的完整故事

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 21. [attention] 请完整描述Scaled Dot-Product Attention从Q、K、V到输出的计算流程。

- Heuristic score: **0.40**
- Group hits: `[True, False, False, True, False]`

### Model response

Scaled Dot-Product Attention从Q、K、V到输出的计算流程如下：

1. 计算QK矩阵，得到QK矩阵的平方根，得到SQ，即QK的向量化表示。
2. 计算SV矩阵，即K的向量化表示与Q的向量化表示的点积，再取平方根，得到SV。
3. 计算SQ和SV的乘积，得到注意力权重矩阵AT。
4. 将AT中的元素进行归一化，得到最终的输出矩阵。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 22. [attention] 在Self-Attention中，Query、Key和Value各自承担什么角色？

- Heuristic score: **0.60**
- Group hits: `[True, True, True, False, False]`

### Model response

Query、Key和Value各自承担输入到注意力向量和注意力向量到输出的线性变换，是Self-Attention模型中注意力计算的核心参数。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 23. [attention] 为什么Attention分数要除以sqrt(d_k)？

- Heuristic score: **0.25**
- Group hits: `[True, False, False, False]`

### Model response

因为注意力权重通常以指数形式分布，而使用sqrt(d_k)作为分母可以保持注意力分数的计算简洁性和有效性。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 24. [attention] 一个token如何通过Self-Attention从整句话其他位置获取上下文信息？

- Heuristic score: **0.00**
- Group hits: `[False, False, False, False, False]`

### Model response

通过Self-Attention建模序列中不同位置之间的关系，可以利用注意力权重捕捉到的上下文信息。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 25. [attention] Multi-Head Attention为什么不是只用一个Attention头？

- Heuristic score: **0.75**
- Group hits: `[True, True, True, False]`

### Model response

因为Multi-Head Attention可以使用不同的注意力头来捕捉不同特征之间的关系，从而通常能够更好地建模数据中的复杂模式。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 26. [attention] Causal Mask在自回归语言模型中具体阻止了什么？

- Heuristic score: **0.00**
- Group hits: `[False, False, False, False]`

### Model response

Causal Mask阻止模型预测下一个字符，从而避免因果倒置。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 27. [attention] Padding Mask和Causal Mask解决的问题有什么不同？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

Padding Mask用于屏蔽输入序列中未开始或未结束的部分，而Causal Mask用于屏蔽输入序列中不连续的位置，从而确保模型只处理连续输入。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 28. [attention] Self-Attention与Cross-Attention在Q、K、V来源上有什么区别？

- Heuristic score: **0.67**
- Group hits: `[True, False, True, True, True, False]`

### Model response

Self-Attention使用Q、K、V三个输入张量，而Cross-Attention通常只使用Q和K，不包含V。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 29. [attention] 为什么标准Self-Attention在序列长度n上常被说成O(n²)？

- Heuristic score: **0.50**
- Group hits: `[True, False, False, True]`

### Model response

因为Self-Attention中的位置注意力矩阵需要n²个元素，因此序列长度n上常被说成O(n²)。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 30. [attention] RoPE是怎样把位置信息作用到Attention里的？

- Heuristic score: **0.40**
- Group hits: `[True, False, False, False, True]`

### Model response

RoPE通过计算序列中每个位置与注意力索引之间的向量点积，从而将位置信息作用到Attention中。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 31. [kv_cache] 自回归解码时，KV Cache到底缓存哪些张量？

- Heuristic score: **0.50**
- Group hits: `[True, True, False, False]`

### Model response

KV Cache缓存了前向传播中使用到的输入序列的键和值向量。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 32. [kv_cache] 如果关闭KV Cache，每生成一个新token会重复计算什么？

- Heuristic score: **0.50**
- Group hits: `[False, True, True, False]`

### Model response

每生成一个新token会重复计算前一个token的输入输出状态。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 33. [kv_cache] 为什么KV Cache能加速decode，却会额外占用显存？

- Heuristic score: **0.40**
- Group hits: `[False, True, False, True, False]`

### Model response

因为KV Cache存储了模型参数的前向插值，当需要继续推理时，显存和计算开销会增加，但通常显存和计算开销是显存和计算开销的函数，因此显存和计算开销通常会增加，但显存是显存的函数，因此显存通常会增加。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 34. [kv_cache] LLM推理里的prefill和decode分别在做什么？

- Heuristic score: **0.40**
- Group hits: `[True, False, False, True, False]`

### Model response

prefill填充输入，decode继续推理。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 35. [kv_cache] 为什么上下文越长，KV Cache通常越占显存？

- Heuristic score: **0.25**
- Group hits: `[False, False, True, False]`

### Model response

因为上下文长度增加，模型需要存储更多的前向插入和键值对，这会增加显存和存储开销。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 36. [kv_cache] 为什么batch size增大会提高KV Cache显存占用？

- Heuristic score: **0.75**
- Group hits: `[True, False, True, True]`

### Model response

因为更大的batch size通常会使用更多的显存和更少的缓存空间，因此显存和KV Cache显存占用通常会增加。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 37. [kv_cache] KV Cache和FlashAttention分别主要优化什么问题？

- Heuristic score: **0.60**
- Group hits: `[True, False, True, True, False]`

### Model response

KV Cache主要优化内存访问效率和模型参数的高效存储与计算，而FlashAttention主要优化序列注意力计算的高效性和计算开销。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 38. [kv_cache] 为什么KV Cache通常不需要缓存历史Query？

- Heuristic score: **0.75**
- Group hits: `[False, True, True, True]`

### Model response

因为KV Cache中的键值对通常已经经过显存或内存的缓存，不再需要再次使用，因此通常不需要显存或内存缓存，因此KV Cache通常不需要缓存历史Query。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 39. [kv_cache] GQA/MQA为什么能减小KV Cache？

- Heuristic score: **0.40**
- Group hits: `[True, False, False, False, True]`

### Model response

因为GQA和MQA模型只使用输入序列的前一部分来计算注意力，因此可以显存和计算开销更低，从而减少对KV Cache的依赖。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 40. [kv_cache] 正确实现KV Cache会不会改变模型理论上的生成结果？为什么？

- Heuristic score: **0.50**
- Group hits: `[True, False, True, False]`

### Model response

不会。因为KV Cache只存储前向计算中使用的键值对，不会影响模型的显存、计算或推理结果，因此不会改变理论上的生成结果。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 41. [agent] 请用搜索实时天气的例子描述一次完整ReAct循环。

- Heuristic score: **0.20**
- Group hits: `[False, False, False, True, False]`

### Model response

示例：搜索实时天气发现北京当前温度为22°C，降水概率为65%。然后使用该信息训练模型，生成预测未来1天的天气情况，最后验证模型是否符合搜索结果，若符合则输出最终天气预测结果。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 42. [agent] LLM Agent相比普通聊天模型，多出来的核心能力通常有哪些？

- Heuristic score: **0.20**
- Group hits: `[True, False, False, False, False]`

### Model response

1. 状态空间表示与管理能力  
2. 状态转移函数建模能力  
3. 策略搜索与执行能力  
4. 知识与推理能力（部分）

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 43. [agent] 如果模型声称“我已经调用天气API并得到25℃”，但系统实际上没有执行任何工具，这属于什么问题？

- Heuristic score: **0.25**
- Group hits: `[False, False, True, False]`

### Model response

工具调用未完成或未执行

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 44. [agent] Agent调用工具后为什么必须读取Observation再决定下一步？

- Heuristic score: **0.75**
- Group hits: `[True, True, True, False]`

### Model response

因为Observation提供了工具执行后的状态和结果，帮助Agent判断是否继续执行或终止当前任务。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 45. [agent] Agent中的Planning解决的是什么问题？

- Heuristic score: **0.00**
- Group hits: `[False, False, False, False]`

### Model response

Planning解决的是如何、何时、何地完成任务，以及如何利用现有或可获得的资源和约束条件完成任务。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 46. [agent] Agent中的Memory和当前上下文窗口有什么区别？

- Heuristic score: **0.75**
- Group hits: `[True, True, False, True]`

### Model response

Memory存储了历史输入和输出，而当前上下文窗口显示最新的连续输入输出。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 47. [agent] 评估Tool Use时，除了最终任务成功率，还可以看哪些指标？

- Heuristic score: **0.00**
- Group hits: `[False, False, False, False]`

### Model response

看工具调用的准确性、效率和结果是否符合预期。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 48. [agent] 为什么Agent系统通常要设置最大步数或终止条件？

- Heuristic score: **0.25**
- Group hits: `[True, False, False, False]`

### Model response

因为Agent系统通常需要完成指定任务，而任务可能在输入输出、状态或时间上被限制，设置最大步数或终止条件可以确保系统不超限并保持合理运行。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 49. [agent] Reasoning、Action和Observation三者在Agent里分别是什么？

- Heuristic score: **0.75**
- Group hits: `[True, True, True, False]`

### Model response

Reasoning是Agent根据输入和输出推导出下一步行动的逻辑，Action是Agent根据推理选择或尝试执行的步骤，Observation是Agent完成Action后获得或系统反馈的最新状态。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

## 50. [agent] 如果一个搜索工具连续两次返回无关结果，Agent应该怎样处理？

- Heuristic score: **0.25**
- Group hits: `[False, False, True, False]`

### Model response

Agent可以尝试调整搜索关键词、增加搜索参数或使用不同的搜索方法来获取更相关的结果。

### Human review

- Correctness (0/1/2): TODO
- Completeness (0/1/2): TODO
- Hallucination (0/1): TODO
- Notes: TODO

