---
tags: [learning]
title: Active-2020-07-23-PGM-Tutorial-p3-w2_part2
created: '2020-07-05T10:43:41.740Z'
modified: '2020-07-27T09:35:58.196Z'
---

# Active-2020-07-23-PGM-Tutorial-p3-w2_part2
---
layout: post
title: "Tutorial: CRF Learning for OCR (PGM p3.week2) - part2"
author: "Sergei Semenov"
categories: learning
image: 2020-07-PGM_OCR_Learning.jpg
---

Previous part is [here](https://simonrus.github.io/about/learning/PGM-Tutorial-p3-w2.html)

# Assignment - what is under the hood?
The programming assignment is supplied with some already implemented functions and modules. As for 
any other assignment in this course, it is mandatory to understand how course creators see the 
path we shall pass (actually, it defines 80% of success).
 
## Selected algorithm
Here the stochastic gradient is in use. It means, that we run ascent gradient for every training 
sample independently. We wont see any batches in this assignments.

## How model looks exactly?

We have our initial 8 factors:
![8 factors](https://simonrus.github.io/about/assets/img/2020-07-23-PGM-Tutorial-p3-w2_part2_drawing1.jpg){:height="80%" width="80%"}

After connecting edges and calling *PruneTree()* (it combines factors with common parts to the one factor) we get something like:
![connected 8 factors](https://simonrus.github.io/about/assets/img/2020-07-23-PGM-Tutorial-p3-w2_part2_drawing2.jpg){:height="80%" width="80%"}

Now our model (painter with black) is relative simple. The BP for this tree requires only passing of two messages. The resulting beliefs can be used to extract marginals to compute conditional probabilities for every feature: $$P(Y_1 \mid X_1); P(Y_2 \mid X_2); P(Y_3 \mid X_3)$$

These computations are later used to calculate model expected feature count using following expression:
$$E_{\theta}\left[f_{i}\right]=\sum_{\mathbf{Y}^{\prime}} P\left(\mathbf{Y}^{\prime} \mid \mathbf{x}\right) f_{i}\left(\mathbf{Y}^{\prime}, \mathbf{x}\right)$$

## How features are stored in featureSet?
They are stored in the following order:
* Conditional $$F(Y \mid X)$$ - first half for black pixels, second half for whites.
* Unconditional stand-alone $$F(Y)$$ - actually letter frequencies.
* Unconditional pairwise $$F(Y_{i}, Y_{i+1})$$.

![full graph](https://simonrus.github.io/about/assets/img/2020-07-23-PGM-Tutorial-p3-w2_part2_drawing2.jpg){:height="80%" width="80%"}

# How to implement that?
I used the following code sequence
![code sequnce](https://simonrus.github.io/about/assets/img/2020-07-23-PGM-Tutorial-p3-w2_part2_drawing4.png){:height="80%" width="80%"}


















