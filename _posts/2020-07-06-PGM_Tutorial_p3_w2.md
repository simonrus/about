---
layout: post
title: "PGM (p3.week2)"
author: "Sergei Semenov"
categories: life
image: 2020-07-PGM_Logo.jpg
---

# Number of parameters as CPD model

## Factor graph
We have the MN with the following structure
$$
F(Y_1, Y_2, Y_3 | X_1, X_2, X_3) = F1(Y_1) * F2(Y_2) * F3(Y_3) * F4(Y_1 | X_1) * F5(Y_2 | X_2) * F6(Y_2 | X_2) * F7 (Y_1, Y_2)* F8 (Y_2, Y_3)
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

Oops, that's too much. Lets try to reduce total ammount

## Declare some factors as shared params

