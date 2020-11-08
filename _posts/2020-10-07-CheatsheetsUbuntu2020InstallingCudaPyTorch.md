---
layout: post
title: "Cheat sheet: Installing Cuda and PyTorch on Ubuntu 2020"
author: "Sergei Semenov"
categories: cheatsheets
image: 2020-10-07-Cheatsheets_Ubuntu2020_Installing_Cuda_PyTorch.jpg
---
# Introduction
One can follow the next steps to install Anaconda + pytorch with enabled GPU

# Installing Cuda 
```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget http://developer.download.nvidia.com/compute/cuda/11.0.2/local_installers/cuda-repo-ubuntu2004-11-0-local_11.0.2-450.51.05-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2004-11-0-local_11.0.2-450.51.05-1_amd64.deb
sudo apt-key add /var/cuda-repo-ubuntu2004-11-0-local/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda
```

# Installing NVidia drivers
```bash
ubuntu-drivers devices
sudo apt-get install nvidia-driver-450
echo 'export PATH=/usr/local/cuda/bin$${PATH:+:$${PATH}}' >> ~/.bashrc
nvcc --version
```

# > SM50 support with Anaconda (Cuda 10.2 will be used instead of 11.00 - TB fixed later) 
There are alread compiled binaries for pytorch 
```bash
conda create --name pytorch
conda activate pytorch
conda install pytorch torchvision cudatoolkit=11.0 -c pytorch 
```

# SM35 Support and Anacoda
Old cuda version (e.g. SM3.5, as I have on NVIDIA TITAN) is not supported by pytorch.
We need to install it from binaries

```bash
conda create -n pytorch python=3.8
source ~/bin/anaconda.sh && conda activate pytorch
conda install numpy ninja pyyaml mkl mkl-include setuptools cmake cffi typing_extensions future six requests dataclasses
conda install -c pytorch magma-cuda110

git clone --recursive https://github.com/pytorch/pytorch
cd pytorch
# if you are updating an existing checkout
git submodule sync
git submodule update --init --recursive

export CMAKE_PREFIX_PATH=$${CONDA_PREFIX:-"$$(dirname $$(which conda))/../"}
#Next step takes 20-30 minutes
python setup.py install
```

# Use with google colab (WOW)
```bash
jupyter notebook   --NotebookApp.allow_origin='https://colab.research.google.com'   --port=8889   --NotebookApp.port_retries=0
```
copy and past link to colab

# But how to merry it with git??
TBD
```
[https://medium.com/@ashwindesilva/how-to-use-google-colaboratory-to-clone-a-github-repository-e07cf8d3d22b](https://medium.com/@ashwindesilva/how-to-use-google-colaboratory-to-clone-a-github-repository-e07cf8d3d22b)
```


# Links
1. [https://linuxconfig.org/how-to-install-cuda-on-ubuntu-20-04-focal-fossa-linux](https://linuxconfig.org/how-to-install-cuda-on-ubuntu-20-04-focal-fossa-linux)
2. [https://timoast.github.io/blog/installing-pytorch/](https://timoast.github.io/blog/installing-pytorch/)
3. [https://github.com/pytorch/pytorch#from-source](https://github.com/pytorch/pytorch#from-source)


*Last update:08 November 2020*
