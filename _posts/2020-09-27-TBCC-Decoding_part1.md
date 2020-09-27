---
layout: post
title: "Decoding TBCC (part 1)"
author: "Sergei Semenov"
categories: fec
image: TBCC_Logo.jpg
---

# Introduction
Tailbiting convolutional codes (TBCC) are widely used (PDCCH LTE, 802.11), because they:
* can be represented as quasi-cyclic block codes;
* have equal error protection over all bits if we compare with truncated construction;
* allow easy rate matching.

The main drawback of TBCC is an additional decoding complexity. Decoder (e.g. Viterbi) shall know/predict the starting state in a trellis. In this series of posts I will provide an overview of main existing methods/ideas and patents.

# Notation
The following notation will be used
* $$m$$ - constraints length
* $$R = \frac{K}{N}$$ - rate
* $$K$$ - number of shift registers used (let's assume we use controller canonical form)

 Note: "Controller canonical form" has encoder implementation with $$K$$ registers and $$N$$ adders. The other known form is "Observer canonical form@. It is done with $$N$$ shift registers and $$K$$ adders.

# Reference Decoder 
Well, as the reference decoder we will use Viterbi decoder, that starts on every possible starting state. The decoding result
is a closest codeword sequence over all possible runs.

Total required Viterbi runs is $$2^{mK}$$

# (1986) Article "On Tail Biting Convolutional Codes" by H. MA, J. Wolf 
[Source on IEEE](http://ieeexplore.ieee.org/document/1096498/)
DOI: 10.1109/TCOM.1986.1096498

This article compares solution from Bard-David with author's one. 
## Bard-David (1982)
Algorithm offers custom steps order and has following steps:
1. Choose an arbitrary starting state and Decode using a maximum likelihood decoder. 
2. Check if the starting state is the same as the ending state. If yes, stop, otherwise go to step 3.
3. Use the previous ending state as the new starting state.

## Two-step scheme
Author (H.Ma) provides own steps order, based on continued fractions list. The algorithm does the following:
1. Obtain ordered list of $$2^{mK}$$ starting state using an algebraic method called "continued fractions". The method is described in PhD and, unfortunately,not available
2. Run with starting state from list until found

![simulation_results](https://simonrus.github.io/about/assets/img/2020-09-27-TBCC-Decoding_part1_hma_simulation_results.png)

# TBD


*Last update:27 September 2020*
