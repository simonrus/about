---
title: Active-2021-03-10-HMM_Applications
created: '2021-03-11T07:58:07.671Z'
modified: '2021-03-16T07:35:12.129Z'
---

# Active-2021-03-10-HMM_Applications

---
layout: post
title: "HMM - Applications"
author: "Sergei Semenov"
categories: learning fec
image: 2020-12_HMM_Trellis_Alphas.svg
---

# Applications 

[Previously](https://simonrus.github.io/about/learning/fec/ForwardBackward-Algorithm_p2.html) we found how to estimate a hidden transition probability between two neighbouring states in a HMM. 

Let's show quickly how HMM are used in practice. Our model may look like:
![full graph](https://simonrus.github.io/about/assets/img/2021-01-03-HMM_EmissionsModel.svg "Model"){:height="80%" width="80%"}

The states transitions, produced by Core Markov Chain, generate hidden patterns in an observed sequence. These patterns are extracted from the observed sequence and are utilized to estimate actual states, providing us insights into structures and properties of the Core Markov Chain.

The most important here is that the presence of noise has impacts only on emissions and doesn't affect Core Markov Chain. For this reason, an HMM is also called a doubly-embedded stochastic process.

Moreover, modeling observations in two layers, one visible (emission layer) and the other invisible (Core Markov Chain), is very useful, since many real world problems deal with classifying raw observations into a number of categories, or class labels, that are more meaningful to us.

The good examples are also:
1. Speech recognition tasks
2. Robot localisation
3. Computational Biology (sequency alignment problems, structure prediction)
4. Text annotation


# References 
1. L. R. Rabiner, “A tutorial on hidden Markov models and selected applications in speech recognition,” Proc. IEEE, vol. 77, no. 2, pp. 257–286, Feb. 1989, doi: 10.1109/5.18626.
2. B.-J. Yoon, “Hidden Markov Models and their Applications in Biological Sequence Analysis,” CG, vol. 10, no. 6, pp. 402–415, Sep. 2009, doi: 10.2174/138920209789177575.






