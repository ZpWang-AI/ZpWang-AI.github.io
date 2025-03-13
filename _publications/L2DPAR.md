---
title: "Learning to Differentiate Pairwise-Argument Representations for Implicit Discourse Relation Recognition"
collection: publications
category: conferences
permalink: /publication/L2DPAR
excerpt: 'This paper proposes a joint learning framework that combines prototypical learning, adversarial learning, and hub-migration based redistribution to enhance the performance of Pre-trained Language Models (PLMs) for Implicit Discourse Relation Recognition (IDRR).'
date: 2024-10-21
venue: 'Proceedings of the 33rd ACM International Conference on Information and Knowledge Management (CIKM 2024)'
paperurl: 'https://doi.org/10.1145/3627673.3679584'
# citation: '' # "Zhipang Wang, Yu Hong, Yuxiang Lu, Xiabing Zhou, Jianmin Yao, and Guodong Zhou. 2024. Learning to Differentiate Pairwise-Argument Representations for Implicit Discourse Relation Recognition. In Proceedings of the 33rd ACM International Conference on Information and Knowledge Management (CIKM '24). Association for Computing Machinery, New York, NY, USA, 2503–2512."
---

<!-- [Code of Github](https://github.com/ZpWang-AI/L2DPAR) is coming soon. -->


## Implicit Discourse Relation Recognition: A Joint Learning Framework

Implicit Discourse Relation Recognition (IDRR) is a challenging task that involves recognizing relationships between texts without explicit connectives. This paper proposes a joint learning framework that combines prototypical learning, adversarial learning, and hub-migration based redistribution to enhance the performance of Pre-trained Language Models (PLMs) for IDRR. The framework is designed to produce more distinguishable argument representations, which is crucial for connective-free relation determination.

## Key Contributions:

* A joint learning framework that combines three learning methods to enhance PLMs for IDRR
Prototypical learning that uses contrastive learning to guide the encoder to produce more typical representations
* Adversarial learning that generates highly distracting examples to improve the robustness of the model
* Hub-migration based redistribution that disperses the centers of all classes in the feature space and drives in-class samples to converge towards the centers

## Experimental Results:

* The proposed framework achieves substantial improvements compared to BERT, RoBERTa, and DeBERTa baselines on PDTB 2.0, PDTB 3.0, and CoNLL-2016 datasets
* The framework outperforms previous work in the scenario of connective-free IDRR and obtains comparable performance to some of the connective-exposed IDRR models

## Conclusion:

This paper proposes a joint learning framework that enhances PLMs for IDRR by producing more distinguishable argument representations. The framework combines prototypical learning, adversarial learning, and hub-migration based redistribution to improve the performance of IDRR models. Experimental results demonstrate the effectiveness of the proposed framework, which achieves state-of-the-art performance on several benchmark datasets.