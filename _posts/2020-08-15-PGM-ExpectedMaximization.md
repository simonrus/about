---
layout: post
title: "Expected Maximization by example"
author: "Sergei Semenov"
categories: learning
image: 2020-07-PGM_Logo.jpg
---
# The Simplest example of Expected Maximization Algorithm

What could be simpler then just a naive CPD bayesian network with 2 observed outputs ($$X_1$$ and $$X_2$$)?
Let's take it and see how EM works.

![Naive BN](https://simonrus.github.io/about/assets/img/2020-08-15-PGM-ExpectedMaximization_drawing1.inkscape.svg){:height="80%" width="80%"}

The $$X1$$ and $$X2$$ are observed and $$C$$ is not observed. Our data set consists of the following samples: $$D=\{x_1[m], x_2[m]  \}_{m=1}^M$$. For our test example we can assume, that $$X1$$ and $$X2$$ are binary values.

## Is it a Clustering?
Yes, we can state, that in this particular form we do clustering. Our task sounds: "Given a set of data points, we want to classify each data point into a specific group".

## How to select cardinality of C?
One option is to select it manually using some prior knowledge. I would prefer to have it binary for our example. Then our CPD tables would look like:

|   |    $$P(C)$$      |
|---|:--------------:|
| 0 | $$\theta_{C=0}$$ |
| 1 | $$\theta_{C=0}$$ | 

|   | $$P(X_1 \mid C = 0)$$  | $$P(X_1 \mid C = 1)$$  |
|---|:--------------:|:--------------:|
| 0 | $$\theta_{X_1=0, C=0}$$ | $$\theta_{X_1=0, C=1}$$ |
| 1 | $$\theta_{X_1=1, C=0}$$ | $$\theta_{X_1=1, C=1}$$ | 

|   | $$P(X_2 \mid C = 0)$$  | $$P(X_2 \mid C = 1)$$  |
|---|:--------------:|:--------------:|
| 0 | $$\theta_{X_2=0, C=0}$$ | $$\theta_{X_2=0, C=1}$$ |
| 1 | $$\theta_{X_2=1, C=0}$$ | $$\theta_{X_2=1, C=1}$$ | 


# EM intro: What we want to do?
We want to find all $$\theta$$s. If we had $$C$$ in our data set $$D$$, it would be an easy task. 

It would be cool, if we could somehow extend every sample $$d[m] = \{x_1[m], x_2[m] \}$$ of $$D$$ with some $$\hat{c}[m]$$ for  missing values. In this case, we would have a full observations $$\hat{d}[m] =\{x_1[m], x_2[m], \hat{c}[m]\}$$!

How we can do it? Let's use expected values.

But we need some already known $$\theta$$s! 

It is called "egg and chicken problem". So, we can start with some initial $$\theta^{(0)} = \{\theta^{(0)}_{C=0}, \theta^{(0)}_{C=1},\}$$ and try to build data samples $$\hat{D}^{(0)} = \{x_1[m], x_2[m], \hat{c}^{(0)}[m]\}_{m=1}^M$$, where missing(latent) variable $$c$$ is replaced with expected value $$\hat{c}^{(0)}[m]$$. This step is called *E-Step*. 

Then we can again evaluate new $$\theta^{(1)}$$ using MLE procedure. It would be *M-Step*.

Repeat *E-Step* and *M-Step* many times, until updates/corrections of $$\hat{D}^{(t)}$$ do not bring any improvements in likelihood for $$\theta^{(t+1)}$$. It will be our final estimation.

## E-Step: from $$\theta^{(t)}$$ to $$\hat{D}^{(t)}$$
As said before, we want to extend every sample $$\hat{d}[m]$$ of $$\hat{D}$$ with some $$\hat{c}[m]$$ to have a triplet $$\hat{d}[m] =\{x_1[m], x_2[m], \hat{c}[m]\}$$. Particularly, in our example at step $$t$$ we calculate:

$$\hat{c}_{c}^{(t)}[m] = P(C=c \mid x_1[m], x_2[m]) = \frac{P(C=c, x_1[m], x_2[m])}{\sum_{c}P(C=c, x_1[m], x_2[m])} =
 \frac{P(x_1[m], x_2[m] \mid C=c)P(C=c)}{\sum_{c}P(x_1[m], x_2[m] \mid C=c)P(C=c)}$$

where $$\hat{c}_{c}^{(t)}[m]$$ is expected value of variable $$C$$ (at step $$t$$ and sample $$m$$) taken in different clusters, Or just $$P(C=0 \mid x_1[m], x_2[m])$$ and $$P(C=1 \mid x_1[m], x_2[m])$$ in the empirical distribution.

## M-Step: from $$\hat{D}^{(t)}$$ to $$\theta^{(t+1)}$$
It is just a MLE solution for $$\hat{D}^{(t)}$$:

$$\theta^{(t+1)} = \argmax_\theta \hat{D}^{(t)}$$

# Cool links
1. [Probabilistic Graphical Models at Coursera (Daphna Koller, Stanford)](https://www.coursera.org/learn/probabilistic-graphical-models-3-learning/lecture/YVVxw/expectation-maximization-intro)
2. [Bayesian Methods In Machine Learning at Coursera (Novikov, HSE)](https://www.coursera.org/learn/bayesian-methods-in-machine-learning/home/week/2)
3. [cs228 notes: latent variables](https://ermongroup.github.io/cs228-notes/learning/latent/)
4. [cs228 notes: learning in directed models](https://ermongroup.github.io/cs228-notes/learning/directed/)



*Last update:15 August 2020*
