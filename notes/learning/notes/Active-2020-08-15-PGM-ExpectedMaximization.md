---
title: Active-2020-08-15-PGM-ExpectedMaximization
created: '2020-08-15T05:04:17.063Z'
modified: '2020-08-15T06:59:30.554Z'
---

# Active-2020-08-15-PGM-ExpectedMaximization

---
layout: post
title: "Expected Maximization by example"
author: "Sergei Semenov"
categories: learning
image: 2020-07-PGM_Logo.jpg
---
# The Simplest example of Expected Maximization Algorithm

What could be simpler then just a naive CPD bayesian network with 2 observed outputs ($X_1$ and $X_2$)?
Let's take it and see how EM works.

![Naive BN](https://simonrus.github.io/about/assets/img/2020-08-15-PGM-ExpectedMaximization_drawing1.inkscape.svg){:height="80%" width="80%"}

The $X1$ and $X2$ are observed and $C$ is not observed. Our data set is $D=\{x_1[m], x_2[m]  \}_{m=1}^M$. We can also assume for our test case, that $X1$ and $X2$ are binary values.

## Is it a Clustering?
Yes, we can state, that in this particular form we do simple clustering. Our task sounds: "Given a set of data points, we want to classify each data point into a specific group".

If we take another graph or network structure, it will be a graph with latent (hidden variables)

## How to select cardinality of C?
One option is to select it manually using some prior knowledge. I would prefer to have it binary for a given example. Our CPD tables would be:

|   |    $P(C)$      |
|---|:--------------:|
| 0 | $\theta_{C=0}$ |
| 1 | $\theta_{C=0}$ | 

|   | $P(X_1 \mid C = 0)$  | $P(X_1 \mid C = 1)$  |
|---|:--------------:|:--------------:|
| 0 | $\theta_{X_1=0, C=0}$ | $\theta_{X_1=0, C=1}$ |
| 1 | $\theta_{X_1=1, C=0}$ | $\theta_{X_1=1, C=1}$ | 

|   | $P(X_2 \mid C = 0)$  | $P(X_2 \mid C = 1)$  |
|---|:--------------:|:--------------:|
| 0 | $\theta_{X_2=0, C=0}$ | $\theta_{X_2=0, C=1}$ |
| 1 | $\theta_{X_2=1, C=0}$ | $\theta_{X_2=1, C=1}$ | 


## What we want to do?
We want to find all $\theta$\s 

TBD
#
https://www.coursera.org/learn/bayesian-methods-in-machine-learning/home/week/2
https://ermongroup.github.io/cs228-notes/learning/latent/
https://ermongroup.github.io/cs228-notes/learning/directed/


