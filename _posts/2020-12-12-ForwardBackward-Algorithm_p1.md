---
layout: post
title: "ForwardBackward Algorithm (Part 1)"
author: "Sergei Semenov"
categories: learning fec
image: 2020-12_HMM_Trellis_Alphas.svg
---

# Sum-Product 
In the post ["Introduction to Hidden Markov Models"](https://simonrus.github.io/about/learning/fec/Introduction-to-HMM.html), we have raised the first problem: "How do we compute the probability that the observed sequence $$O^1,O^2...O^L$$ was produced by a given HMM?". Or in the mathematical form, we need to find:
$$P(O^1,O^2...O^L \mid \lambda)$$

_"If you don't know what to do, start with joint distribution"_ (c) Mackey. But we don't know hidden state values $$S^{1}, S^{2} ... S^{L}$$ at time moments t=$$1,2 ... L$$. Let's introduce them like as they are marginalized out:
$$P(O^1,O^2...O^L) = \sum\limits_{S^1,S^2,...,S^L} P(S^1,S^2,...,S^L, O^1,O^2,...,O^L)$$

It can be easily seen, that above equation computes the sum over all possible states and has the complexity is $$O(L \cdot N^{L})$$. 

Now we can apply the distributive property and chain-rule as follows:
$$\sum\limits_{S^1,S^2,...,S^L}P(S^1,S^2,...,S^L, O^1,O^2,...,O^L) = \\
= \sum\limits_{S^1,S^2, ..., S^L}P(S^1)P(O^1 \mid S^1 ) P(S^2 \mid S^1) P(O^2 \mid S^2)...P(S^L \mid S^{L-1})P(O^L \mid S^L) ) = \\
= \sum\limits_{S^1}\pi(S^1)P(O^1 \mid S^1) \cdot \sum\limits_S^2 P(S^2 \mid S^1)P(O^2 \mid S^2) \cdot ... \cdot \\ \sum\limits_{S^{L-1}}P(S^{L-1} \mid S^{L-2})P(O^{L-1} \mid S^{L-1}) \cdot  \sum\limits_{S^L}P(S^{L} \mid S^{L-1})P(O^L \mid S^{L})$$

The equation above is written in an untypical form and introduces the following new variables:
1. $$S^{t}$$ - is a possible hidden state at time $$t$$.
2. $$S_t$$ - is a choosen state at time $$t$$ (will be used later). 

The final result can be calculated as the product of sums and has lower complexity.

# Trellis represenation
Now we can represents the computations above as a trellis:
![full graph](https://simonrus.github.io/about/assets/img/2020-12_HMM_Trellis.svg "Graph"){:height="80%" width="80%"}

Edges represent a state transitions probability  $$P(S^{t+1} = i \mid S^{t} = j) = P(S_{i} \mid S_{j}) = A_{ji}$$ and nodes represent an observation probability $$P(O^t=i\mid{S^{t}=j}) = P(O_i \mid {S_{j}}) = B_{ji}$$.

The equation (1) computes the sum over **all possible paths** in the trellis.  

The equation (2) does calculations in a  sum-product manner, where we extend step by step the calculated result from the initial section with new trellis sections. 

# Forward-Backward algorithm 
## Forward step in a trellis
We evaluate the whole trellis by consequently calculating the product-sums that correspond in the begging to the left (initial) section and with next steps is extended to the more and more sections, until we reach the right (end) section. We store all intermidiate results in $$\alpha_{t}(i)$$ variables ($$t$$ - time, $$i$$ - current state),

![full graph with alphas](https://simonrus.github.io/about/assets/img/2020-12_HMM_Trellis_Alphas.svg "Graph")

Our algorithm consists of the folowing steps:
1. Step 1: $$\alpha_{1}(i)= P(S^{1} = S_{i}) \cdot P(O^{1} \mid S^{1} = S_{i} ) =\\= \pi(S_{i}) \cdot P(O^{1} \mid S_{i} )$$
2. Step 2: 
$$\alpha_{2}(i)=\left[ \sum\limits_{j =1} \alpha_{1}(j) \cdot P(S^{2} = S_{i} \mid S^{1} = S_{j}) \right] \cdot P(O^{2} \mid S^{2} = S_{i})=\\=
\left[ \sum\limits_{j =1} \alpha_{1}(j) \cdot P(S_{i} \mid S_{j}) \right] \cdot P({O^{2}} \mid S_{i}) 
$$
2. Step $$t+1$$:
$$\alpha_{t+1}(i)=\left[ \sum\limits_{j =1} \alpha_{t}(j) \cdot P(S^{t+1} = S_{i} \mid S^{t} = S_{j}) \right] \cdot P({O^{t+1}} \mid S^{t+1} = S_{i})=\\=
\left[ \sum\limits_{j =1} \alpha_{t}(j) \cdot P(S_{i} \mid S_{j}) \right] \cdot P({O^{t+1}} \mid S_{i}) 
$$

{:height="80%" width="80%"}

What does a variable $$\alpha_{t}(i)$$ mean? One can take a look at equation (2) and notice, that it $$\alpha_{t}(i) = P(O^1,O^2,...,{O^t}, S^{t} = S_{i})$$. Or in other words: it is the probability of the joint event that sequence $$O^1,O^2,...,{O^t}$$ is observed and state $$S_{i}$$ is reached at time $$t$$.

## Backward step
Can we do calculations in the trellis from left to right? No problem! Let's refer to equation (2) again and do the following:

1. Step 1: $$\beta_{L}(i)=1$$
2. Step 2: 
$$\beta_{L-1} = \sum\limits_{S^{L}}P(S^{L} \mid S^{L-1})\cdot P(O^L\mid S^{L})$$
$$\beta_{L-1}(i) = \sum\limits_{S^{L}}P(S^{L} \mid S^{L-1} = S_{i}) \cdot P(O^L\mid S^{L}) = \\
= \sum\limits_{j=1}^{N} \beta_{L}(j) \cdot P(S^{L} = S_{j} \mid S^{L-1} = S_{i}) \cdot P(O^L\mid S^{L} = S_{j})\\
= \sum\limits_{j =1}^{N} \beta_{L}(j) \cdot P(S_{j} \mid S_{i}) \cdot P({O_{L}} \mid S_{j})
$$
3. Step 3: 
$$\beta_{L-2}(i) = \sum\limits_{j =1} \beta_{L-1}(j) \cdot P(S^{L-1} = S_{j} \mid S^{L-2} = S_{i})\cdot P(O^{L-1}\mid S^{L-1} = S_{j} ) = \\
= \sum\limits_{j =1} \beta_{L-1}(j) \cdot P(S_{j} \mid S_{i}) \cdot P(O^{L-1} \mid S_{j}) 
$$
3. Step $$t$$:
$$\beta_{t}(i) =
\sum\limits_{j =1} \beta_{t+1}(j) \cdot P(S_{j} \mid S_{i}) \cdot P(O^{t+1} \mid S_{j}) 
$$
4. Last step (the represenation is different, because all paths start in the same point):
$$\beta_{0} = 
\sum\limits_{j =1} \beta_{1}(j) \cdot \pi(S_{j}) \cdot P(O^{1} \mid S_{j}) 
$$

What does a variable $$\beta_{t}(i)$$ mean? Let's take a look at $$\beta_{L-1}(i)$$:
$$\beta_{L-1}(i) = \sum\limits_{S^{L}}P(S^{L} \mid S^{L-1} = S_{i}) \cdot P(O^L\mid S^{L}) = \\
= \sum\limits_{S^{L}}P(S^{L}, O^L \mid S^{L-1} = S_{i}) = P(O^L \mid S^{L-1} = S_{i})$$
Taken into accound that $$P(O^L \perp \!\!\! \perp O^{L-1} \mid S^{L-1})$$, we can write:
$$
\beta_{L-2}(i) = \sum\limits_{j =1} \beta_{L-1}(j) \cdot P(S^{L-1} = S_{j} \mid S^{L-2} = S_{i})\cdot P(O^{L-1}\mid S^{L-1} = S_{j} )=\\
=\sum\limits_{j =1} P(O^L \mid S^{L-1} = S_{j}) \cdot P(S^{L-1} = S_{j} \mid S^{L-2} = S_{i})\cdot P(O^{L-1}\mid S^{L-1} = S_{j} )=\\
= \sum\limits_{j =1} P(O^{L-1}, O^L \mid S^{L-1} = S_{j}) \cdot P(S^{L-1} = S_{j} \mid S^ {L-2} = S_{i})=\\
=P(O^{L-1}, O^L \mid S^{L-2} = S_{i})$$

In a general case we have :
$$\beta_{t}(i) = P(O^{t+1}, O^{t+2}...O^{L} \mid S^{t} = S_{i})$$
or using conditional probability definition:
$$\beta_{t}(i) = \frac{P(O^{t+1}, O^{t+2}...O^{L}, S^{t} = S_{i})}{P(S^{t} = S_{i})}$$
or in a form, where hidden states starting from timepoint $$t+1$$ are marginalized out:
$$\beta_{t}(i) = \frac{\sum\limits_{S^{t+1}, S^{t+2}...S^{L}}P(O^{t+1}, O^{t+2}...O^{L}, S^{t} = S_{i})}{ P(S^{t} = S_{i})}$$


# Solution for the  first problem
Now we have two options to solve first problem with complexity $$O(L \cdot N^2)$$:
1. Using Forward steps: $$P(O^1,O^2...O^L \mid \lambda) = \sum\limits_{i}\alpha_{L}(i)$$ 
2. Using Backward steps: $$P(O^1,O^2...O^L \mid \lambda) = \beta_{0} = \sum\limits_{j=1} \beta_{1}(j) \cdot \pi(S_{j}) \cdot P(O^{1} \mid S_{j})$$
3. Using Forward and backward steps together: $$P(O^1, O^2 .. O^L\mid \lambda) =   \sum\limits_{i} P(O^1, O^2 .. O^L, S_t = i) = \sum\limits_{i} \frac{P( S_t = i\mid O^1, O^2 .. O^L)}{P(O^1, O^2 .. O^L)} = \sum\limits_{i} \alpha_{t}(i) \beta_{t}(i)$$

# Why Forward and Backward?
Answer: Forward and Backward steps can help us to answer more complicated queries. Stay tuned!

# References 
1. L. R. Rabiner, “A tutorial on hidden Markov models and selected applications in speech recognition,” Proc. IEEE, vol. 77, no. 2, pp. 257–286, Feb. 1989, doi: 10.1109/5.18626.





*Last update:10 March 2021*
