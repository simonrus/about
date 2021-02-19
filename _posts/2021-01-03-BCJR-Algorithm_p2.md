---
layout: post
title: "BCJR Algorithm (Part 2)"
author: "Sergei Semenov"
categories: learning fec
image: 2020-12_BCJR_Trellis_Alphas.svg
---

# Introduction
[Previously](https://simonrus.github.io/about/learning/fec/BCJR-Algorithm_p1.html) we introduced Forward and Backward procedure and solved the first HMM problem. We also stated, that $$\alpha_t(i)$$ and $$\beta_t(i)$$ can help us in answering more complicated queries. 

In this post we would like to provide solution for the second HMM problem, namely: __What is sequence $$S = {S^1},{S^2}...{S^L}$$ that could "most likely" produce our sequence $$O = {O^1},{O^2}...{O^L}$$?__ 

This problem is also known as hidden states estimation.

# Hidden states estimation solution (ML way)
First, we may use Bayes' theorem to estimate the hidden state at moment $$t$$ given our observed sequence $$O$$. Taken into account, that $$(O^1...O^{t-1} \perp O^{t} \perp O^{t+1}...O^{L} \mid S^{t})$$, we may write:
$$
P(S^t = i \mid O^1, O^2,...,O^L) = \\
= \frac{P(O^1, O^2,...,O^{t-1} \mid S^t = i) \cdot P(O^{t} \mid S^t = i) \cdot P(O^{t+1}...O^{L} \mid S^t = i) P(S^t = i)}{P(O^1,O^2,...,O^L)} = \\
= \frac{P(O^1, O^2,...,O^{t} \mid S^t = i) \cdot P(O^{t+1}...O^{L} \mid S^t = i) \cdot P(S^t = i)}{P(O^1,O^2...O^L)} = \\
= \frac{P(O^1, O^2,...,O^{t}, S^t = i) \cdot P(O^{t+1}...O^{L} \mid S^t = i)}{P(O^1,O^2,...,O^L)} = \\
= \frac{\alpha_{t}(i)\beta_{t}(i)}{\sum\limits_{i} \alpha_{t}(i) \beta_{t}(i)}
$$

# Hidden transitions estimation solution (ML way)
If we decode an error-correcting code using its trellis representation, we are interested to estimate the transition probability between two consecutive hidden states, since it represents bits of codeword.

Taking 
$$P(S^{t-1} = i, S^t = j \mid O^1, O^2,...,O^L) = \\ \frac{P(O^1, O^2,...,O^{L} \mid S^{t-1} = i, S^t = j) \cdot P(S^{t-1} = i, S^t = j )}{P(O^1,O^2,...,O^L)}
$$


In a case of HMM, the following dependencies are met (we still use $$\perp$$ symbol instead of $$\perp \!\!\! \perp$$ just for simplicity):
1. $$O^1, O^2,...,O^{t-2} \perp O^{t-1} \mid S^{t-1}$$
2. $$O^{t-1} \perp S^{t} \mid S^{t-1}$$
3. $$O^{t} \perp S^{t-1} \mid S^{t}$$
4. $$O^{t} \perp S^{t+1} \mid S^{t}$$

![full graph](https://simonrus.github.io/about/assets/img/2021-01-03-HMM.svg "Graph"){:height="80%" width="80%"}

It allows us to represent nominator as :
$$\begin{aligned}  P&(O^1,  O^2,...,O^{L} \mid S^{t-1} = i, S^t = j) \cdot P(S^{t-1} = i, S^t = j ) = \\ =  & P(O^1, O^2,...,O^{t-2} \mid S^{t-1} = i, S^t = j) \cdot  P(O^{t-1} \mid S^{t-1} = i, S^t = j)\cdot \\ \cdot & P(O^{t} \mid S^{t-1} = i, S^t = j)\cdot P(O^{t+1},...,O^{L} \mid S^{t-1} = i, S^t = j) \cdot  P(S^{t-1} = i, S^t = j )= \\ =  & P(O^1, O^2,...,O^{t-2}, O^{t-1} \mid S^{t-1} = i)\cdot \\ \cdot & P(O^{t} \mid S^t = j)\cdot P(O^{t+1},...,O^{L} \mid S^t = j) \cdot  P(S^{t-1} = i) P(S^t = j \mid S^{t-1} = i)= \\ = & \alpha_{t-1}(i)  \cdot \beta_{t}(j) \cdot \omega_{i,j} \end{aligned}$$, where $$\omega_{i,j} = P(O^{t} \mid S^t = j) P(S^t = j \mid S^{t-1} = i) = B_{j,O_t} A_{j, i}$$

Finally, we have:
$$P(S^{t-1} = i, S^t = j \mid O^1, O^2,...,O^L) =\frac{\alpha_{t-1}(i)  \cdot \beta_{t}(j) \cdot \omega_{i,j}}{\sum\limits_{i} \alpha_{t}(i) \beta_{t}(i)}$$

Simple and beautiful, right?
# References 
1. L. R. Rabiner, “A tutorial on hidden Markov models and selected applications in speech recognition,” Proc. IEEE, vol. 77, no. 2, pp. 257–286, Feb. 1989, doi: 10.1109/5.18626.
2. L. Bahl, J. Cocke, F. Jelinek, and J. Raviv, “Optimal decoding of linear codes for minimizing symbol error rate (Corresp.),” IEEE Trans. Inform. Theory, vol. 20, no. 2, pp. 284–287, Mar. 1974, doi: 10.1109/TIT.1974.1055186.






*Last update:19 February 2021*
