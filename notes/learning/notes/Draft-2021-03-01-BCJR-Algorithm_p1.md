---
title: Draft-2021-03-01-BCJR-Algorithm_p1
created: '2021-03-01T19:27:35.496Z'
modified: '2021-07-03T13:19:06.713Z'
---

# Draft-2021-03-01-BCJR-Algorithm_p1

---
layout: post
title: "BCJR Algorithm (Part 1)"
author: "Sergei Semenov"
categories: learning fec
image: 2021-03-05_TrellisConvCode.png
---

# Introduction

The [Forward-Backward algorithm](https://simonrus.github.io/about/learning/fec/ForwardBackward-Algorithm_p2.html) can be used for decoding on a trellis, if we apply some modifications. The new algorithm will be BCJR and was introduced in [1]

# Our Model
 Let's take a look again to a trellis ![full graph](https://simonrus.github.io/about/assets/img/2021-03-05_TrellisConvCode.png "Graph"){:height="80%" width="80%"}


An encoder uses an input symbol(green) to generate codeword symbol (red) based on own current state. Then the Encoder updates it's state and pushes the codeword symbol into a channel or, in terms of HMM world, **encoder emits**.


The channel corrupts the symbols during transmission. Receiver observes noisy codewords or, it terms of HMM worlds, **decoder  observes**. 


Now the decoding task can be expressed in terms of HMM as follows: **What is a codeword at sender, that could “most likely” produce the received sequence given known channel conditions?**

The main difference between BCJR and Fast-Forward algorithm is that emissions in HMMs appear only in states. But in a trellis, emissions appear during the transitions(!) between states.

![full graph](https://simonrus.github.io/about/assets/img/2021-03-05_Trellis_EmissionModel.png "Trellis Emission Model"){:height="80%" width="80%"}


# Emission probability matrix

In the case of hard-decoding, emissions are discrete and the emission probability matrix has a finite number of elements. And $O_t$ is a number of all possible received symbols. 

In the case of soft-decoding, emissions and corresponding $B$ matrix are continuous variables. We may still notice, that the computation model remains the same: taking into an account, that trellis produces only on possible emission during state transition,  we may write:
$P(O^t \mid S^t, S^{t+1}) = \sum_{E^{l}} P(O^t, E^l \mid S^t, S^{t+1}) = \sum_{E^{l}} (P(O^t \mid E^l, S^t, S^{t+1}) * P(E^l \mid S^t, S^{t+1})) = P(O^t \mid E^t) = \prod\limits_{i} P(O^t(i) \mid E^t(i)))$, where
$E^t(i)$ - i-th bit of codeword, produced by state transition from $S^t$ to $S^{t+1}$
$O^t(i)=r(i)$ - received value

$$P(O_t(i) \mid E_t(i)) = \begin{cases}
    {\displaystyle {\frac {1}{\sigma {\sqrt {2\pi }}}}e^{-{\frac {1}{2}}\left({\frac {r(i)-\mu }{\sigma }}\right)^{2}}}, & \text{if $S^t(i)=0$}.\\
    {\displaystyle {\frac {1}{\sigma {\sqrt {2\pi }}}}e^{-{\frac {1}{2}}\left({\frac {r(i)+\mu }{\sigma }}\right)^{2}}}, & \text{otherwise}.
  \end{cases}$$

# Algorithm description

![full graph with alphas](https://simonrus.github.io/about/assets/img/2021-06_BCJR_Trellis_Alphas.svg "Graph"){:height="80%" 
width="80%"}
asdas
Our algorithm consists of the folowing steps:
1. Step 1: $\alpha_{0}(i)= \pi(S_{i})$
2. Step 2: 
$$\alpha_{1}(i)=\alpha_{0}(j)  \sum\limits_{j =1} P(S^{2} = S_{i} \mid S^{1} = S_{j}) \cdot P(O^{1} \mid S^{1} = S_{j},S^{2} = S_{i})=\\=
\alpha_{0}(j)  \sum\limits_{j =1} P(S_{i} \mid S_{j}) \cdot P(O^{1} \mid S_{j},S_{i})
$$
2. Step $t+1$:
$$\alpha_{t+1}(i)=\alpha_{t}(j)  \sum\limits_{j =1} P(S_{i} \mid S_{j}) \cdot P(O^{t} \mid S_{j},S_{i})$$

# And few remarks...
We can raise the following questions:

**Q:** Emission matrix $B$ now depends on time. Will it affect the computations using Forward-Backward Algorithm?
**A:** No :-)



# References 
1. L. Bahl, J. Cocke, F. Jelinek, and J. Raviv, “Optimal decoding of linear codes for minimizing symbol error rate (Corresp.),” IEEE Trans. Inform. Theory, vol. 20, no. 2, pp. 284–287, Mar. 1974, doi: 10.1109/TIT.1974.1055186.





