---
tags: [learning]
title: Active-2020-07-06-PGM-Tutorial-p3-w2
created: '2020-07-05T10:43:41.740Z'
modified: '2020-07-24T08:38:05.153Z'
---

# Active-2020-07-06-PGM-Tutorial-p3-w2
---
layout: post
title: "Tutorial: CRF Learning for OCR (PGM p3.week2)"
author: "Sergei Semenov"
categories: learning
image: 2020-07-PGM_OCR_Learning.jpg
---
# Assignment: CRF Learning for OCR
Here I would like to write some useful tips, that helped me to deeply understand and complete "CRF Learning for OCR" home assignment from Probabilistic Graphical Models course on Coursera (it's part3, week 2).

The goal of task is to train the model for Optical character recognition for 3 letter words.

# Model description

We have input (observed variable) images $$I$$ or $$X$$ which consists of 32 white/black pixels (denoted as $$x_{i,j}$$)
We have output (single characters / hidden states) chars $$C$$ or $$Y$$ (26 letters).

We will train an OCR model that have:
* Singleton conditioned factors for observed images $$\widetilde{P}(C_{i} \mid I)$$. These factors defines a simplest
 per-symbol OCR model.
* Singleton factors for characters $$P(C)$$ (actually, letter probability in the English language).
* Pairwise factors $$P(C_{i}, C_{i+1})$$ are used tp describe pairwise letters probability.

Lets try to build using CPD model
##  CPD Model
Let's try to represent our model as the MN with the following structure:
$$
F(Y_1, Y_2, Y_3 | X_1, X_2, X_3) = F1(Y_1) * F2(Y_2) * F3(Y_3) * F4(Y_1 \mid X_1) * F5(Y_2 \mid X_2) * F6(Y_3 \mid X_3) * F7 (Y_1, Y_2)* F8 (Y_2, Y_3)
$$

![full graph](https://simonrus.github.io/about/assets/img/2020-07_PGM_p2_week2_drawing1.inkscape.svg "Graph"){:height="50%" width="50%"}

### CPD Model: Number of parameters 
Lets count number of parameters for CPD model. What would be a total number of parameters?

$$
card(F1) = 26 \\
card(F2) = 26 \\
card(F3) = 26 \\
card(F4) = 26 * 32 \\
card(F5) = 26 * 32 \\
card(F6) = 26 * 32 \\
card(F7) = 26 * 26 \\
card(F8) = 26 * 26 \\
$$

$$card(F) = 3 * 26 + 3 * 26 * 32 + 2 * 26 * 26 = 3926$$

Oops, that's definitily too much. Lets try to reduce total amount of parameters by using shared parameters.

But first of all, let's move to the model with log-linear features.

## Log-linear model: from factors to features
Given the features $$f_{i}$$ and the weight $$\theta_{i}$$ we may write:

$$P(\mathbf{Y} \mid \mathbf{x}: \theta)=\frac{1}{Z_{\mathbf{x}}(\theta)} \exp \left\{\sum_{i=1}^{k} \theta_{i} f_{i}\left(\mathbf{D}_{i}\right)\right\}$$

with the following partition function:

$$Z_{\mathbf{x}}(\theta) \equiv \sum_{\mathbf{Y}} \exp \left\{\sum_{i=1}^{k} \theta_{i} f_{i}\left(\mathbf{D}_{i}\right)\right\}$$

Every feature is binary and takes 0 or 1 value (presented or not). In this case, the number of required features is also 3926

### Log-linear model: adding shared parameters

How can we simplify our model? Take the next recipes:
* Assuming that letter probability doesn't depend on position, we can let factors $$F1,F2,F3$$ to have same parameters and  we can estimate them together in $$F_{123}$$.
* As next step, we can assume that pairwise letter probabilities don't depend on position. We can assume that $$F7 = F8$$ and use $$F_{78}$$ instead.
* And one extra step: We would use the same OCR model for single character $$F4 = F5 = F6$$ and declare it as $$F_{456}$$.

*To think later*: Can we evaluate parameters using the following model?
![full graph](https://simonrus.github.io/about/assets/img/2020-07_PGM_p2_week2_drawing2.inkscape.svg "Graph"){:height="50%" width="50%"}

### Log-linear model: How many shared parameters?
The programming assignments provide the following functions to evaluate the number of shared parameters:
* *ComputeConditionedSingletonFeatures()* - counts the number of features and shared parameters from singleton conditioned factors (yes, __conditioned__!). For factor $$F_{456}$$, the function returns __3\*26\*32=2496 features and 2\*26\*32=1664 shared parameters__. That makes sense, since we have 2 feature per pixel - (1 for a white, 1 for a black).
* *ComputeUnconditionedSingletonFeatures()* - counts for singleton and unconditioned factors. For $$F_{123}$$ we get __3\*26=78 features and 26 shared parameters__.
* *ComputeUnconditionedPairFeatures()* - counts parameters for pairwise factors. E.g. for factor $$F_{78}$$ it returns __2\*26\*26=1352 features and 26\*26 = 676 shared parameters__.

The total number of shared parameters is:
$$card(F_{train}) = 26 + 2 * 26 * 32 + 26 * 26 = 2366$$

# Calculating log partition function
The log partition function is represented as the following marginal:

$$Z_{\mathbf{x}}(\theta) \equiv \sum_{\mathbf{Y}} \exp \left\{\sum_{i=1}^{k} \theta_{i} f_{i}\left(\mathbf{D}_{i}\right)\right\}$$

As previously discussed in [Belief Propagation in Clique Trees](https://simonrus.github.io/about/learning/PGM-p2-w2-BP-In-CliqueTrees.html), BP calculates unnormalized marginals for all cliques. If we were using joint distributions, our model could look like:

![full graph](https://simonrus.github.io/about/assets/img/2020-07_PGM_p2_week2_drawing3.inkscape.svg "Graph"){:height="50%" width="50%"}

The complexity of BP would be extremely huge since it is needed to calculate $$P(Y_n, X_n)$$. It would require knowledge over
all possible $$X_n$$ or some prior distribution.

So, the trick here is to use conditional distribution. The model may look like:
![full graph](https://simonrus.github.io/about/assets/img/2020-07_PGM_p2_week2_drawing4.inkscape.svg "Graph"){:height="50%" width="50%"}

Now, our Clique tree contains only 2 cliques.

Now let's go to [part 2](https://simonrus.github.io/about/learning/PGM-Tutorial-p3-w2_part2.html)









