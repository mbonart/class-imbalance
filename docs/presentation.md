---
author: Malte Bonart
title: Evaluation of binary classifiers under high class imbalance
subtitle: malte@bonart.de
date: October 25, 2019
header-includes:
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.css" />
---

### Evaluation of binary classifiers under high class imbalance

<div class="smallfont">

Under high class imbalance it is crucial to select proper evaluation metrics that both reflect the asymmetry and match with your classification goal. In this lesson we will explore various evaluation metrics, compare our model to simple baselines and take a closer look at the trade-off between precision and recall.

<p>This work and the underlying source code is available on <a href="https://github.com/mbonart/class-imbalance"> <i class="fab fa-github-square"></i>GitHub</a>.</p>
 
<p>This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.</p>

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />
</div>

### Goals

- given a confusion matrix, calculate the accuracy, precision, recall and f1 score
- vary the threshold of the classification rule and examine the effect on precision and recall
- describe possible classification goals and how they are related to the trade-off between precision and recall


### {data-background-iframe="https://www.kaggle.com/mlg-ulb/creditcardfraud/data"}


### Write one keyword on a card

- Which real-world problems contain imbalanced classes?
- What methods did you already use when confronted with high class imbalance?
- For binary classification, which evaluation metrics do you know?

### Let's start

1. Clone the repository
```bash
git clone https://github.com/mbonart/class-imbalance.git
cd class-imbalance
```
2. Download the data
```bash
python src/download_data.py
```
3. Have a look at the script and run
```bash
python src/threshold.py
```
> What is the result of the script?

### Classification rule

$$
G(f(x_i)) = \mathbf{I}(f(x_i) > b)
$$

### Group work

- examine the precision, recall and f1 score for different thresholds $b$
- use the script `src/threshold.py` 
- write your results on cards

### {data-background-iframe="www/precision-recall-curve.html"}



### [‘imbalanced_learn’ package](https://imbalanced-learn.org/en/stable) for advanced sampling strategies

- Oversampling: Random, [SMOTE](https://imbalanced-learn.readthedocs.io/en/stable/generated/imblearn.over_sampling.SMOTE.html)
- Undersampling: Random, [Tomeklinks](https://imbalanced-learn.readthedocs.io/en/stable/generated/imblearn.under_sampling.TomekLinks.html)
- [Combinations](https://imbalanced-learn.readthedocs.io/en/stable/api.html#module-imblearn.combine)

## Outlier detection?

- [OnceClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html)
- [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html)

## What do you think?

> "Hey, look at my awesome classifiers, it achieves almost 99% accuracy?"