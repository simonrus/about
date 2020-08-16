---
title: Active-2020-08-07-PGM-Structure-Learning-LikelihoodScores
created: '2020-08-05T09:50:39.530Z'
modified: '2020-08-16T19:42:21.860Z'
---

# Active-2020-08-07-PGM-Structure-Learning-LikelihoodScores

---
layout: post
title: "Structure Learning: Likelihood Scores"
author: "Sergei Semenov"
categories: learning
image: 2020-07-PGM_Logo.jpg
---
# Using Likelihood scores to find best structure
[Likelihood Structure Scores lecture](https://www.coursera.org/learn/probabilistic-graphical-models-3-learning/lecture/4hX6p/likelihood-scores) introduces the likelihood scores. The overall concept is quite clear: we can evaluate, how good is a random graph, if we use its structure to estimate some data (using MLE, of course).

What I find exciting here is the following: 
- one can see a certain strong connection between Machine Learning and Information Theory.
- if two graphs have a very similar score, can we run inference in a sparser graph instead of inference in other more complex graphs?
- inference optimization can be replaced by another type of optimization, e.g. with a focus to memory

# Decomposible score theorem
Theorem says, that:

$$\operatorname{score}_{L}(\mathcal{G}: \mathcal{D})=M \sum_{i=1}^{n} \mathbf{I}_{\hat{P}}\left(X_{i} ; \mathbf{P a}_{X_{i}}^{G}\right)-M \sum_{i=1}^{n} \boldsymbol{H}_{\hat{P}}\left(X_{i}\right)$$

## Property
Let's assume, that $G_0$ is a graph, where all variables are independent. The likelihood score can be written as:

$$\operatorname{score}_{L}(\mathcal{G_0}: \mathcal{D})= - M \sum_{i=1}^{n} \boldsymbol{H}_{\hat{P}}\left(X_{i}\right)$$

Let's connect a pair of nodes (e.g $X_i$ -> $X_j$). Denote new graph as $G_1$. The likelihood score will be:

$$\operatorname{score}_{L}(\mathcal{G_1}: \mathcal{D})=M \mathbf{I}_{\hat{P}}\left(X_{i};X_{j}\right)-M \sum_{i=1}^{n} \boldsymbol{H}_{\hat{P}}\left(X_{i}\right)$$

If can be seen, that one connection adds contribution that is equivalent to exactly $M\mathbf{I}_{\hat{P}}\left(X_{i};X_{j}\right)$.

If $X_i \perp\!\!\!\perp X_j$, then $\mathbf{I}_{\hat{P}}\left(X_{i};X_{j}\right) = 0$ and we get the same likelihood score as for graph $G_0$.

## Does direction plays role?
The direction doesn't play any role. But if the parents list was affected(!), the likelihood score changes

## Interesting facts
$\mathbf{I}_{\hat{P}}\left(X_{i}\right) = 0$ and $\mathbf{I}_{\hat{P}}\left(X_{i};\emptyset\right) = 0$






