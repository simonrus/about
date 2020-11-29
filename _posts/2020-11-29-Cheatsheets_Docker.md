---
layout: post
title: "Cheat sheets: Docker"
author: "Sergei Semenov"
categories: cheatsheets
image: Docker_Moby-logo.png
---

# Maintain images and containers
```
docker image ls
docker image rm
docker container ls
docker container rm <HASH>
```

# normal mode 
```
#echo can be -t option ...
docker run --name <name> 
docker stop <name>
docker rm <name>
```

# Problems ??
```
docker ps -a
docker exec -it <name> /bin/bash
```



*Last update:29 November 2020*
