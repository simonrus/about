---
title: Draft-2020-12-12-BCJR-Algorithms
created: '2020-11-30T08:19:27.713Z'
modified: '2020-12-23T12:24:10.681Z'
---

# Draft-2020-12-12-BCJR-Algorithms


---
layout: post
title: "BCJR Algorithm"
author: "Sergei Semenov"
categories: learning
image: 2020-07-PGM_Logo.jpg
---

# Sum-Product 
In the post ["Introduction to Hidden Markov Models"](https://simonrus.github.io/about/learning/Introduction-to-HMM.html), we have raised the first problem: "How do we compute the probability that the observed sequence was produced by a given HMM?". Or in the mathematical form, we need to find:
$$P(O_1,O_2...O_L \mid \lambda)$$

_"If you don't know what to do, start with joint distribution"_ (c) Mackey. But we don't know hidden states ($S_1, S_2 ... S_L$). Let's introduce them like as they are marginalized out:
$$P(O_1,O_2...O_L) = 
\sum_{{S^{(1)}},{S^{(2)}}...{S^{(L)}}}P({S^{(1)}},{S^{(2)}} ... {S^{(L)}}, O_1,O_2...O_L) \tag{1} $$

It can be easily seen, that above equation computes the sum over all possible states and has the complexity is $O(L \cdot N^{L})$. 

Now we can apply the distributive property and chain-rule as follows:
$$ \sum_{{S^{(1)}},{S^{(2)}}...{S^{(L)}}}P({S^{(1)}},{S^{(2)}} ... {S^{(L)}}, O_1,O_2...O_L) = \\
= \sum_{{S^{(1)}},{S^{(2)}}, ... {S^{(L)}}}P({S^{(1)}})P(O_1\mid{S^{(1)}}) P({S^{(2)} | S^{(1)}})P(O_2\mid{S^{(2)}})...P({S_L | S_{L-1}})P(O_L\mid{S^{(L)}}) ) = \\
= \sum_{S^{(1)}}\pi({S^{(1)}})P(O_1\mid{S^{(1)}}) \cdot \\ \sum_{S^{(2)}} P({S^{(2)} | S_{1}})P(O_2\mid{S^{(2)}}) \cdot ... \cdot \\ \sum_{S^{(L)}}P({S^{(L)} | S_{L-1}})P(O_L\mid{S^{(L)}}) ) \tag{2}$$

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
1. Step 1: $\alpha_{1}(i)=P(O^{1} \mid S^{(1)} = S_{i} ) \cdot P(S^{(1)} = S_{i})=\\=P(O^{1} \mid S_{i} ) \cdot \pi(S_{i})$
2. Step 2: 
$$\alpha_{2}(i)=\left[ \sum_{j =1} \alpha_{1}(j) \cdot P(S^{(2)} = S_{i} | S^{(1)} = S_{j}) \right] \cdot P(O^{2} \mid S^{(2)} = S_{i})=\\=
\left[ \sum_{j =1} \alpha_{1}(j) \cdot P(S_{i} | S_{j}) \right] \cdot P({O^{2}} \mid S_{i}) 
$$
2. Step $t+1$:
$$\alpha_{t+1}(i)=\left[ \sum_{j =1} \alpha_{t}(j) \cdot P(S^{(t+1)} = S_{i} | S^{(t)} = S_{j}) \right] \cdot P({O^{t+1}} \mid S^{(t+1)} = S_{i})=\\=
\left[ \sum_{j =1} \alpha_{t}(j) \cdot P(S_{i} | S_{j}) \right] \cdot P({O^{t+1}} \mid S_{i}) 
$$

{:height="80%" width="80%"}

What does a variable $\alpha_{t}(i)$ mean? One can notice, that it is simply $\alpha_{t}(i) = P(O_1,O_2...\hat{O_t}, S^{(t)} = S_{i})$. Or in other words: it is the probability of the joint event that sequence $O_1,O_2...\hat{O_t}$ is observed and state $S_{i}$ is reached at time $t$.

## Backward step
Can we move in trellis from left to right? No problem:

1. Step 1: $\beta_{L}(i)=1$
2. Step 2: 
$$\beta_{L-1}(i) =
\sum_{j =1} \beta_{L}(j) \cdot P(S_{j} | S_{i}) \cdot P({O_{L}} \mid S_{j}) =\\=
\sum_{j =1} P(S_{j} | S_{i}) \cdot P({O_{L}} \mid S_{j})
$$
3. Step 3: 
$$\beta_{L-2}(i) = \sum_{j =1} \beta_{L-1}(j) \cdot P(S_{j} | S_{i}) \cdot P(O^{L-1} \mid S_{i}) 
$$
3. Step $t$:
$$\beta_{t}(i) =
\sum_{j =1} \beta_{t+1}(j) \cdot P(S_{j} | S_{i}) \cdot P(O^{t+1} \mid S_{i}) 
$$
4. Last step:
$$\beta_{0}(i) = 
\sum_{j =1} \beta_{1}(j) \cdot P(S_{j} | S_{i}) \cdot P(O^{1} \mid S_{j}) 
$$

It can be seen, that $$\beta_{1}(i) \cdot \pi(S_i) = \alpha_{L} (i)$$







# 
# Reference





