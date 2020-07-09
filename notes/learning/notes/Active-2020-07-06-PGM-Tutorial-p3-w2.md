---
tags: [learning]
title: Active-2020-07-06-PGM-Tutorial-p3-w2
created: '2020-07-05T10:43:41.740Z'
modified: '2020-07-09T20:02:44.942Z'
---

# Active-2020-07-06-PGM-Tutorial-p3-w2
---
layout: post
title: "Tutorial: CRF Learning for OCR (PGM p3.week2)"
author: "Sergei Semenov"
categories: learning
image: 2020-07-PGM_Logo.jpg
---
# Assignment: CRF Learning for OCR
Here I would like to write some useful tips, that helped me to deeply understand and complete "CRF Learning for OCR" home assignment from Probabilistic Graphical Models course on Coursera (it's part3, week 2)

The goal of task is to train the model for Optical character recognition for 3 letter words

# Model descripion

We have input (observed variable) images $$I$$ or $$X$$ which consists of 32 white/black pixels (denoted as $$x_{i,j}$$)
We have output (single characters / hidden states) chars $$C$$ or $$Y$$ (26 letters)

We will train a OCR model that have
* singleton factors for observed images $$\widetilde{P}(C_{i} \mid I)$$ that defines OCR model for single character $$i$$
* singleton factors for characters $$P(C)$$ describes letter probability in the English language
* pairwise factors $$P(C_{i}, C_{i+1})$$ describes pairwise letters probability 

Lets try to build using CPD model
##  CPD Model
Let's try to represent our model as the MN with the following structure
$$
F(Y_1, Y_2, Y_3 | X_1, X_2, X_3) = F1(Y_1) * F2(Y_2) * F3(Y_3) * F4(Y_1 \mid X_1) * F5(Y_2 \mid X_2) * F6(Y_3 \mid X_3) * F7 (Y_1, Y_2)* F8 (Y_2, Y_3)
$$

![full graph](https://simonrus.github.io/about/assets/img/2020-07_PGM_p2_week2_drawing1.inkscape.svg "Graph")

### CPD Model: Number of parameters 
Let cound number of parameters when we use CPD model

What is the total number of parameters in our model?

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

Oops, that's too much. Lets try to reduce total amount of parameters by using shared parameters

But first of all, lets move to the model with log-linear features

## Log-linear model: from factors to features
Given the features $$f_{i}$$ and the weight $$\theta_{i}$$
$$P(\mathbf{Y} \mid \mathbf{x}: \theta)=\frac{1}{Z_{\mathbf{x}}(\theta)} \exp \left\{\sum_{i=1}^{k} \theta_{i} f_{i}\left(\mathbf{D}_{i}\right)\right\}$$
where the partition function is 

$$Z_{\mathbf{x}}(\theta) \equiv \sum_{\mathbf{Y}} \exp \left\{\sum_{i=1}^{k} \theta_{i} f_{i}\left(\mathbf{D}_{i}\right)\right\}$$

Every feature is binary and takes 0 or 1 value (presented or not).

The number of required features is also 3926

### Log-linear model: adding shared parameters

What we can simplify? 
* let's assume that letter probability doesn't depend on position. In this case factors $$F1,F2,F3$$ will have the same parameters and we can estimate them together $$F_{123}$$
* let's assume that pairwise letter probability doesn't depend on position. In this case, $$F7 = F8$$ and use $$F_{78}$$ instead
* We would use the same OCR model for single character $$F4 = F5 = F6$$. We will declare it as $$F_{456}$$ 

*To think later*: Can we evaluate parameters using the following model 
![full graph](https://simonrus.github.io/about/assets/img/2020-07_PGM_p2_week2_drawing2.inkscape.svg "Graph")

### Log-linear model: How many shared parameters?
For $$F_{456}$$ factor we count number of features and shared parameters using function *ComputeConditionedSingletonFeatures()*. 
It return __3\*26\*32=2496 features and 2\*26\*32=1664 shared parameters__ (We have 2 features per pixel - for white and black pixel)

For $$F_{123}$$ factor we use function *ComputeUnconditionedSingletonFeatures()*. It returns __3\*26=78 features and 26 shared parameters__

For $$F_{78}$$ factor the function *ComputeUnconditionedPairFeatures()* is used. It returns __2\*26\*26=1352 features and 26\*26 = 676 shared parameters__

The total number of shared parameters is $$card(F_{train}) = 26 + 2 * 26 * 32 + 26 * 26 = 2366$$

# Calculating log partition function

The log partition function is represented as the following marginal

$$Z_{\mathbf{x}}(\theta) \equiv \sum_{\mathbf{Y}} \exp \left\{\sum_{i=1}^{k} \theta_{i} f_{i}\left(\mathbf{D}_{i}\right)\right\}$$

As previously discussed in [Belief Propagation in Clique Trees](https://simonrus.github.io/about/learning/PGM-p2-w2-BP-In-CliqueTrees.html), BP calculates unnormalized marginals for all cliques

If we were using joint distributions, our model could look like

![full graph](https://simonrus.github.io/about/assets/img/2020-07_PGM_p2_week2_drawing3.inkscape.svg "Graph")

The complexity of BP would be extremely huge since we were needed to calculate $$P(Y_n, X_n)$$. It would require knowledge over
all possible $$X_n$$ or some prior distribution


So, the trick here is to use conditional distrubution
![full graph](https://simonrus.github.io/about/assets/img/2020-07_PGM_p2_week2_drawing4.inkscape.svg "Graph")

In this case, Clique tree would contain only 2 cliques

[TBD]









