---
tags: [learning]
title: Active2020-07-06-PGMTutorialp3w2
created: '2020-07-05T10:43:41.740Z'
modified: '2020-07-06T10:11:16.680Z'
---

# Active_2020-07-06-PGM_Tutorial_p3_w2
---
layout: post
title: "PGM (p3.week2)"
author: "Sergei Semenov"
categories: learing
image: 2020-07-PGM_Logo.jpg
---
# Tutorial: CRF Learning for OCR
Here I would like to write some useful tips, that helped me to deeply understand and complete "CRF Learning for OCR" home assignment from Probabilistic Graphical Models course on Coursera (it's part3, week 2)

The goal of task is to train the model for Optical character recognition for 3 letter words

# Basic CRF Model

We have input (observed variable) images $$I$$ or $$X$$ which consists of 32 white/black pixels (denoted as $$x_{i,j}$$)
We have output (single charachters / hidden states) chars $$C$$ or $$Y$$ (26 letters)

We will train a OCR model that have
* singleton factors for observed images $$\widetilde{P}(C_{i} \mid I)$$ that defines OCR model for single character $$i$$
* singleton factors for charachers $$P(C)$$ describes letter probability in the English language
* pairwise factors $$P(C_{i}, C_{i+1})$$ describes pairwise letters probability 


# Number of parameters as CPD model

## Direct counting using factor graph
Let's try to represent our model as the MN with the following structure
$$
F(Y_1, Y_2, Y_3 | X_1, X_2, X_3) = F1(Y_1) * F2(Y_2) * F3(Y_3) * F4(Y_1 \mid X_1) * F5(Y_2 \mid X_2) * F6(Y_3 \mid X_3) * F7 (Y_1, Y_2)* F8 (Y_2, Y_3)
$$

![full graph](https://simonrus.github.io/about/assets/img/2020-07_PGM_p2_week2_drawing1.inkspace.svg "Graph")

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

Oops, that's too much. Lets try to reduce total ammount of parameters by using shared params

## Declare shared params

What we can simplify? 
* let's assume that letter probability doesn't depend on position. In this case factors $$F1,F2,F3$$ will have the same parameters
* let's assume that pairwise letter probability doesn't depend on position.  $$F7,F8$$ 
* I would offer to use the same OCR model for single character. But for some reason, Daphna doesn't do it (TBD)

So, to evaluate parameters we will use the following model

![full graph](https://simonrus.github.io/about/assets/img/2020-07_PGM_p2_week2_drawing2.inkspace.svg "Graph")

What is the total number of parameters in traing model?
$$card(F_{train}) = 26 + 2 * 26 * 32 + 26 * 26 = 2366$$

