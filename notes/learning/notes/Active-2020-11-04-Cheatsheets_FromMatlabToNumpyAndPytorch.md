---
title: Active-2020-11-04-Cheatsheets_FromMatlabToNumpyAndPytorch
created: '2020-10-07T11:26:31.667Z'
modified: '2020-11-04T20:58:09.422Z'
---

# Active-2020-11-04-Cheatsheets_FromMatlabToNumpyAndPytorch

---
layout: post
title: "Cheat sheets: From Matlab to Numpy and Pytorch"
author: "Sergei Semenov"
categories: cheatsheets
image: 2020-11-04-Cheatsheets_FromMatlabToNumpyAndPytorch.jpg
---
# Introduction

# Tensors
## Construction
| Matlab  	|  Numpy 	|  Pytorch 	|
|:-:	|:-:	|:-:	|
|    	|   	| torch.empty(5, 3)	|
|    	|   	| torch.rand(5, 3)	|
|    	|   	| torch.zeros(5, 3)	|
|    	|   	| torch.ones(5, 3)	|

## Convert from From other types (using using pre-existing)
Or from python list or np.array (MAKES COPY!)
```python
torch.tensor([[1., -1.], [1., -1.]])
torch.tensor(np.array([[1, 2, 3], [4, 5, 6]]))

# Other option
a = np.ones(5)
torch.from_numpy(a)
```

## Tensory copy with new size 
```python
tensor = torch.ones((2,), dtype=torch.float64)
tensor.new_full((3, 4), 3.141592)
```

## Option: requires_grad (Autograd)
Use autograd option (requires_grad=true) to add tensor in computational network 
(gradients)
```python
t1 = torch.randn((3,3), requires_grad = True) 

#remove from compuations 
t1.detach()
```

## Options: torch.device

Select device to store tensor

## Option: torch.dtype

| Torch  	|  CPU tensor 	|  Cuda Tensor 	|
|:-:	|:-:	|:-:	|
| torch.bfloat16 | torch.BFloat16Tensor	| torch.cuda.BFloat16Tensor	|
| torch.float | torch.FloatTensor | torch.cuda.FloatTensor |
| torch.uint8 | torch.ByteTensor | torch.cuda.ByteTensor |
| torch.bool | torch.BoolTensor | torch.cuda.BoolTensor |


## Template

| Matlab  	|  Numpy 	|  Pytorch 	|
|:-:	|:-:	|:-:	|
|   	|   	|   	|
|   	|   	|   	|
|   	|   	|   	|
|   	|   	|   	|
|   	|   	|   	|
|   	|   	|   	|
|   	|   	|   	|


# References
1. [https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html](https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html)
2. [https://blog.paperspace.com/pytorch-101-understanding-graphs-and-automatic-differentiation/](https://blog.paperspace.com/pytorch-101-understanding-graphs-and-automatic-differentiation/)

