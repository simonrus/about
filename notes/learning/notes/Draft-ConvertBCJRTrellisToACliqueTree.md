---
title: Draft-ConvertBCJRTrellisToACliqueTree
created: '2020-12-23T10:52:35.499Z'
modified: '2020-12-23T10:52:55.611Z'
---

# Draft-ConvertBCJRTrellisToACliqueTree


## Convert trellis to a clique tree
The trellis can be viewed as a factor graph.


![full graph with alphas](https://simonrus.github.io/about/assets/img/2020-12_BCJR_Trellis_Alphas_as_CliqueTree.svg "Graph")

The nodes within one section form a singleton factor (denoted as $\Psi(i)$). 
The edges form a factor with 2 variables. 

![full graph with alphas](https://simonrus.github.io/about/assets/img/2020-12_BCJR_Trellis_Alphas_as_CliqueTree2.svg "Graph")

Factor $\Psi^{1}(S^{(1)})$ is:

| $S^{(1)}$ |value |
| ------ | --- |
| [$S_1$] | $\pi(S_1) \cdot P(S_1 \mid O_1)$ |
| [$S_2$] | $\pi(S_1) \cdot P(S_2 \mid O_1)$ |
| ... | ... |
| [$S_N$] | $\pi(S_1) \cdot P(S_N \mid O_1)$  |

Wait, please! How to find $P(S_i \mid O_1)$ if we know only $P(O_1 \mid S_i )$? Let's use Bayes Theorem for some time $t$ as follows:

$$P(S_i \mid \hat{O_t}) = \frac{P(\hat{O_t} \mid S_i ) \cdot P(S_i)} {P(\hat{O_t})} = P(\hat{O_t} \mid S_i ) \cdot y^{(t)}_{i}$$

So, our Factor $\Psi^{1}(S^{(1)})$ becomes:

| $S^{(1)}$ |value |
| ------ | --- |
| [$S_1$] | $\pi(S_1) \cdot P(S_1 \mid O_1) \cdot y^{(1)}_{1}$ |
| [$S_2$] | $\pi(S_1) \cdot P(S_2 \mid O_1) \cdot y^{(1)}_{2}$ |
| ... | ... |
| [$S_N$] | $\pi(S_1) \cdot P(S_N \mid O_1) \cdot y^{(1)}_{N}$  |


So, our Factor $\Psi^{2}(S^{(1)}, S^{(2)})$ is:

| $S^{(1)} S^{(1)}$ |value |
| ------ | --- |
| [$S_1, S_1$] | $\pi(S_1) \cdot P(S_1 \mid O_1) \cdot y^{(1)}_{1}$ |
| [$S_1, S_2$] | $\pi(S_1) \cdot P(S_2 \mid O_1) \cdot y^{(1)}_{2}$ |
| ... | ... |
| [$S_2, S_1$] | $\pi(S_1) \cdot P(S_2 \mid O_1) \cdot y^{(1)}_{2}$ |
| [$S_2, S_2$] | $\pi(S_1) \cdot P(S_2 \mid O_1) \cdot y^{(1)}_{2}$ |
| ... | ... |
| [$S_N, S_N$] | $\pi(S_1) \cdot P(S_N \mid O_1) \cdot y^{(1)}_{N}$  |


Factor $\phi$ has the same values for all variables a, has values from $A$ and contains values:
|  |value |
| ------ | --- |
| [1, 1] | $P(S_{1} \mid S_{1})$ |
| [1, 2] | $P(S_{2} \mid S_{1})$ |
| ... | ... |
| [N, N] | $P(S_{N} \mid S_{N})$ |

Factor $\pi$ also corresponds 1-to-1 to $\pi$ from HMM model

## Forward step as BP in a clique tree with factors

