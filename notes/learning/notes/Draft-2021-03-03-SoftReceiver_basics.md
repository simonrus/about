---
title: Draft-2021-03-03-SoftReceiver_basics
created: '2021-03-03T07:50:46.337Z'
modified: '2021-03-04T07:41:34.554Z'
---

# Draft-2021-03-03-SoftReceiver_basics

---
layout: post
title: "Receiver Basics"
author: "Sergei Semenov"
categories: fec sp
image: 2020-12_BCJR_Trellis_Alphas.svg
---
# Receiver basics

## Gaussian distribution
$X = \mathcal{N} (\mu, \sigma)$

$$
\operatorname{PDF}(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{ -\frac{(x-\mu)^2}{2 \sigma^2} }.
$$

$$
\operatorname{CDF}(x) = \frac{1}{2}\left[1 + \operatorname{erf}\left( \frac{x-\mu}{\sigma\sqrt{2}}\right)\right]
$$
where
$$
erf(x) = \frac{1}{\sqrt\pi}\int_{-x}^x e^{-t^2} \,dt = \frac{2}{\sqrt\pi}\int_0^x e^{-t^2}\,dt.
$$

## BPSK case

For the transmitted 0:
$$
P(x = 1 | y) = \frac{P(y | x = 1) * P(x = 1)}{\sum \limits_{x_i={-1,1}} P(y | x_i) * P(x_i)} = 
\frac{L(y)}{L(y) + 1}
$$
where
$$
L(y) = \frac{\frac{1}{\sigma\sqrt{2\pi}} e^{ -\frac{(x-1)^2}{2 \sigma^2} }}{\frac{1}{\sigma\sqrt{2\pi}} {e^{ -\frac{(x+1)^2}{2 \sigma^2} }}}  = ... = \operatorname{exp}(\frac{2y}{\sigma^2})
$$

For the transmitted 0:
$$
P(x = 0 | y) = \frac{1}{L(y) + 1}
$$

# References 
1. https://www.gaussianwaves.com/2015/06/how-to-generate-awgn-noise-in-matlaboctave-without-using-in-built-awgn-function/

1. L. R. Rabiner, “A tutorial on hidden Markov models and selected applications in speech recognition,” Proc. IEEE, vol. 77, no. 2, pp. 257–286, Feb. 1989, doi: 10.1109/5.18626.
2. L. Bahl, J. Cocke, F. Jelinek, and J. Raviv, “Optimal decoding of linear codes for minimizing symbol error rate (Corresp.),” IEEE Trans. Inform. Theory, vol. 20, no. 2, pp. 284–287, Mar. 1974, doi: 10.1109/TIT.1974.1055186.





