---
title: Active-2020-10-07-CheatsheetsUbuntu2020InstallingCudaPyTorch
created: '2020-10-07T11:26:31.667Z'
modified: '2020-10-07T12:07:43.356Z'
---

# Active-2020-10-07-Cheatsheets_Ubuntu2020_Installing_Cuda_PyTorch

---
layout: post
title: "Cheetsheet: Installing Cuda and PyTorch on Ubuntu 2020"
author: "Sergei Semenov"
categories: cheatsheets
image: 2020-10-07-Cheatsheets_Ubuntu2020_Installing_Cuda_PyTorch.jpg
---
# Introduction
One can follow the next steps to install Anaconda + pytorch that uses GPU

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
echo 'export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}' >> ~/.bashrc
nvcc --version
```

# Anaconda (Cuda 10.2 will be used instead of 11.00 - TB fixed later)
```bash
conda create --name pytorch
conda activate pytorch
conda install pytorch torchvision cudatoolkit=10.2 -c pytorch 
```

# Links
1. [https://linuxconfig.org/how-to-install-cuda-on-ubuntu-20-04-focal-fossa-linux](https://linuxconfig.org/how-to-install-cuda-on-ubuntu-20-04-focal-fossa-linux)
2. [https://timoast.github.io/blog/installing-pytorch/](https://timoast.github.io/blog/installing-pytorch/)

