---
title: Draft-2021-01-03-BCJR-Algorithm_p2
created: '2021-01-03T09:19:05.796Z'
modified: '2021-01-03T13:04:45.246Z'
---

# Draft-2021-01-03-BCJR-Algorithm_p2

---
layout: post
title: "BCJR Algorithm (Part 2)"
author: "Sergei Semenov"
categories: learning fec
image: 2020-12_BCJR_Trellis_Alphas.svg
---

# Introduction
[Previously](https://simonrus.github.io/about/learning/fec/BCJR-Algorithm_p1.html) we introduced Forward and Backward procedure and solved the first HMM problem. We also stated, that $\alpha_t(i)$ and $\beta_t(i)$ can help us in answering more complicated queries. 

In this post we would like to provide solution for the second HMM problem, namely: What is sequence $S = {S^1},{S^2}...{S^L}$ that could "most likely" produce our sequence $O = {O^1},{O^2}...{O^L}$? This problem is also known as hidden states estimation.

# Hidden states estimation solution (ML way).
First we may use Chain Rule and Bayes' theorem to estimate the hidden state at moment $t$ given our observed sequence $O$:
$$
P(S^t = i \mid O^1, O^2,...,O^L) = \\
= P(S^t = i \mid O^1, O^2,...,O^t) \cdot P(S^t = i \mid O^{t+1}, O^{t+2},...,O^L) = \\
= \frac{P(S^t = i,O^1, O^2,...,O^t)}{P(O^1, O^2,...,O^t)} \cdot \frac{P(O^{t+1}, O^{t+2},...,O^L \mid S^t = i ) \cdot P(S^t = i)}{P(O^{t+1}, O^{t+2},...,O^L)} = \\
= \frac{\alpha_t(i) \cdot \beta_t(i)}{P(O^{1}, O^{2},...,O^L)} \cdot P(S^t = i) 
$$

That looks cool, because:
1. $P(S^t = i)$ - prior probability.
2. $P(O^{1}, O^{2},...,O^L) = \sum_{i} \alpha_{L}(i)$ or $\beta_{O}$.

It can be also noticed, that all terms 

Now we may find to

# Hidden states estimation solution (MAP way).




# References 
1. L. R. Rabiner, “A tutorial on hidden Markov models and selected applications in speech recognition,” Proc. IEEE, vol. 77, no. 2, pp. 257–286, Feb. 1989, doi: 10.1109/5.18626.




