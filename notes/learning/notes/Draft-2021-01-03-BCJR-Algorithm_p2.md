---
title: Draft-2021-01-03-BCJR-Algorithm_p2
created: '2021-01-03T09:19:05.796Z'
modified: '2021-02-19T07:47:32.124Z'
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

In this post we would like to provide solution for the second HMM problem, namely: __What is sequence $S = {S^1},{S^2}...{S^L}$ that could "most likely" produce our sequence $O = {O^1},{O^2}...{O^L}$?__ 

This problem is also known as hidden states estimation.

# Hidden states estimation solution (ML way).
First we may use Bayes' theorem to estimate the hidden state at moment $t$ given our observed sequence $O$. Taken into account, that $(O^1...O^{t-1} \perp O^{t} \perp O^{t+1}...O^{L} \mid S^{t})$, we may write:
$$
P(S^t = i \mid O^1, O^2,...,O^L) = \\
= \frac{P(O^1, O^2,...,O^{t-1} \mid S^t = i) \cdot P(O^{t} \mid S^t = i) \cdot P(O^{t+1}...O^{L} \mid S^t = i) P(S^t = i)}{P(O^1,O^2,...,O^L)} = \\
= \frac{P(O^1, O^2,...,O^{t} \mid S^t = i) \cdot P(O^{t+1}...O^{L} \mid S^t = i) \cdot P(S^t = i)}{P(O^1,O^2...O^L)} = \\
= \frac{P(O^1, O^2,...,O^{t}, S^t = i) \cdot P(O^{t+1}...O^{L} \mid S^t = i)}{P(O^1,O^2,...,O^L)} = \\
= \frac{\alpha_{t}(i)\beta_{t}(i)}{\sum\limits_{i} \alpha_{t}(i) \beta_{t}(i)}
$$

# Hidden states estimation solution (MAP way).




# References 
1. L. R. Rabiner, “A tutorial on hidden Markov models and selected applications in speech recognition,” Proc. IEEE, vol. 77, no. 2, pp. 257–286, Feb. 1989, doi: 10.1109/5.18626.




