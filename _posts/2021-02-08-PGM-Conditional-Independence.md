---
layout: post
title: "Conditional Independence and it's properties"
author: "Sergei Semenov"
categories: learning
image: 2020-07-PGM_Logo.jpg
---

# Introduction
Instead of discussing an independence between events, we will focus on the generalization of independence to sets of random variables.

Let's start with key definitions.

# Definitions
**Def (Conditional Independence)**: $$X \perp Y \mid Z 	\Leftrightarrow P(X,Y \mid Z) = P(X\mid Z) P(Y \mid Z)$$

*Note: We use $$\perp$$ symbol instead of $$\perp \!\!\! \perp$$ just for simplicity*

**Proposition**: if $$(X \perp Y \mid Z)$$ then $$P(X \mid  YZ) = P(X \mid Z)$$

Proof: By definition of Conditional Independence we have:

$$P(X,Y \mid Z) = P(X\mid Z) P(Y \mid Z)$$

On the other hand we may ise chain rule :

$$P(X,Y \mid Z) = P(X\mid Y,Z) P(Y \mid Z)$$

Now we can compare both sides and it is clear that $$P(X \mid  YZ) = P(X \mid Z)$$#


# Properties
#### __1.Symmetry__: $$(X \perp Y \mid Z) \Rightarrow (Y \perp X \mid Z)$$
   
#### __2.Decomposition__: 
$$(X \perp Y, W \mid Z) \Rightarrow (X \perp Y \mid Z)$$ or
$$(X \perp Y, W \mid Z) \Rightarrow (X \perp W \mid Z)$$

##### Proof
$$(X \perp Y, W \mid Z) \Rightarrow \\ \Rightarrow P(X, Y, W \mid Z) =P(X \mid Z)\cdot P(Y,W \mid Z)\Leftrightarrow \\ \Leftrightarrow \sum\limits_{W}P(X, Y, W \mid Z) = \sum\limits_{W} P(X \mid Z)\cdot P(Y,W \mid Z)\Leftrightarrow \\ \Leftrightarrow P(X, Y\mid Z) = P(X \mid Z)\sum\limits_{W}  P(Y,W \mid Z) \Leftrightarrow \\ \Leftrightarrow P(X, Y\mid Z) = P(X \mid Z)P(Y \mid Z) \Rightarrow \\ \Rightarrow (X \perp Y \mid Z)$$ #

#### __3.Weak union__
$$(X \perp Y, W \mid Z) \Rightarrow(X \perp Y \mid Z, W)$$

##### Proof
Using Chain rule(1), Decomposition property(2) and proposition of Conditional Independency (3),  we may write:

$$P(X,Y \mid W, Z) \stackrel{(1)}{=}P(X \mid W, Z, Y) P(Y \mid W, Z) \stackrel{(2)}{=} \\ \stackrel{(2)}{=} P(X \mid Z) P(Y \mid W, Z) \stackrel{(3)}{=} P(X \mid W, Z) P(Y \mid W, Z)$$ #

#### __4.Contraction__
$$(X \perp W \mid Z, Y) \&(X \perp Y \mid Z) \Rightarrow(X \perp Y, W \mid Z)$$

##### Proof: 
$$(X \perp W \mid Z, Y) \Rightarrow \\ \Rightarrow P(X, W\mid Z, Y) = P(X\mid Z, Y) \cdot P(W\mid Z,Y)\Leftrightarrow \\ \Leftrightarrow \frac{P(X,W,Y \mid Z)}{P(Y \mid Z)}=\frac{P(X,Y \mid Z)}{P(Y \mid Z)}\frac{P(W,Y \mid Z)}{P(Y \mid Z)}\Leftrightarrow \\ \Leftrightarrow \frac{P(X,W,Y \mid Z)}{P(Y \mid Z)}=\frac{P(X \mid Z)P(Y \mid Z)}{P(Y \mid Z)}\frac{P(W,Y \mid Z)}{P(Y \mid Z)}\Leftrightarrow \\ \Leftrightarrow \frac{P(X,W,Y \mid Z)}{P(Y \mid Z)}=P(X \mid Z)\frac{P(W,Y \mid Z)}{P(Y \mid Z)}\Leftrightarrow \\ \Leftrightarrow P(X,W,Y \mid Z)=P(X \mid Z)P(W,Y \mid Z)\Rightarrow \\ \Rightarrow X \perp W,Y \mid Z$$ #

#### __5.Intersection__
$$(X \perp Y \mid Z, W) \&(X \perp W \mid Z, Y) \Longrightarrow(X \perp Y, W \mid Z)$$

##### Proof: 
Using independency, we may write:
$$P(X \mid Z, W) = P(X  \mid Z, W, Y) = P(X  \mid Z, Y)\Leftrightarrow \\ \Leftrightarrow \frac{P(X, W \mid Z)}{P(W \mid Z)} = \frac{P(X,Z \mid Y)}{P(Y \mid Z)}\Leftrightarrow \\ \Leftrightarrow P(X, W \mid Z)P(Y \mid Z) = P(X,Z \mid Y)P(W \mid Z)$$

Marginalizing over $$W$$ gives us:
$$P(X \mid Z) P(Y \mid Z) = P(X, Y \mid Z)$$ or $$(X \perp Y \mid Z)$$

After applying __contraction property (see above)__ we get: $$(X \perp Y, W \mid Z)$$ #


# Conclusion
The proofs of Contraction and Intersection were hard for me. Solutions were found on [3]

# References
1. D. Koller and N. Friedman, Probabilistic graphical models: principles and techniques. Cambridge, MA: MIT Press, 2009.
2. [Probabilistic Graphical Models 1: Representation, Conditional Independence](https://www.coursera.org/learn/probabilistic-graphical-models/lecture/PTXfn/conditional-independence)
3. [Proofs for conditiona independence properties](https://math.stackexchange.com/questions/855002/what-does-the-decomposition-weak-union-and-contraction-rule-mean-for-conditiona/1474274#1474274?newreg=846a45c4381943e0a9e21803cbf1e15b)

*Last update:09 February 2021*
