---
title: Draft-2020-08-07-PGM-Structure-Learning-BayesianScores
created: '2020-08-04T06:10:52.700Z'
modified: '2020-08-05T09:50:30.510Z'
---

# Draft-2020-08-07-PGM-Structure-Learning-BayesianScores

---
layout: post
title: "Marginal likelihood: BayesNets"
author: "Sergei Semenov"
categories: learning
image: 2020-07-PGM_Logo.jpg
---


http://www.pachecoj.com/courses/csc665-1/schedule.html

$$P(\mathcal{D} \mid \mathcal{G})=\int P\left(\mathcal{D} \mid \mathcal{G}, \boldsymbol{\theta}_{\mathcal{G}}\right) \underbrace{P\left(\boldsymbol{\theta}_{\mathcal{G}} \mid \mathcal{G}\right) d \boldsymbol{\theta}_{\mathcal{G}}}$$

$$P(\mathcal{D} \mid \mathcal{G})=\prod_{i} \prod_{u_{i} \in \operatorname{Val}\left(\mathbf{P a}_{X_{i}}^{G}\right)} \frac{\Gamma\left(\alpha_{X_{i} \mid \boldsymbol{u}_{i}}\right)}{\Gamma\left(\alpha_{X_{i} \mid \boldsymbol{u}_{i}}+M\left[\boldsymbol{u}_{i}\right]\right)} \prod_{x_{i}^{j} \in \operatorname{Val}\left(X_{i}\right)}\left[\frac{\Gamma\left(\alpha_{x_{i}^{j} \mid \boldsymbol{u}_{i}}+M\left[x_{i}^{j}, \boldsymbol{u}_{i}\right]\right)}{\Gamma\left(\alpha_{x_{i}^{j} \mid \boldsymbol{u}_{i}}\right)}\right]$$
