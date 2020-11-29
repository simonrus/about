---
layout: post
title: "Cheat sheets: Yocto training"
author: "Sergei Semenov"
categories: cheatsheets
image: Yocto-logo.png
---

## HINTS
*Ctrl-a,a,Ctrl-x* - Exit picocom

# Yocto
## Prepare 
### Terminal
```
picocom -b 115200 /dev/ttyUSB0
```
### TFTP Server (Docker way)
Source: https://hub.docker.com/r/pghalliday/tftp/
```
docker run -d --name tftp_server -p 0.0.0.0:69:69/udp -v /home/simon/work/yocto-training/__output/tftpboot:/var/tftpboot -i -t pghalliday/tftp 
```

How to check
```
tftp
```

How to shutdown
```
docker container stop tftp_server
docker container rm tftp_server
```


### NFS Server (Docker way) with v3 support
https://hub.docker.com/r/erichough/nfs-server/
docker pull erichough/nfs-server
```
sudo modprobe {nfs,nfsd}
docker -d run --name nfs_server --privileged -v /home/simon/work/yocto-training/__output/rootfs/:/nfs -v  /home/simon/work/yocto-training/__output/exports:/etc/exports:ro -p 2049:2049 -p 2049:2049/udp -p 111:111 -p 111:111/udp -p 32765:32765 -p 32765:32765/udp -p 32767:32767 -p 32767:32767/udp erichough/nfs-server
```
  
How to check from <host> machine: 
```
sudo mount -v -o vers=3,loud localhost:/nfs ./nfs/
```
  
How to shutdown
```
docker container stop nfs_server
docker container rm nfs_server
```

## Testing with community image
### getting default image
```
wget https://rcn-ee.com/rootfs/bb.org/testing/2020-04-06/buster-console/bone-debian-10.3-console-armhf-2020-04-06-1gb.img.xz
unxz < ./bone-debian-10.3-console-armhf-2020-04-06-1gb.img.xz > ./bone-debian-10.3-console-armhf-2020-04-06-1gb.img
sudo mount -o loop,offset=4194304 bone-debian-10.3-console-armhf-2020-04-06-1gb.img ./squashfs/

```
copy to tftp server zImage2 and dtb2.dtb

### UBoot Settings with pred
```
setenv ipaddr 192.168.0.100
setenv serverip 192.168.0.111
tftp $${loadaddr} zImage2
tftp $${fdtaddr} dtb2.dtb
setenv bootargs console=ttyO0,115200n8 root=/dev/nfs rw nfsroot=192.168.0.111:/,nolock, wsize=1024, rsize=1024 rootwait init=/linuxrc ip=192.168.0.100
bootz $${kern_addr} - $${fdtaddr}
```


https://clarkli86.wordpress.com/2015/08/18/nfs-boot-beaglebone-black/

## UBoot Settings
```
setenv ipaddr 192.168.0.100
setenv serverip 192.168.0.111
tftp $${loadaddr} zImage
tftp $${fdtaddr} am335x-boneblack.dtb
setenv bootargs console=ttyO0,115200n8 root=/dev/nfs rw nfsroot=192.168.0.111:/nfs,nolock, wsize=1024, rsize=1024,nfsvers=3 rootwait init=/linuxrc ip=192.168.0.100
bootz $${kern_addr} - $${fdtaddr}
```


*Last update:29 November 2020*
