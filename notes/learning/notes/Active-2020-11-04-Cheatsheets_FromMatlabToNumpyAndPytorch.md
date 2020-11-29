---
title: Active-2020-11-04-Cheatsheets_FromMatlabToNumpyAndPytorch
created: '2020-10-07T11:26:31.667Z'
modified: '2020-11-29T07:24:20.261Z'
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

# Matrices/Tensors
## Construction
| Matlab  	|  Numpy 	|  Pytorch 	|
|:-:	|:-:	|:-:	|
| NaN(5, 3)	 | np.ones([5,3]) * np.nan | torch.empty(5, 3)	|
| rand(5, 3) |  np.random.rand(5,3) 	| torch.rand(5, 3)	|
| zeros(5, 3)	|  np.zeros([5,3]) 	| torch.zeros(5, 3)	|
| ones(5, 3) |  np.ones([5,3]) 	| torch.ones(5, 3)	|

## Convert from other types using using pre-existing tensor
Or from python list or np.array (MAKES COPY!)
```python
torch.tensor([[1., -1.], [1., -1.]])
torch.tensor(np.array([[1, 2, 3], [4, 5, 6]]))

# Other option
a = np.ones(5)
torch.from_numpy(a)
```

## Tensor copy with a new size 
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

# Shapes
| Matlab  	|  Numpy 	|  Pytorch 	|
|:-:	|:-:	|:-:	|
| reshape(x,3,4)	|  x.reshape(3,4,order=’F’).copy()  	| view  	|



## Template
This document will be updated regulary
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
3. [https://numpy.org/doc/stable/user/numpy-for-matlab-users.html](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)

