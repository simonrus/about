---
title: Draft-2021-03-01-BCJR-Algorithm_p1
created: '2021-03-01T19:27:35.496Z'
modified: '2021-03-16T08:14:00.446Z'
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

The [Forward-Backward algorithm](https://simonrus.github.io/about/learning/fec/ForwardBackward-Algorithm_p2.html) with small modifications can be used for decoding on a trellis. This algorithm is called BCJR and was intoruduced in [1]

# System model
 Let's take a look again to a trellis ![full graph](https://simonrus.github.io/about/assets/img/2021-03-05_TrellisConvCode.png "Graph"){:height="80%" width="80%"}

The main difference between trellis and HMM is that in HMM the emissions appear only in states.
But in a trellis, emissions appear during the transitions between states.

![full graph](https://simonrus.github.io/about/assets/img/2021-03-05_Trellis_EmissionModel.png "Trellis Emission Model"){:height="80%" width="80%"}

The transition between states represents codeword symbol(what we transmit) and emissions represent received symbols. 

Now the task of decoding in the following: we need to estimate transmitted symbols (hidden state transitions) using our observations - a received sequence. 




# Decoding on trellis

In the case of hard-decoding, emissions are discrete and the emission probability matrix has a finite number of elements (actually, the $O_t$ is a number of all possible received symbols). But in the case of soft-decoding, emissions and corresponding $B$ matrice are continuous variables. 

Let us focus only on soft-decoding for now. We may write:
$P(O_t \mid S_t) = \prod\limits_{i} P(O_t(i) \mid S_t(i))$, where
$S_t(i)$ - i-th bit of codeword, produced by state S_t
$O_t(i)=r_t(i)$ - received value

$$P(O_t(i) \mid S_t(i)) = \begin{cases}
    {\displaystyle {\frac {1}{\sigma {\sqrt {2\pi }}}}e^{-{\frac {1}{2}}\left({\frac {r(i)-\mu }{\sigma }}\right)^{2}}}, & \text{if $S_t(i)=0$}.\\
    {\displaystyle {\frac {1}{\sigma {\sqrt {2\pi }}}}e^{-{\frac {1}{2}}\left({\frac {r(i)+\mu }{\sigma }}\right)^{2}}}, & \text{otherwise}.
  \end{cases}$$

We can extend the original HMM assumption with following points:
1. we have a continius distribution for emission probabilities. Will it affect the computation model? Answer is: No! 
2. the emission matrix $B$ now depends on state. But it doesn't affect the computation model as well!



# References 
1. L. Bahl, J. Cocke, F. Jelinek, and J. Raviv, “Optimal decoding of linear codes for minimizing symbol error rate (Corresp.),” IEEE Trans. Inform. Theory, vol. 20, no. 2, pp. 284–287, Mar. 1974, doi: 10.1109/TIT.1974.1055186.





