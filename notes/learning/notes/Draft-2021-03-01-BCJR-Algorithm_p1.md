---
title: Draft-2021-03-01-BCJR-Algorithm_p1
created: '2021-03-01T19:27:35.496Z'
modified: '2021-03-11T07:25:06.516Z'
---

# Draft-2021-03-01-BCJR-Algorithm_p1

---
layout: post
title: "BCJR Algorithm (Part 1)"
author: "Sergei Semenov"
categories: learning fec
image: 2021-03-03-BCJR_EmissionsCausedByChannel.svg
---

# Introduction




# Decoding on trellis

But how this technique could be applied to turbo codes or, generally speaking, can be used for decoding on a trellis?

# Decoding 
The transition between states can represent a transmitted symbol (codeword symbol) and emissions can represent received symbols. Now the task of decoding in the following: we need to estimate transmitted symbols (hidden states/state transitions) using our observations - a received sequence. 


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
1. L. R. Rabiner, “A tutorial on hidden Markov models and selected applications in speech recognition,” Proc. IEEE, vol. 77, no. 2, pp. 257–286, Feb. 1989, doi: 10.1109/5.18626.
2. L. Bahl, J. Cocke, F. Jelinek, and J. Raviv, “Optimal decoding of linear codes for minimizing symbol error rate (Corresp.),” IEEE Trans. Inform. Theory, vol. 20, no. 2, pp. 284–287, Mar. 1974, doi: 10.1109/TIT.1974.1055186.





