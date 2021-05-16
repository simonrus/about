---
title: Draft-2021-03-01-BCJR-Algorithm_p1
created: '2021-03-01T19:27:35.496Z'
modified: '2021-05-16T16:03:03.502Z'
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

In the case of hard-decoding, emissions are discrete and the emission probability matrix has a finite number of elements (actually, the $O_t$ is a number of all possible received symbols). But in the case of soft-decoding, emissions and corresponding $B$ matrix are continuous variables. 


**Q:** If we have a continius distribution for emission probabilities, will it affect the computation model? 
**A:** No! The computation model will be still the same. We may write:
$P(O^t \mid S^t) = \prod\limits_{i} P(O^t(i) \mid S^t(i))$, where
$S^t(i)$ - i-th bit of codeword, produced by state $S^t$
$O^t(i)=r(i)$ - received value

$$P(O_t(i) \mid S_t(i)) = \begin{cases}
    {\displaystyle {\frac {1}{\sigma {\sqrt {2\pi }}}}e^{-{\frac {1}{2}}\left({\frac {r(i)-\mu }{\sigma }}\right)^{2}}}, & \text{if $S^t(i)=0$}.\\
    {\displaystyle {\frac {1}{\sigma {\sqrt {2\pi }}}}e^{-{\frac {1}{2}}\left({\frac {r(i)+\mu }{\sigma }}\right)^{2}}}, & \text{otherwise}.
  \end{cases}$$

# And few remarks...
We can raise the following questions:

**Q:** Emission matrix $B$ now depends on time. Will it affect the computations using Forward-Backward Algorithm?
**A:** No :-)



# References 
1. L. Bahl, J. Cocke, F. Jelinek, and J. Raviv, “Optimal decoding of linear codes for minimizing symbol error rate (Corresp.),” IEEE Trans. Inform. Theory, vol. 20, no. 2, pp. 284–287, Mar. 1974, doi: 10.1109/TIT.1974.1055186.





