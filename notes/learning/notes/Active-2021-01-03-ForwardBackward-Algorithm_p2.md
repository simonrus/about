---
title: Active-2021-01-03-ForwardBackward-Algorithm_p2
created: '2021-01-03T09:19:05.796Z'
modified: '2021-05-16T14:28:35.921Z'
---

# Active-2021-01-03-ForwardBackward-Algorithm_p2

---
layout: post
title: "ForwardBackward Algorithm (Part 2)"
author: "Sergei Semenov"
categories: learning fec
image: 2020-12_HMM_Trellis_Alphas.svg
---

# Introduction
[Previously](https://simonrus.github.io/about/learning/fec/ForwardBackward-Algorithm_p1.html) we introduced Forward and Backward procedure and solved the first HMM problem. We also stated, that $\alpha_t(i)$ and $\beta_t(i)$ can help us in answering more complicated queries. 

In this post we would like to provide solution for the second HMM problem, namely: __What is sequence $S = {S^1},{S^2}...{S^L}$ that could "most likely" produce our sequence $O = {O^1},{O^2}...{O^L}$?__ 

This problem is also known as hidden states estimation.

# Hidden states estimation
First, we may use Bayes' theorem to estimate the hidden state at moment $t$ given our observed sequence $O$. Taken into account, that $(O^1...O^{t-1} \perp O^{t} \perp O^{t+1}...O^{L} \mid S^{t})$, we may write:
$$
P(S^t = i \mid O^1, O^2,...,O^L) = \\
= \frac{P(O^1, O^2,...,O^{t-1} \mid S^t = i) \cdot P(O^{t} \mid S^t = i) \cdot P(O^{t+1}...O^{L} \mid S^t = i) P(S^t = i)}{P(O^1,O^2,...,O^L)} = \\
= \frac{P(O^1, O^2,...,O^{t} \mid S^t = i) \cdot P(O^{t+1}...O^{L} \mid S^t = i) \cdot P(S^t = i)}{P(O^1,O^2...O^L)} = \\
= \frac{P(O^1, O^2,...,O^{t}, S^t = i) \cdot P(O^{t+1}...O^{L} \mid S^t = i)}{P(O^1,O^2,...,O^L)} = \\
= \frac{\alpha_{t}(i)\beta_{t}(i)}{\sum\limits_{i} \alpha_{t}(i) \beta_{t}(i)}
$$

# Hidden transitions estimation 
Also, we may be interested in estimating a transition probability between two consecutive hidden states. We can derive the following equation:
$$P(S^{t-1} = i, S^t = j \mid O^1, O^2,...,O^L) = \\ \frac{P(O^1, O^2,...,O^{L} \mid S^{t-1} = i, S^t = j) \cdot P(S^{t-1} = i, S^t = j )}{P(O^1,O^2,...,O^L)}
$$

Let's explore conditional independencies in a given HMM:
![full graph](https://simonrus.github.io/about/assets/img/2021-01-03-HMM.svg "Graph"){:height="80%" width="80%"}

We have following independecies (we still use $\perp$ symbol instead of $\perp \!\!\! \perp$ just for simplicity):
1. $O^1, O^2,...,O^{t-2} \perp O^{t-1} \mid S^{t-1}$
2. $O^{t-1} \perp S^{t} \mid S^{t-1}$
3. $O^{t} \perp S^{t-1} \mid S^{t}$
4. $O^{t} \perp S^{t+1} \mid S^{t}$

Now we can rewrite nominator as:
$$\begin{aligned}  P&(O^1,  O^2,...,O^{L} \mid S^{t-1} = i, S^t = j) \cdot P(S^{t-1} = i, S^t = j ) = \\ =  & P(O^1, O^2,...,O^{t-2} \mid S^{t-1} = i, S^t = j) \cdot  P(O^{t-1} \mid S^{t-1} = i, S^t = j)\cdot \\ \cdot & P(O^{t} \mid S^{t-1} = i, S^t = j)\cdot P(O^{t+1},...,O^{L} \mid S^{t-1} = i, S^t = j) \cdot  P(S^{t-1} = i, S^t = j )= \\ =  & P(O^1, O^2,...,O^{t-2}, O^{t-1} \mid S^{t-1} = i)\cdot \\ \cdot & P(O^{t} \mid S^t = j)\cdot P(O^{t+1},...,O^{L} \mid S^t = j) \cdot  P(S^{t-1} = i) P(S^t = j \mid S^{t-1} = i)= \\ = & \alpha_{t-1}(i)  \cdot \beta_{t}(j) \cdot \omega_{i,j} \end{aligned}$$, where $\omega_{i,j} = P(O^{t} \mid S^t = j) P(S^t = j \mid S^{t-1} = i) = B_{j,O_t} A_{j, i}$

Finally, we have:
$$P(S^{t-1} = i, S^t = j \mid O^1, O^2,...,O^L) =\frac{\alpha_{t-1}(i)  \cdot \beta_{t}(j) \cdot \omega_{i,j}}{\sum\limits_{i} \alpha_{t}(i) \beta_{t}(i)}$$

Simple and beautiful, right?

# References 
1. L. R. Rabiner, “A tutorial on hidden Markov models and selected applications in speech recognition,” Proc. IEEE, vol. 77, no. 2, pp. 257–286, Feb. 1989, doi: 10.1109/5.18626.
2. B.-J. Yoon, “Hidden Markov Models and their Applications in Biological Sequence Analysis,” CG, vol. 10, no. 6, pp. 402–415, Sep. 2009, doi: 10.2174/138920209789177575.






