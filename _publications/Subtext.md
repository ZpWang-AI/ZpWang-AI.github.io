---
title: "Using Subtext to Enhance Generative IDRR"
collection: publications
category: conferences
permalink: /publication/Subtext
excerpt: 'This paper introduces a Subtext-based Confidence-diagnosed Dual-channel Network (SCDN) for enhancing Implicit Discourse Relation Recognition (IDRR) by incorporating subtexts generated through LLaMA. The approach demonstrates significant improvements in recognizing semantic relations between argument pairs, highlighting the importance of subtexts as valuable contextual clues that enrich the understanding of implicit relations, ultimately resulting in higher F1-scores on benchmark datasets.'
date: 2025-07-1
venue: 'Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers) (ACL 2025)'
paperurl: 'https://aclanthology.org/2025.acl-short.35/'
# citation: '' # "Zhipang Wang, Yu Hong, Yuxiang Lu, Xiabing Zhou, Jianmin Yao, and Guodong Zhou. 2024. Learning to Differentiate Pairwise-Argument Representations for Implicit Discourse Relation Recognition. In Proceedings of the 33rd ACM International Conference on Information and Knowledge Management (CIKM '24). Association for Computing Machinery, New York, NY, USA, 2503–2512."
---

<!-- [Code of Github](https://github.com/ZpWang-AI/L2DPAR) is coming soon. -->


> **Zhipang Wang**, *Yu Hong, Weihao Sun, Guodong Zhou


## Motivation

The motivation behind this research stems from the need to enhance Implicit Discourse Relation Recognition (IDRR) by leveraging subtexts, which can offer deeper insights into the semantic relationships between argument pairs. Traditional models often overlook these connotative meanings, leading to suboptimal performance in recognizing implicit relations.

## Methodology

We introduced a Subtext-based Confidence-diagnosed Dual-channel Network (SCDN) that utilizes a generative approach with LLaMA to produce subtexts for argument pairs. The architecture consists of three models: Mα for subtext generation, Mβ for out-of-subtext IDRR, and Mλ for in-subtext IDRR. This dual-channel approach allows for a nuanced understanding of relations by reconciling outputs based on confidence levels.

## Experimental Results
Our experiments were conducted on the PDTB-2.0 and PDTB-3.0 datasets, where we evaluated the performance of our SCDN against existing benchmarks. The results demonstrated significant improvements in F1-scores compared to baseline models, affirming the effectiveness of incorporating subtexts in the IDRR task. An ablation study further confirmed that the use of subtexts enhances model performance across various relation types.

## Conclusion
In summary, our findings indicate that integrating subtexts into IDRR significantly strengthens the model's ability to discern implicit relations. This work not only contributes to the field of natural language processing by filling a gap in IDRR research but also sets the stage for future exploration of common-sense knowledge in subtext generation. Our approach opens avenues for improving relational understanding in NLP tasks, emphasizing the importance of semantic nuances in enhancing model performance.

