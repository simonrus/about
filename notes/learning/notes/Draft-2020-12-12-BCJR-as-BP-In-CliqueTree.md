---
title: Draft-2020-12-12-BCJR-as-BP-In-CliqueTree
created: '2020-11-30T08:19:27.713Z'
modified: '2020-12-13T20:14:44.738Z'
---

# Draft-2020-12-12-BCJR-as-BP-In-CliqueTree


---
layout: post
title: "BCJR as Belief Propagation in Clique Trees"
author: "Sergei Semenov"
categories: learning
image: 2020-07-PGM_Logo.jpg
---

# Introduction
We have already elaborated about [the properties of BP in CliqueTrees](https://simonrus.github.io/about/learning/PGM-p2-w2-BP-In-CliqueTrees.html).

Let us make a next step and see how we can derive BCJR algorithm.

# Sum-Product 
In the post ["Introduction to Hidden Markov Models"](https://simonrus.github.io/about/learning/Introduction-to-HMM.html), we have raised the first problem: "How do we compute the probability that the observed sequence was produced by a given HMM?". Or in the mathematical form, we need to find:
$$P(\hat{O_1},\hat{O_2}...\hat{O_L} \mid \lambda)$$

_"If you don't know what to do, start with joint distribution"_ (c) Mackey. But we don't know hidden states ($S_1, S_2 ... S_L$). Let's introduce them like as they are marginalized out:
$$P(\hat{O_1},\hat{O_2}...\hat{O_L}) = 
\sum_{{S^{(1)}},{S^{(2)}}...{S^{(L)}}}P({S^{(1)}},{S^{(2)}} ... {S^{(L)}}, \hat{O_1},\hat{O_2}...\hat{O_L}) \tag{1} $$

It can be easily seen, that above equation computes the sum over all possible states and has the complexity is $O(L \cdot N^{L})$. 

Now we can apply the distributive property and chain-rule as follows:
$$ \sum_{{S^{(1)}},{S^{(2)}}...{S^{(L)}}}P({S^{(1)}},{S^{(2)}} ... {S^{(L)}}, \hat{O_1},\hat{O_2}...\hat{O_L}) = \\
= \sum_{{S^{(1)}},{S^{(2)}}, ... {S^{(L)}}}P({S^{(1)}})P(\hat{O_1}\mid{S^{(1)}}) P({S^{(2)} | S^{(1)}})P(\hat{O_2}\mid{S^{(2)}})...P({S_L | S_{L-1}})P(\hat{O_L}\mid{S^{(L)}}) ) = \\
= \sum_{S^{(1)}}\pi({S^{(1)}})P(\hat{O_1}\mid{S^{(1)}}) \cdot \\ \sum_{S^{(2)}} P({S^{(2)} | S_{1}})P(\hat{O_2}\mid{S^{(2)}}) \cdot ... \cdot \\ \sum_{S^{(L)}}P({S^{(L)} | S_{L-1}})P(\hat{O_L}\mid{S^{(L)}}) ) \tag{2}$$

The equation above is written in the untypical form and introduces the following new variables:
1. $S^{(t)}$ - is a possible hidden state at time $t$.
2. $S_t$ - is a choosen state at time $t$.

The final result can be calculated as the product of sums and has lower complexity.

# Trellis represenation
Now we can represents the computations above as a trellis:
![full graph](https://simonrus.github.io/about/assets/img/2020-12_BCJR_Trellis.svg "Graph"){:height="80%" width="80%"}

Edges represent a state transitions probability   $P(S_{i} | S_{j})$ and nodes represent an observation probability $P(\hat{O_i}\mid{S_{i}})$.

The equation (1) computes the sum over all possible paths in the trellis.  

The equation (2) does calculations in a  sum-product manner, where we extend step by step the calculated result from the initial section with new trellis sections. 

# Forward-Backward algorithm 
## Forward step in a trellis
We evaluate the whole trellis by consequently calculating the product-sums that correspond in the begging to the left (initial) section and with next steps is extended to the more and more sections, until we reach the right (end) section. We store all intermidiate results in $\alpha_{t}(i)$ variables ($t$ - time, $i$ - current state),

![full graph with alphas](https://simonrus.github.io/about/assets/img/2020-12_BCJR_Trellis_Alphas.svg "Graph")

Our algorithm consists of the folowing steps:
1. Step 1: $\alpha_{1}(i)=P(\hat{O_1} \mid S^{(1)} = S_{i} ) \cdot P(S^{(1)} = S_{i})$
2. Step 2: 
$$\alpha_{2}(i)=\left[ \sum_{j =1} \alpha_{1}(j) \cdot P(S^{(2)} = S_{i} | S^{(1)} = S_{j}) \right] \cdot P(\hat{O_{2}} \mid S^{(2)} = S_{i})=\\=
\left[ \sum_{j =1} \alpha_{1}(j) \cdot P(S_{i} | S_{j}) \right] \cdot P(\hat{O_{2}} \mid S_{i}) 
$$
2. Step $t+1$:
$$\alpha_{t+1}(i)=\left[ \sum_{j =1} \alpha_{t}(j) \cdot P(S^{(t+1)} = S_{i} | S^{(t)} = S_{j}) \right] \cdot P(\hat{O_{t+1}} \mid S^{(t+1)} = S_{i})=\\=
\left[ \sum_{j =1} \alpha_{t}(j) \cdot P(S_{i} | S_{j}) \right] \cdot P(\hat{O_{t+1}} \mid S_{i}) 
$$

{:height="80%" width="80%"}

What does a variable $\alpha_{t}(i)$ mean? One can notice, that it is simply $\alpha_{t}(i) = P(\hat{O_1},\hat{O_2}...\hat{O_t}, S^{(t)} = S_{i})$. Or in other words: it is the probability of the joint event that sequence $\hat{O_1},\hat{O_2}...\hat{O_t}$ is observed and state $S_{i}$ is reached at time $t$.

## Convert trellis to a clique tree
The trellis can be viewed as a factor graph.


![full graph with alphas](https://simonrus.github.io/about/assets/img/2020-12_BCJR_Trellis_Alphas_as_CliqueTree.svg "Graph")

The nodes within one section form a singleton factor (denoted as $\Psi(i)$). 
The edges form a factor with 2 variables. 

![full graph with alphas](https://simonrus.github.io/about/assets/img/2020-12_BCJR_Trellis_Alphas_as_CliqueTree2.svg "Graph")

Factor $\Psi^{1}(S^{(1)})$ is:

| $S^{(1)}$ |value |
| ------ | --- |
| [$S_1$] | $\pi(S_1) \cdot P(S_1 \mid \hat{O_1})$ |
| [$S_2$] | $\pi(S_1) \cdot P(S_2 \mid \hat{O_1})$ |
| ... | ... |
| [$S_N$] | $\pi(S_1) \cdot P(S_N \mid \hat{O_1})$  |

Wait, please! How to find $P(S_i \mid \hat{O_1})$ if we know only $P(\hat{O_1} \mid S_i )$? Let's use Bayes Theorem for some time $t$ as follows:

$$P(S_i \mid \hat{O_t}) = \frac{P(\hat{O_t} \mid S_i ) \cdot P(S_i)} {P(\hat{O_t})} = P(\hat{O_t} \mid S_i ) \cdot y^{(t)}_{i}$$

So, our Factor $\Psi^{1}(S^{(1)})$ becomes:

| $S^{(1)}$ |value |
| ------ | --- |
| [$S_1$] | $\pi(S_1) \cdot P(S_1 \mid \hat{O_1})$ |
| [$S_2$] | $\pi(S_1) \cdot P(S_2 \mid \hat{O_1})$ |
| ... | ... |
| [$S_N$] | $\pi(S_1) \cdot P(S_N \mid \hat{O_1})$  |


Factor $\phi$ has the same values for all variables a, has values from $A$ and contains values:
|  |value |
| ------ | --- |
| [1, 1] | $P(S_{1} \mid S_{1})$ |
| [1, 2] | $P(S_{2} \mid S_{1})$ |
| ... | ... |
| [N, N] | $P(S_{N} \mid S_{N})$ |

Factor $\pi$ also corresponds 1-to-1 to $\pi$ from HMM model

## Forward step as BP in a clique tree with factors

## Backward step
Can we move in trellis from left to right? 
One can notice that we can rewrite equation (2) as follows:





# 
# Reference





