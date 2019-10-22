---
author: Malte Bonart
title: Strategies for dealing with high class imbalance
subtitle: <i class="fas fa-chart-pie"></i>
date: October 25, 2019
header-includes:
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.css" />
---

---

<div class="smallfont">
<p>This work and the underlying source code is available on <a href="https://github.com/bonartm/class-imbalance"> <i class="fab fa-github-square"></i>GitHub</a>.</p>
 
<p>This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.</p>

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />
</div>

### Example - credit card fraud detection

<iframe scrolling="no" style="border:none;" seamless="seamless" data-src="figures/age.html" height="450" width="100%"></iframe>

<div class="smallfont">
Only
</div>

### Challenges when dealing with high class imbalance


### Goals of this session


### Organization


### Confusion matrix


 &nbsp;| &nbsp;| Reality |&nbsp;
---|---|---|--- |---
&nbsp;|&nbsp;|1|0 |&nbsp;
Model|1|True positive TP|False positive FP |&nbsp;
&nbsp;|0|False negative FN|True negative TN |&nbsp;
&nbsp;| &nbsp;|$n_1$|$n_0$ | n


- Recall: $\frac{TP}{TP+FN}$
- Precision: $\frac{TP}{TP+FP}$
- Sensitivity: $\frac{TN}{FP+TN}

### Quiz - Simple baselines for the credit card challenge

What's the accuracy recall, precision, sensitivity, f1 score and balanced accuracy for a predictor that:

- only predicts $1$
- only predicts $0$
- predicts $1$ with probability of 

### Simple baselines for the credit card challenge

| only $1$ | only $0$ | $P(\hat{y}=1) = 0.0018$
---|---|---|---
accuracy | | |
precision | | |
recall | | |
sensitivity | | |
f1 score | | |
balanced accuracy | | |

### Varying the treshold

### `class_weight` parameter for LR and RF


### What's next?

